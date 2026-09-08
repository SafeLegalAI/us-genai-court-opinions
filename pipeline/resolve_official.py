#!/usr/bin/env python3
"""Resolve `mirror-read` rows to the court's official document.

For every decision whose text was read from a public mirror (Charlotin's copy, a storage
mirror), find the same document at an official or primary repository, confirm it is the same
document by locating our quoted `ai_passage` verbatim in its text, and upgrade the row:

    source_url   → the official URL          verification → fetched-and-read
    mirror_url   → the URL we originally read (kept: per-row attribution to the lead source)
    notes        → "Official copy located <date> via <route>; passage confirmed."

Routes, in order:
  A. GovInfo (USCOURTS collection) — api.govinfo.gov search by court code + docket core, then
     the package's granule PDFs. Needs GOVINFO_API_KEY (api.data.gov; 1,000+/hour).
  B. CourtListener v4 search API — anonymous, within Free Law Project's published limits
     (5/min, 50/hour, 125/day; https://free.law/membership/allowed-api-usage/). RECAP
     documents and opinions; result URLs are storage.courtlistener.com PDFs (the public RECAP
     archive). Off unless --courtlistener; a daily cap is enforced via work/resolve/cl-quota.json.
  State courts have no common API: see work/resolve/state-queue.json for the agent queue.

Nothing is guessed: a row is upgraded only when the passage is found in the fetched document.

    python3 pipeline/resolve_official.py --dry-run            # report what would change
    python3 pipeline/resolve_official.py                      # GovInfo only
    python3 pipeline/resolve_official.py --courtlistener      # + CourtListener within limits
    python3 pipeline/resolve_official.py --only <decision_id>
"""
import argparse
import datetime as dt
import glob
import json
import os
import pathlib
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "agents"
RES = ROOT / "work" / "resolve"
RES.mkdir(parents=True, exist_ok=True)
LOG = RES / "log.jsonl"
CL_QUOTA = RES / "cl-quota.json"
UA = "SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)"
KEY = os.environ.get("GOVINFO_API_KEY", "")
TODAY = dt.date.today().isoformat()

OFFICIAL_HOSTS = ("govinfo.gov", "uscourts.gov", "storage.courtlistener.com", "courtlistener.com")


def log(**kw):
    kw["ts"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    with LOG.open("a") as f:
        f.write(json.dumps(kw, ensure_ascii=False) + "\n")


def fetch(url, timeout=60, binary=False, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
        return data if binary else data.decode("utf-8", "replace")


def pdf_text(data: bytes) -> str:
    p = RES / "tmp.pdf"
    p.write_bytes(data)
    try:
        return subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True, timeout=120).stdout
    except Exception:
        return ""


def norm(s: str) -> str:
    """Lower-case, de-hyphenate, strip page headers, then keep letters only. Court PDFs interleave
    pleading-paper line numbers, footnote markers and page headers with the text; dropping every
    digit and punctuation mark makes both sides comparable, and a 12-word letters-only window is
    still far too specific to match a different document."""
    s = s.replace("\u201c", '"').replace("\u201d", '"').replace("\u2018", "'").replace("\u2019", "'").replace("\u2014", " ").replace("\u2013", " ")
    s = re.sub(r"-\s*\n\s*", "", s)  # hyphenation at line ends
    s = re.sub(r"case \S+ document \d+ filed \d\d/\d\d/\d\d(?: pageid\.\S*)? page \d+ of \d+", " ", s, flags=re.I)
    s = re.sub(r"[^a-z ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def passage_found(passage: str, text: str) -> bool:
    """True when the quoted passage appears in the text: try successive 90-char windows of each
    segment (between ellipses) and require most windows to hit — tolerant of footnote markers,
    page breaks and small OCR differences, strict enough that a different document will not match."""
    t = norm(text)
    if not t:
        return False
    segs = [norm(x) for x in re.split(r"\s*(?:\.\.\.|…|\[\.\.\.\])\s*", passage or "") if len(x.strip()) > 40]
    if not segs:
        return False
    total, hit = 0, 0
    for seg in segs:
        words = seg.split()
        for start in range(0, max(1, len(words) - 12), 12):
            window = " ".join(words[start:start + 12])
            if len(window) < 50:
                continue
            total += 1
            if window in t:
                hit += 1
    return total > 0 and hit / total >= 0.5


# ------------------------------------------------------------------ rows

def load_rows():
    """All decision rows from the agents' files, with the file each came from."""
    out = []
    for f in sorted(WORK.glob("decisions*.jsonl")):
        for i, line in enumerate(f.read_text().splitlines()):
            if line.strip():
                out.append((f, i, json.loads(line)))
    return out


def save_row(f: pathlib.Path, idx: int, row: dict):
    lines = f.read_text().splitlines()
    lines[idx] = json.dumps(row, ensure_ascii=False)
    f.write_text("\n".join(lines) + "\n")


def patch_row(f: pathlib.Path, idx: int, changes: dict):
    """Re-read the line and change only the given fields, so a concurrent re-coding pass that edited
    other fields of the same row is not overwritten with our stale copy."""
    lines = f.read_text().splitlines()
    cur = json.loads(lines[idx])
    assert cur["decision_id"] == changes.pop("decision_id"), f"line {idx} of {f.name} moved"
    cur.update(changes)
    lines[idx] = json.dumps(cur, ensure_ascii=False)
    f.write_text("\n".join(lines) + "\n")
    return cur


def docket_core(d):
    """'1:26-cv-10860-MFL-PTM' → '26-cv-10860' ; '2:25-cv-01234' → '25-cv-01234'."""
    if not d:
        return None
    m = re.search(r"(\d{1,2})[-:](?:[a-z]{1,3}[-:])?(\d{2,5})", d.lower())
    m2 = re.search(r"\d{1,2}-(?:cv|cr|mc|md|bk|ap|md|po|mj)-\d{3,6}", d.lower())
    if m2:
        return m2.group(0)
    return None


# ------------------------------------------------------------------ route A: GovInfo

def govinfo_search(query: str, size=10):
    body = json.dumps({"query": query, "pageSize": size, "offsetMark": "*", "resultLevel": "default"}).encode()
    req = urllib.request.Request(f"https://api.govinfo.gov/search?api_key={KEY}", data=body, headers={"Content-Type": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def govinfo_granules(pkg: str):
    d = json.loads(fetch(f"https://api.govinfo.gov/packages/{pkg}/granules?offsetMark=*&pageSize=50&api_key={KEY}"))
    return [g["granuleId"] for g in d.get("granules", [])]


def route_govinfo(row: dict):
    code = row.get("court_code")
    core = docket_core(row.get("docket_number"))
    if not code or not KEY:
        return None
    queries = []
    if core:
        queries.append(f"collection:USCOURTS courtcode:{code} {core}")  # unquoted: GovInfo's phrase matching breaks on docket strings
    words = [w for w in re.findall(r"[A-Za-z]{4,}", row.get("case_name") or "") if w.lower() not in {"united", "states", "america", "inc", "llc", "corp", "county", "city", "state", "department", "board", "company", "district"}][:3]
    if words:
        queries.append(f"collection:USCOURTS courtcode:{code} " + " ".join(words))
    for q in queries:
        try:
            res = govinfo_search(q)
        except Exception as e:
            log(route="govinfo", decision_id=row["decision_id"], query=q, error=str(e)[:200])
            continue
        hits = res.get("results", [])[:8]
        if core:
            tag = core.replace("-", "_")  # 26-cv-00029 → 26_cv_00029 as GovInfo writes package ids
            hits.sort(key=lambda h: 0 if tag in (h.get("packageId") or "") else 1)
        seen = set()
        for hit in hits:
            pkg = hit.get("packageId")
            if not pkg or pkg in seen:
                continue
            seen.add(pkg)
            try:
                granules = govinfo_granules(pkg)
            except Exception as e:
                log(route="govinfo", decision_id=row["decision_id"], pkg=pkg, error=str(e)[:200])
                continue
            for g in sorted(granules, reverse=True)[:12]:  # newest granule first: the AI order is usually the latest filing
                url = f"https://www.govinfo.gov/content/pkg/{pkg}/pdf/{g}.pdf"
                try:
                    data = fetch(url, binary=True)
                except Exception:
                    continue
                if passage_found(row.get("ai_passage") or "", pdf_text(data)):
                    return {"official_url": url, "route": "govinfo", "package": pkg, "granule": g, "query": q}
                time.sleep(0.2)
    return None


# ------------------------------------------------------------------ route B: CourtListener (within published limits)

def cl_quota_ok():
    q = json.loads(CL_QUOTA.read_text()) if CL_QUOTA.exists() else {}
    if q.get("date") != TODAY:
        q = {"date": TODAY, "count": 0, "hour": dt.datetime.now(dt.timezone.utc).hour, "hour_count": 0}
    if dt.datetime.now(dt.timezone.utc).hour != q.get("hour"):
        q["hour"], q["hour_count"] = dt.datetime.now(dt.timezone.utc).hour, 0
    if q["count"] >= 120:
        return "day", q
    if q["hour_count"] >= 48:
        return "hour", q
    return True, q


def cl_bump(q):
    q["count"] += 1
    q["hour_count"] += 1
    CL_QUOTA.write_text(json.dumps(q))
    time.sleep(13)  # ≤5 requests/minute


def route_courtlistener(row: dict):
    ok, q = cl_quota_ok()
    if ok == "day":
        return "quota"
    if ok == "hour":
        # hourly cap reached: wait for the next hour rather than give up the day's budget
        now = dt.datetime.now(dt.timezone.utc)
        wait = 60 * (60 - now.minute) + 5
        print(f"  … CourtListener hourly cap reached; sleeping {wait // 60} min", flush=True)
        time.sleep(wait)
        ok, q = cl_quota_ok()
        if ok is not True:
            return "quota"
    core = docket_core(row.get("docket_number"))
    code = row.get("court_code")
    if not (core and code):
        return None
    url = "https://www.courtlistener.com/api/rest/v4/search/?" + urllib.parse.urlencode({"type": "r", "q": f'docketNumber:"{core}"', "court": code, "order_by": "score desc"})
    try:
        res = json.loads(fetch(url, headers={"Accept": "application/json"}))
    except Exception as e:
        cl_bump(q)
        log(route="courtlistener", decision_id=row["decision_id"], error=str(e)[:200])
        return None
    cl_bump(q)
    for docket in res.get("results", [])[:3]:
        for doc in docket.get("recap_documents", [])[:15]:
            path = doc.get("filepath_local")
            if not path or not doc.get("is_available"):
                continue
            pdf_url = f"https://storage.courtlistener.com/{path}"
            time.sleep(2)  # storage is a public archive, still be gentle
            try:
                data = fetch(pdf_url, binary=True)
            except Exception:
                continue
            if passage_found(row.get("ai_passage") or "", pdf_text(data)):
                return {"official_url": pdf_url, "route": "courtlistener-recap", "docket": docket.get("docket_id"), "document": doc.get("id")}
            time.sleep(0.5)
    return None


# ------------------------------------------------------------------ main

def from_file(decision_id: str, path: pathlib.Path, official_url: str, dry_run: bool):
    """Editor route for courts whose sites refuse the bot: the PDF was downloaded by hand from the
    court's site; we still require the quoted passage to be in it before the row is upgraded."""
    import hashlib
    hit = [(f, i, r) for f, i, r in load_rows() if r["decision_id"] == decision_id]
    if not hit:
        sys.exit(f"no row {decision_id}")
    f, i, row = hit[0]
    data = path.read_bytes()
    text = pdf_text(data) if data[:4] == b"%PDF" else data.decode("utf-8", "replace")
    if not passage_found(row["ai_passage"], text):
        log(decision_id=decision_id, result="passage-mismatch", route="hand", official_url=official_url)
        sys.exit("quoted passage NOT found in the file — row left unchanged")
    found = {"official_url": official_url, "route": "hand"}
    log(decision_id=decision_id, **found, result="upgraded", dry_run=dry_run)
    print(f"  ✓ {decision_id} ← {official_url} (hand-downloaded, passage confirmed)")
    if not dry_run:
        cur = json.loads(f.read_text().splitlines()[i])
        notes = re.sub(r"\s*Official copy not (?:published online|obtained)[^.]*\.(?:[^.]*\.)?", "", (cur.get("notes") or "").replace("official copy pending", "")).strip("; ")
        patch_row(f, i, {"decision_id": decision_id, "mirror_url": cur.get("source_url"), "source_url": official_url,
                         "verification": "fetched-and-read", "fetched_at": TODAY, "text_sha256": hashlib.sha256(data).hexdigest(),
                         "notes": (notes + f"; Official copy downloaded by hand from the court's site {TODAY} (site refuses automated access); quoted passage confirmed in the official document.").strip("; ")})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--courtlistener", action="store_true")
    ap.add_argument("--skip-govinfo", action="store_true", help="go straight to the CourtListener route (after a GovInfo pass has run)")
    ap.add_argument("--only")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--from-file", help="hand-downloaded PDF for --only; checks the passage and upgrades the row without fetching")
    ap.add_argument("--official-url", help="the court URL the file was downloaded from (required with --from-file)")
    a = ap.parse_args()
    if a.from_file:
        if not (a.only and a.official_url):
            sys.exit("--from-file needs --only <decision_id> and --official-url <url>")
        return from_file(a.only, pathlib.Path(a.from_file), a.official_url, a.dry_run)
    if not KEY:
        print("GOVINFO_API_KEY not set — GovInfo route disabled", file=sys.stderr)

    rows = load_rows()
    todo = [(f, i, r) for f, i, r in rows if r.get("verification") == "mirror-read" and (not a.only or r["decision_id"] == a.only)]
    fed = [t for t in todo if str(t[2].get("court_level", "")).startswith("federal")]
    state = [t for t in todo if not str(t[2].get("court_level", "")).startswith("federal")]
    print(f"mirror-read rows: {len(todo)} (federal {len(fed)}, state/other {len(state)})")
    if a.limit:
        fed = fed[: a.limit]

    # rows already tried on CourtListener in an earlier run are not re-queried (the budget is small)
    cl_tried = set()
    for lf in RES.glob("log*.jsonl"):
        for line in lf.read_text().splitlines():
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            if e.get("result") == "not-found" and "courtlistener" in (e.get("routes") or []):
                cl_tried.add(e["decision_id"])
    if a.courtlistener and a.skip_govinfo:
        before = len(fed)
        fed = [t for t in fed if t[2]["decision_id"] not in cl_tried]
        print(f"skipping {before - len(fed)} rows already tried on CourtListener")

    upgraded, misses, quota_stop = 0, 0, False
    for f, i, row in fed:
        found = None if a.skip_govinfo else route_govinfo(row)
        if not found and a.courtlistener and not quota_stop:
            r = route_courtlistener(row)
            if r == "quota":
                quota_stop = True
            elif r:
                found = r
        if found:
            upgraded += 1
            log(decision_id=row["decision_id"], **found, result="upgraded", dry_run=a.dry_run)
            print(f"  ✓ {row['decision_id']} ← {found['official_url']} ({found['route']})")
            if not a.dry_run:
                cur = json.loads(f.read_text().splitlines()[i])
                notes = re.sub(r"\s*Official copy not (?:published online|obtained)[^.]*\.(?:[^.]*\.)?", "", (cur.get("notes") or "").replace("official copy pending", "")).strip("; ")
                patch_row(f, i, {"decision_id": row["decision_id"], "mirror_url": cur.get("source_url"), "source_url": found["official_url"],
                                 "verification": "fetched-and-read", "fetched_at": TODAY,
                                 "notes": (notes + f"; Official copy located {TODAY} via {found['route']}; quoted passage confirmed in the official document.").strip("; ")})
        else:
            misses += 1
            log(decision_id=row["decision_id"], result="not-found", routes=["govinfo"] + (["courtlistener"] if a.courtlistener and not quota_stop else []))
    # state-court queue for the agents
    queue = [{"decision_id": r["decision_id"], "case_name": r["case_name"], "court": r["court"], "state": r.get("state"), "court_level": r["court_level"], "docket_number": r.get("docket_number"), "citation": r.get("citation"), "date_filed": r.get("date_filed"), "mirror_url": r.get("source_url"), "passage_head": (r.get("ai_passage") or "")[:160]} for _, _, r in state]
    (RES / "state-queue.json").write_text(json.dumps(queue, indent=1, ensure_ascii=False))
    print(f"federal: upgraded {upgraded}, not found {misses}{' (CourtListener daily quota reached)' if quota_stop else ''}; state/other rows queued for agents: {len(queue)} → work/resolve/state-queue.json")
    if not a.dry_run and upgraded:
        print("now: python pipeline/build_release.py --version <next> --push")


if __name__ == "__main__":
    main()
