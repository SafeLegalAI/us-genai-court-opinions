#!/usr/bin/env python3
"""Apply re-coding overlays (work/recode/recode-*.jsonl) to work/agents/decisions-*.jsonl.

Each overlay object carries `decision_id`, `recode_status` and a subset of row fields as
defined in work/recode/RUBRIC.md. Only rows with recode_status == "recoded" change the
source; other statuses are logged. Fields are validated against the schema enums before
anything is written. A change log (work/recode/applied-<date>.jsonl) records every field
that changed, old → new, so the release notes can state exactly what moved.

Usage:
  python pipeline/apply_recode.py            # dry run: report what would change
  python pipeline/apply_recode.py --write    # apply
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "work" / "agents"
RECODE = ROOT / "work" / "recode"
SCHEMA = json.loads((ROOT / "schema" / "decisions.schema.json").read_text())

TOP_FIELDS = (
    "case_name", "court", "docket_number", "citation", "date_filed", "document_type",
    "ai_mention", "ai_passage", "primary_topic", "topics", "court_used_ai", "disposition",
)
INCIDENT_FIELDS = ("actor", "ai_tool", "conduct", "outcome", "monetary_penalty", "currency")

ENUM = {
    "document_type": set(SCHEMA["properties"]["document_type"]["enum"]),
    "ai_mention": set(SCHEMA["properties"]["ai_mention"]["enum"]),
    "primary_topic": set(SCHEMA["properties"]["primary_topic"]["enum"]),
    "topics": set(SCHEMA["properties"]["topics"]["items"]["enum"]),
    "outcome": set(SCHEMA["properties"]["incident"]["properties"]["outcome"]["enum"]),
    "actor": set(SCHEMA["properties"]["incident"]["properties"]["actor"]["enum"]),
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# Docket strings that are sentence fragments rather than identifiers.
BAD_DOCKET_RE = re.compile(r"\b(the|and|court|plaintiff|defendant|motion|order|filed|because|that)\b", re.I)
# Words whose presence shows a passage carries the court's AI reference.
AI_RE = re.compile(r"artificial intelligence|\bAI\b|A\.I\.|ChatGPT|chatbot|large language model|\bLLM|generative|hallucinat|Gemini|Copilot|Claude|Bard\b|OpenAI|machine[- ]learning|algorithm", re.I)


def keep_old_passage(old: str, new: str, ai_mention: str | None) -> bool:
    """The first-pass passages were verbatim in every QA row; the fault was passages that never
    reached the court's AI reference. So the existing passage stays unless it lacks that reference
    while the court makes one, or the re-read supplies a strictly longer excerpt."""
    if not old or len(old) < 20:
        return False
    if ai_mention in ("explicit", "implied") and not AI_RE.search(old) and AI_RE.search(new or ""):
        return False
    if new and len(new) > len(old) * 1.15:
        return False
    return True


def load_rows():
    files = {}
    for f in sorted(AGENTS.glob("decisions-*.jsonl")):
        files[f] = [json.loads(l) for l in f.read_text().splitlines() if l.strip()]
    return files


def load_overlays():
    out = {}
    dupes = 0
    for f in sorted(RECODE.glob("recode-*.jsonl")):
        for n, line in enumerate(f.read_text().splitlines(), 1):
            if not line.strip():
                continue
            try:
                o = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"  ! {f.name}:{n} bad JSON: {e}", file=sys.stderr)
                continue
            if "decision_id" not in o:
                print(f"  ! {f.name}:{n} missing decision_id", file=sys.stderr)
                continue
            if o["decision_id"] in out:
                dupes += 1
            out[o["decision_id"]] = o  # last wins
    return out, dupes


def validate(o) -> list[str]:
    errs = []
    for k in ("document_type", "ai_mention", "primary_topic"):
        if k in o and o[k] is not None and o[k] not in ENUM[k]:
            errs.append(f"{k}={o[k]!r}")
    if "topics" in o:
        if not isinstance(o["topics"], list) or not o["topics"]:
            errs.append("topics not a non-empty list")
        else:
            bad = [t for t in o["topics"] if t not in ENUM["topics"]]
            if bad:
                errs.append(f"topics={bad!r}")
    if "primary_topic" in o and "topics" in o and isinstance(o["topics"], list) and o["primary_topic"] not in o["topics"]:
        errs.append("primary_topic not in topics")
    if "date_filed" in o and o["date_filed"] and not DATE_RE.match(str(o["date_filed"])):
        errs.append(f"date_filed={o['date_filed']!r}")
    if "docket_number" in o and o["docket_number"] and BAD_DOCKET_RE.search(str(o["docket_number"])):
        errs.append(f"docket looks like prose: {o['docket_number']!r}")
    if "ai_passage" in o and (not isinstance(o["ai_passage"], str) or len(o["ai_passage"]) < 20):
        errs.append("ai_passage too short")
    if "court_used_ai" in o and not isinstance(o["court_used_ai"], bool):
        errs.append("court_used_ai not bool")
    inc = o.get("incident")
    if inc is not None:
        if not isinstance(inc, dict):
            errs.append("incident not an object")
        else:
            if "outcome" in inc and inc["outcome"] not in ENUM["outcome"]:
                errs.append(f"incident.outcome={inc['outcome']!r}")
            if "actor" in inc and inc["actor"] not in ENUM["actor"]:
                errs.append(f"incident.actor={inc['actor']!r}")
            mp = inc.get("monetary_penalty")
            if mp is not None and (not isinstance(mp, (int, float)) or mp in (0, 1)):
                errs.append(f"incident.monetary_penalty={mp!r}")
            if mp is not None and not inc.get("currency"):
                errs.append("monetary_penalty without currency")
            if mp is None and inc.get("currency"):
                errs.append("currency without monetary_penalty")
        if "topics" in o and isinstance(o["topics"], list) and "fabricated-citations" not in o["topics"]:
            errs.append("incident present but topics lack fabricated-citations")
    elif "incident" in o and "topics" in o and isinstance(o["topics"], list) and "fabricated-citations" in o["topics"]:
        errs.append("fabricated-citations row with incident: null")
    return errs


def apply(row: dict, o: dict, log: list, today: str) -> int:
    changed = 0
    for k in TOP_FIELDS:
        if k not in o:
            continue
        new = o[k]
        old = row.get(k)
        if k == "topics":
            new = list(dict.fromkeys(new))
        if k == "ai_passage" and keep_old_passage(old, new, o.get("ai_mention", row.get("ai_mention"))):
            continue
        if old != new:
            log.append({"decision_id": row["decision_id"], "field": k, "old": old, "new": new})
            row[k] = new
            changed += 1
    if "incident" in o:
        new_inc = o["incident"]
        old_inc = row.get("incident")
        if new_inc is None:
            if old_inc is not None:
                log.append({"decision_id": row["decision_id"], "field": "incident", "old": old_inc, "new": None})
                row["incident"] = None
                changed += 1
        else:
            inc = dict(old_inc or {})
            for k in INCIDENT_FIELDS:
                if k in new_inc and inc.get(k) != new_inc[k]:
                    log.append({"decision_id": row["decision_id"], "field": f"incident.{k}", "old": inc.get(k), "new": new_inc[k]})
                    inc[k] = new_inc[k]
                    changed += 1
            for k in INCIDENT_FIELDS:
                inc.setdefault(k, None)
            row["incident"] = inc
            # keep the top-level tool field in step with the incident
            tool = new_inc.get("ai_tool") if "ai_tool" in new_inc else None
            if "ai_tool" in new_inc and row.get("ai_tool_named") != tool:
                log.append({"decision_id": row["decision_id"], "field": "ai_tool_named", "old": row.get("ai_tool_named"), "new": tool})
                row["ai_tool_named"] = tool
                changed += 1
    if changed:
        note = f"Re-coded from the document {today} (independent second read)."
        notes = row.get("notes") or ""
        if "Re-coded from the document" not in notes:
            row["notes"] = (notes + " " + note).strip()
    # place ai_mention after court_used_ai for readable files
    if "ai_mention" in row:
        ordered = {}
        for k, v in row.items():
            if k == "ai_mention":
                continue
            ordered[k] = v
            if k == "court_used_ai":
                ordered["ai_mention"] = row["ai_mention"]
        row.clear()
        row.update(ordered)
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    today = dt.date.today().isoformat()

    files = load_rows()
    by_id = {r["decision_id"]: (f, r) for f, rows in files.items() for r in rows}
    overlays, dupes = load_overlays()
    print(f"source rows: {len(by_id)} · overlays: {len(overlays)} (duplicates superseded: {dupes})")

    status = {}
    invalid = []
    log = []
    rows_changed = 0
    unknown = []
    for did, o in overlays.items():
        st = o.get("recode_status", "?")
        status[st] = status.get(st, 0) + 1
        if did not in by_id:
            unknown.append(did)
            continue
        if st != "recoded":
            if st == "unfetchable":
                f, row = by_id[did]
                mark = f"Second read pending: document could not be fetched {today} ({(o.get('recode_notes') or 'host unreachable').split(';')[0][:90].rstrip('.')})."
                notes = row.get("notes") or ""
                if "Second read pending" not in notes:
                    row["notes"] = (notes + " " + mark).strip()
                    log.append({"decision_id": did, "field": "notes", "old": notes, "new": row["notes"]})
                    rows_changed += 1
            continue
        errs = validate(o)
        if errs:
            invalid.append((did, errs))
            continue
        f, row = by_id[did]
        n = apply(row, o, log, today)
        if n:
            rows_changed += 1

    print(f"status: {status}")
    if unknown:
        print(f"unknown decision_ids ({len(unknown)}): {unknown[:5]}{'…' if len(unknown) > 5 else ''}")
    if invalid:
        print(f"REJECTED ({len(invalid)}) — fix the overlay, not the source:")
        for did, errs in invalid:
            print(f"  {did}: {'; '.join(errs)}")

    per_field = {}
    for e in log:
        per_field[e["field"]] = per_field.get(e["field"], 0) + 1
    print(f"rows changed: {rows_changed} · field changes: {len(log)}")
    for k, v in sorted(per_field.items(), key=lambda kv: -kv[1]):
        print(f"  {k:26s} {v}")

    outcome_moves = {}
    for e in log:
        if e["field"] == "incident.outcome":
            key = f"{e['old']} → {e['new']}"
            outcome_moves[key] = outcome_moves.get(key, 0) + 1
    if outcome_moves:
        print("outcome moves:")
        for k, v in sorted(outcome_moves.items(), key=lambda kv: -kv[1]):
            print(f"  {k:32s} {v}")

    if not a.write:
        print("\n(dry run — pass --write to apply)")
        return
    # Write field-wise onto freshly re-read lines: the official-copy resolver may have patched
    # source_url/verification/notes on the same rows while this ran, and must not be overwritten.
    changes = {}
    for e in log:
        changes.setdefault(e["decision_id"], []).append(e)
    for f in files:
        lines = f.read_text().splitlines()
        for n, line in enumerate(lines):
            if not line.strip():
                continue
            cur = json.loads(line)
            evs = changes.get(cur["decision_id"])
            if not evs:
                continue
            for e in evs:
                k = e["field"]
                if k == "notes":
                    mark = e["new"][len(e["old"]):].strip() if e["new"].startswith(e["old"]) else e["new"]
                    cur["notes"] = ((cur.get("notes") or "") + " " + mark).strip() if mark not in (cur.get("notes") or "") else cur.get("notes")
                elif k.startswith("incident."):
                    inc = dict(cur.get("incident") or {})
                    inc[k.split(".", 1)[1]] = e["new"]
                    for kk in INCIDENT_FIELDS:
                        inc.setdefault(kk, None)
                    cur["incident"] = inc
                elif k == "incident":
                    cur["incident"] = e["new"]
                else:
                    cur[k] = e["new"]
            recoded = by_id[cur["decision_id"]][1]
            if "Re-coded from the document" in (recoded.get("notes") or "") and "Re-coded from the document" not in (cur.get("notes") or ""):
                cur["notes"] = ((cur.get("notes") or "") + f" Re-coded from the document {today} (independent second read).").strip()
            if "ai_mention" in cur:
                ordered = {}
                for k, v in cur.items():
                    if k == "ai_mention":
                        continue
                    ordered[k] = v
                    if k == "court_used_ai":
                        ordered["ai_mention"] = cur["ai_mention"]
                cur = ordered
            lines[n] = json.dumps(cur, ensure_ascii=False)
        f.write_text("\n".join(lines) + "\n")
    stamp = today + "-" + dt.datetime.now().strftime("%H%M")
    (RECODE / f"applied-{stamp}.jsonl").write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in log))
    (RECODE / f"applied-{stamp}-summary.json").write_text(json.dumps({
        "date": today, "overlays": len(overlays), "status": status, "rows_changed": rows_changed,
        "field_changes": len(log), "per_field": per_field, "outcome_moves": outcome_moves,
        "rejected": [{"decision_id": d, "errors": e} for d, e in invalid], "unknown": unknown,
    }, indent=1))
    print(f"\nwritten · log: work/recode/applied-{stamp}.jsonl")


if __name__ == "__main__":
    main()
