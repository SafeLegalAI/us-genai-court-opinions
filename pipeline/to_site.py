"""Convert fabricated-citation decisions into SafeLegalAI incident-tracker records (one YAML per
decision) so each becomes a page at /tracker/<slug>, and back-fill `tracker_slug` on the dataset row.

Rules:
- only `fetched-and-read` or `mirror-read` rows (the court document was actually read — from the court's
  site or from a public mirror of it) whose topics include `fabricated-citations` and carry an `incident{}`;
  link-only rows are never converted
- every record is written with `status: provisional` — the editor flips it after re-opening the source
  (provisional incidents are noindex and excluded from counts, statistics, feeds, widgets, syndication and exports)
- a decision already in the tracker (matching `tracker_slug`, or the same source URL, or the same
  normalised case name + date) is skipped
- nothing is invented: conduct/outcome/actor/penalty come from the dataset row, which was coded from
  the court's document; `summary` is the dataset summary; the court passage is not copied (the
  tracker links to the corpus page for it)

    .venv/bin/python pipeline/to_site.py --site /path/to/safelegalai-site [--limit N] [--write-back]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as DQ

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
JUR = {True: "us-federal", False: "us-state"}
FEDERAL = {"federal-supreme", "federal-appellate", "federal-district", "federal-bankruptcy", "federal-specialty"}
COURT_LONG = {
    "federal-appellate": "US Court of Appeals",
    "federal-district": "US District Court",
    "federal-bankruptcy": "US Bankruptcy Court",
}


def slugify(s: str) -> str:
    s = re.sub(r"[’'\"]", "", s.lower())
    s = re.sub(r"\bv\.?\b", "v", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:80].rstrip("-")


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def build_record(r: dict, DQ) -> dict:
    """One provisional tracker record from a dataset row — nothing invented, every value comes from the row."""
    inc = r["incident"]
    rec = {
        "caseName": DQ(r["case_name"]),
        "date": r["date_filed"],
        "court": DQ(r["court"]),
        "jurisdiction": JUR[r["court_level"] in FEDERAL],
    }
    tool = inc.get("ai_tool") or r.get("ai_tool_named")
    if tool:
        rec["aiTool"] = DQ(tool)
    rec["conduct"] = DQ(inc["conduct"])
    rec["outcome"] = inc["outcome"]
    if inc.get("monetary_penalty"):
        rec["monetaryPenalty"] = inc["monetary_penalty"]
        rec["penaltyCurrency"] = inc.get("currency") or "USD"
    rec["actor"] = inc["actor"]
    mirror = r.get("verification") == "mirror-read"
    sources = [{"label": DQ(f"{r['document_type'].replace('-', ' ').capitalize()} ({r['court']}, {r['date_filed']}){' — public copy of the court document; the court does not publish it online or its site refuses automated access' if mirror else ''}"), "url": DQ(r["source_url"])}]
    if r.get("mirror_url") and r["mirror_url"] != r["source_url"]:
        sources.append({"label": DQ("Public copy the row was first read from"), "url": DQ(r["mirror_url"])})
    sources.append({"label": DQ("SafeLegalAI — the court's passage on AI, coded"), "url": DQ(f"https://safelegalai.com/courts/opinions/{r['decision_id']}")})
    if r.get("courtlistener_url"):
        sources.append({"label": DQ("Docket (CourtListener / RECAP)"), "url": DQ(r["courtlistener_url"])})
    rec["sources"] = sources
    summary = r["summary"]
    # the site validator requires 40–60 words; pad short summaries with facts from the row, never boilerplate judgement
    for extra in ([f"The court names {r['ai_tool_named']} as the tool."] if r.get("ai_tool_named") and r["ai_tool_named"].lower() not in summary.lower() else []) + ([f"Docket {r['docket_number']}."] if r.get("docket_number") and r["docket_number"] not in summary else []) + ([f"Reported at {r['citation']}."] if r.get("citation") and r["citation"] not in summary else []):
        if len(summary.split()) >= 40:
            break
        summary += " " + extra
    if len(summary.split()) < 40:
        summary += f" The decision is dated {r['date_filed']} and was read from a public copy of the court's document."
    if len(summary.split()) > 60:
        summary = " ".join(summary.split()[:58]).rstrip(",;:") + "."
    rec["summary"] = DQ(summary)
    rec["status"] = "provisional"
    rec["lastVerified"] = r["fetched_at"][:10]
    return rec


def refresh_provisional(rows: list, inc_dir: Path, yaml, DQ):
    """Bring every *provisional* tracker record back in line with its dataset row after a re-code:
    conduct, outcome, actor, tool, penalty, sources, summary. Verified records are never touched.
    A provisional record whose row no longer carries a fabricated-citation incident (re-coded to
    another topic, or withdrawn) is deleted — it was generated, not edited."""
    by_id = {r["decision_id"]: r for r in rows}
    by_slug = {r["tracker_slug"]: r for r in rows if r.get("tracker_slug")}
    wf = ROOT / "work" / "withdrawn.json"
    withdrawn = {w["decision_id"] for w in json.loads(wf.read_text())} if wf.exists() else set()
    refreshed, removed, kept = 0, 0, 0
    for f in sorted(inc_dir.glob("*.yaml")):
        d = yaml.load(f.read_text(encoding="utf-8"))
        if d.get("status") != "provisional":
            continue
        r = by_slug.get(f.stem)
        did = None
        if r is None:
            for s_ in d.get("sources", []):
                m = re.search(r"/courts/opinions/([a-z0-9-]+)$", s_.get("url", ""))
                if m:
                    did = m.group(1)
                    r = by_id.get(did)
                    break
        if r is None:
            if did in withdrawn:
                f.unlink()
                removed += 1
            else:
                kept += 1
            continue
        if "fabricated-citations" not in r.get("topics", []) or not r.get("incident"):
            f.unlink()
            removed += 1
            continue
        rec = build_record(r, DQ)
        cur = {k: d.get(k) for k in rec}
        if json.dumps(cur, default=str, sort_keys=True) != json.dumps(rec, default=str, sort_keys=True):
            for k in ("aiTool", "monetaryPenalty", "penaltyCurrency"):
                if k in d and k not in rec:
                    del d[k]
            for k, v in rec.items():
                d[k] = v
            with f.open("w", encoding="utf-8") as fh:
                yaml.dump(d, fh)
            refreshed += 1
    print(f"to_site: refreshed {refreshed} provisional records, removed {removed} (row re-coded away from fabricated citations, or withdrawn), left {kept} provisional records that are not from this dataset")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--write-back", action="store_true", help="write tracker_slug into work/agents rows")
    ap.add_argument("--refresh-provisional", action="store_true", help="re-derive every provisional tracker record from its (re-coded) row; verified records untouched")
    a = ap.parse_args()
    site = Path(a.site)
    inc_dir = site / "src" / "content" / "incidents"
    yaml = YAML()
    yaml.width = 4096
    existing = {}
    for f in inc_dir.glob("*.yaml"):
        d = yaml.load(f.read_text(encoding="utf-8"))
        urls = {s["url"] for s in d.get("sources", [])}
        existing[f.stem] = (norm(d["caseName"]), str(d["date"])[:10], urls)
    rows = [json.loads(l) for l in (DATA / "decisions.jsonl").open(encoding="utf-8") if l.strip()]
    written, skipped, slugs = 0, 0, {}
    for r in rows:
        if r.get("verification") not in ("fetched-and-read", "mirror-read") or "fabricated-citations" not in r.get("topics", []) or not r.get("incident"):
            continue
        if r.get("tracker_slug") and (inc_dir / f"{r['tracker_slug']}.yaml").exists():
            skipped += 1
            continue
        n = norm(r["case_name"])
        match = next((slug for slug, (cn, dt, urls) in existing.items() if r["source_url"] in urls or (cn == n and dt == r["date_filed"]) or (len(cn) > 12 and (cn in n or n in cn) and dt == r["date_filed"])), None)
        if match:
            slugs[r["decision_id"]] = match
            skipped += 1
            continue
        if a.limit and written >= a.limit:
            break
        slug = slugify(r["case_name"])
        if (inc_dir / f"{slug}.yaml").exists():
            slug = f"{slug}-{r['date_filed'][:4]}"
        rec = build_record(r, DQ)
        # the date must be a real date scalar for the content schema (z.coerce.date accepts the string)
        with (inc_dir / f"{slug}.yaml").open("w", encoding="utf-8") as fh:
            yaml.dump(rec, fh)
        existing[slug] = (n, r["date_filed"], {r["source_url"]})
        slugs[r["decision_id"]] = slug
        written += 1
    print(f"to_site: wrote {written} unverified incident records, skipped {skipped} already in the tracker")
    if a.refresh_provisional:
        refresh_provisional(rows, inc_dir, yaml, DQ)
    if a.write_back and slugs:
        for f in (ROOT / "work" / "agents").glob("decisions-*.jsonl"):
            out = []
            changed = 0
            for l in f.open(encoding="utf-8"):
                if not l.strip():
                    continue
                r = json.loads(l)
                if r.get("decision_id") in slugs and not r.get("tracker_slug"):
                    r["tracker_slug"] = slugs[r["decision_id"]]
                    changed += 1
                out.append(json.dumps(r, ensure_ascii=False))
            if changed:
                f.write_text("\n".join(out) + "\n", encoding="utf-8")
                print(f"  {f.name}: tracker_slug set on {changed} rows")
    (ROOT / "work" / "site-slugs.json").write_text(json.dumps(slugs, indent=1))


if __name__ == "__main__":
    main()
