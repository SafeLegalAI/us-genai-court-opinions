#!/usr/bin/env python3
"""Carry the state-court resolver findings (work/resolve/results-*.jsonl) onto the source rows.

Resolved rows were already upgraded in place by the agents. This step records the *misses*
so a reader of the row can see what was checked and when:
  not-published → "Official copy not published online as of <date> (checked <hosts>)."
  not-found     → the agent's note (court site blocks automated access / host timed out / …)
and replaces the bare "official copy pending" phrase where a dated finding now exists.

Usage: python pipeline/apply_resolve_notes.py [--write]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "work" / "agents"
RESOLVE = ROOT / "work" / "resolve"
PENDING_RE = re.compile(r"\s*(?:;|\.)?\s*[Oo]fficial copy (?:is )?pending\.?")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    files = {f: [json.loads(l) for l in f.read_text().splitlines() if l.strip()] for f in sorted(AGENTS.glob("decisions-*.jsonl"))}
    by_id = {r["decision_id"]: r for rows in files.values() for r in rows}

    findings = {}
    # Federal rows the GovInfo/CourtListener script could not place (latest verdict per row wins).
    for f in sorted(RESOLVE.glob("log*.jsonl")):
        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            d = json.loads(line)
            if d.get("result") == "not-found":
                routes = d.get("routes") or ["govinfo"]
                hosts = [{"govinfo": "govinfo.gov (USCOURTS)", "courtlistener": "CourtListener RECAP search"}.get(r, r) for r in routes]
                findings[d["decision_id"]] = {"decision_id": d["decision_id"], "status": "not-found", "checked": hosts, "ts": d.get("ts"),
                                              "note": "not in the court's GovInfo feed for this docket (many district courts publish only some orders)"}
            elif d.get("result") == "upgraded":
                findings[d["decision_id"]] = {"decision_id": d["decision_id"], "status": "resolved"}
    for f in sorted(RESOLVE.glob("results-*.jsonl")):
        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            d = json.loads(line)
            findings[d["decision_id"]] = d

    changed = 0
    by_status = {}
    for did, d in findings.items():
        row = by_id.get(did)
        if not row:
            continue
        st = d.get("status")
        by_status[st] = by_status.get(st, 0) + 1
        if st == "resolved":
            continue
        ts = (d.get("checked_at") or d.get("ts") or "2026-09-08")[:10]
        hosts = ", ".join(d.get("checked") or []) or "court site"
        note = (d.get("note") or "").strip().rstrip(".")
        if st == "not-published":
            finding = f"Official copy not published online as of {ts} (checked {hosts})."
        else:
            finding = f"Official copy not obtained {ts}: {note} (checked {hosts})." if note else f"Official copy not obtained {ts} (checked {hosts})."
        notes = row.get("notes") or ""
        if finding in notes:
            continue
        notes = PENDING_RE.sub("", notes).strip()
        # Drop an earlier undated finding for the same row so the note does not accumulate.
        notes = re.sub(r"\s*Official copy not (?:published online|obtained)[^.]*\.(?:[^.]*\.)?", "", notes).strip()
        row["notes"] = (notes + " " + finding).strip() if notes else finding
        changed += 1

    print(f"findings: {len(findings)} {by_status} · rows annotated: {changed}")
    if a.write:
        for f, rows in files.items():
            f.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
        print("written")
    else:
        print("(dry run — pass --write to apply)")


if __name__ == "__main__":
    main()
