import hashlib
import json
import pathlib
import re
from datetime import datetime, timezone

BASE = "https://www.damiencharlotin.com"
FETCHED_AT = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
LEADS = json.load(open("work/leads/t1-slice-3.json", encoding="utf-8"))
TRACKER = {}
for line in open("work/tracker-slugs.txt", encoding="utf-8"):
    if line.strip():
        parts = line.rstrip("\n").split("\t")
        TRACKER[parts[0]] = parts[1]

COURTS = {
    "10th Cir. CA": ("United States Court of Appeals for the Tenth Circuit", "ca10", "federal-appellate", None, "ca10"),
    "5th Cir. CA": ("United States Court of Appeals for the Fifth Circuit", "ca5", "federal-appellate", None, "ca5"),
    "7th Cir. CA": ("United States Court of Appeals for the Seventh Circuit", "ca7", "federal-appellate", None, "ca7"),
    "11th Cir. CA": ("United States Court of Appeals for the Eleventh Circuit", "ca11", "federal-appellate", None, "ca11"),
    "1st Cir. CA": ("United States Court of Appeals for the First Circuit", "ca1", "federal-appellate", None, "ca1"),
    "Fed. Cir.": ("United States Court of Appeals for the Federal Circuit", "cafc", "federal-appellate", None, "cafc"),
    "S.D. New York": ("United States District Court for the Southern District of New York", "nysd", "federal-district", "NY", "nysd"),
    "E.D. Texas": ("United States District Court for the Eastern District of Texas", "txed", "federal-district", "TX", "txed"),
    "N.D. Indiana (Bankruptcy)": ("United States Bankruptcy Court for the Northern District of Indiana", "innb", "federal-bankruptcy", "IN", "innb"),
    "N.D. Illinois": ("United States District Court for the Northern District of Illinois", "ilnd", "federal-district", "IL", "ilnd"),
    "M.D. Florida": ("United States District Court for the Middle District of Florida", "flmd", "federal-district", "FL", "flmd"),
    "D. Arizona": ("United States District Court for the District of Arizona", "azd", "federal-district", "AZ", "azd"),
    "E.D. Pennsylvania": ("United States District Court for the Eastern District of Pennsylvania", "paed", "federal-district", "PA", "paed"),
    "D. Colorado": ("United States District Court for the District of Colorado", "cod", "federal-district", "CO", "cod"),
    "N.D. Mississippi": ("United States District Court for the Northern District of Mississippi", "msnd", "federal-district", "MS", "msnd"),
    "W.D. Tennessee": ("United States District Court for the Western District of Tennessee", "tnwd", "federal-district", "TN", "tnwd"),
    "D. New Jersey": ("United States District Court for the District of New Jersey", "njd", "federal-district", "NJ", "njd"),
    "E.D. New York": ("United States District Court for the Eastern District of New York", "nyed", "federal-district", "NY", "nyed"),
    "W.D. Missouri": ("United States District Court for the Western District of Missouri", "mowd", "federal-district", "MO", "mowd"),
    "W.D. North Carolina": ("United States District Court for the Western District of North Carolina", "ncwd", "federal-district", "NC", "ncwd"),
    "M.D. North Carolina": ("United States District Court for the Middle District of North Carolina", "ncmd", "federal-district", "NC", "ncmd"),
    "W.D. Washington": ("United States District Court for the Western District of Washington", "wawd", "federal-district", "WA", "wawd"),
    "E.D. Michigan": ("United States District Court for the Eastern District of Michigan", "mied", "federal-district", "MI", "mied"),
    "E.D. Wisconsin": ("United States District Court for the Eastern District of Wisconsin", "wied", "federal-district", "WI", "wied"),
    "D. Massachusetts": ("United States District Court for the District of Massachusetts", "mad", "federal-district", "MA", "mad"),
    "M.D. Pennsylvania": ("United States District Court for the Middle District of Pennsylvania", "pamd", "federal-district", "PA", "pamd"),
    "W.D. Kentucky": ("United States District Court for the Western District of Kentucky", "kywd", "federal-district", "KY", "kywd"),
    "D. Delaware": ("United States District Court for the District of Delaware", "ded", "federal-district", "DE", "ded"),
    "S.D. Indiana": ("United States District Court for the Southern District of Indiana", "insd", "federal-district", "IN", "insd"),
    "D. New Mexico": ("United States District Court for the District of New Mexico", "nmd", "federal-district", "NM", "nmd"),
    "C.D. California": ("United States District Court for the Central District of California", "cacd", "federal-district", "CA", "cacd"),
    "W.D. Oklahoma": ("United States District Court for the Western District of Oklahoma", "okwd", "federal-district", "OK", "okwd"),
    "N.D. Alabama": ("United States District Court for the Northern District of Alabama", "alnd", "federal-district", "AL", "alnd"),
    "S.D. Ohio": ("United States District Court for the Southern District of Ohio", "ohsd", "federal-district", "OH", "ohsd"),
    "E.D. California": ("United States District Court for the Eastern District of California", "caed", "federal-district", "CA", "caed"),
    "W.D. Virginia": ("United States District Court for the Western District of Virginia", "vawd", "federal-district", "VA", "vawd"),
    "E.D. Louisiana": ("United States District Court for the Eastern District of Louisiana", "laed", "federal-district", "LA", "laed"),
    "D. New Jersey (Bankruptcy)": ("United States Bankruptcy Court for the District of New Jersey", "njb", "federal-bankruptcy", "NJ", "njb"),
    "D. Oregon": ("United States District Court for the District of Oregon", "ord", "federal-district", "OR", "ord"),
    "E.D. Missouri": ("United States District Court for the Eastern District of Missouri", "moed", "federal-district", "MO", "moed"),
    "W.D. Louisiana": ("United States District Court for the Western District of Louisiana", "lawd", "federal-district", "LA", "lawd"),
    "D. Minnesota": ("United States District Court for the District of Minnesota", "mnd", "federal-district", "MN", "mnd"),
    "S.D. Florida": ("United States District Court for the Southern District of Florida", "flsd", "federal-district", "FL", "flsd"),
    "N.D. California": ("United States District Court for the Northern District of California", "cand", "federal-district", "CA", "cand"),
    "SC New York": ("Supreme Court of New York", None, "state-trial", "NY", "nysupct"),
    "CA Texas": ("Court of Appeals of Texas", None, "state-appellate", "TX", "texapp"),
    "CA California (1d)": ("Court of Appeal of California, First Appellate District", None, "state-appellate", "CA", "calctapp1"),
    "CA California (5d)": ("Court of Appeal of California, Fifth Appellate District", None, "state-appellate", "CA", "calctapp5"),
    "CA Arizona (1d)": ("Arizona Court of Appeals, Division One", None, "state-appellate", "AZ", "arizctapp1"),
    "CA Arizona": ("Arizona Court of Appeals", None, "state-appellate", "AZ", "arizctapp"),
    "CA Michigan": ("Michigan Court of Appeals", None, "state-appellate", "MI", "michctapp"),
    "CA Iowa": ("Iowa Court of Appeals", None, "state-appellate", "IA", "iowactapp"),
    "CA Georgia": ("Court of Appeals of Georgia", None, "state-appellate", "GA", "gactapp"),
    "Texas": ("District Court of Travis County, Texas, 250th Judicial District", None, "state-trial", "TX", "txdistct"),
    "CA Minnesota": ("Minnesota Court of Appeals", None, "state-appellate", "MN", "minnctapp"),
    "CA Kansas": ("Kansas Court of Appeals", None, "state-appellate", "KS", "kanctapp"),
    "SC Oregon": ("Supreme Court of Oregon", None, "state-supreme", "OR", "orsupct"),
    "CA Maryland": ("Appellate Court of Maryland", None, "state-appellate", "MD", "mdctapp"),
    "CA Missouri": ("Missouri Court of Appeals", None, "state-appellate", "MO", "moctapp"),
    "SC Pennsylvania": ("Supreme Court of Pennsylvania", None, "state-supreme", "PA", "pasupct"),
    "CA Illinois (1d)": ("Appellate Court of Illinois, First District", None, "state-appellate", "IL", "illappct1"),
    "CA New York": ("Supreme Court of New York, Appellate Division, Second Department", None, "state-appellate", "NY", "nyappdiv2"),
    "CA Florida (4d)": ("District Court of Appeal of Florida, Fourth District", None, "state-appellate", "FL", "fladistctapp4"),
    "CA Florida (6d)": ("District Court of Appeal of Florida, Sixth District", None, "state-appellate", "FL", "fladistctapp6"),
    "CA Florida (2d)": ("District Court of Appeal of Florida, Second District", None, "state-appellate", "FL", "fladistctapp2"),
    "SC Delaware": ("Supreme Court of Delaware", None, "state-supreme", "DE", "delsupct"),
    "SC Oklahoma": ("Supreme Court of Oklahoma", None, "state-supreme", "OK", "oksupct"),
    "CA Ohio (6d)": ("Court of Appeals of Ohio, Sixth District", None, "state-appellate", "OH", "ohioctapp6"),
    "CA Ohio (8d)": ("Court of Appeals of Ohio, Eighth District", None, "state-appellate", "OH", "ohioctapp8"),
    "CA Indiana": ("Indiana Court of Appeals", None, "state-appellate", "IN", "indctapp"),
    "CA Kentucky": ("Kentucky Court of Appeals", None, "state-appellate", "KY", "kyctapp"),
    "DC Oklahoma": ("District Court of Tulsa County, Oklahoma", None, "state-trial", "OK", "okdistct"),
    "CA Tennessee": ("Court of Appeals of Tennessee", None, "state-appellate", "TN", "tennctapp"),
    "App. NY (2d)": ("Supreme Court of New York, Appellate Division, Second Department", None, "state-appellate", "NY", "nyappdiv2"),
    "SC Massachussetts": ("Supreme Judicial Court of Massachusetts", None, "state-supreme", "MA", "masssupjudct"),
    "App. Div. 1st Dept (NY)": ("Supreme Court of New York, Appellate Division, First Department", None, "state-appellate", "NY", "nyappdiv1"),
}

OUTCOME_MAP = [
    (re.compile(r"adverse costs|costs order|attorney'?s fees|fees", re.I), "costs-order"),
    (re.compile(r"bar referral|referral|disciplin", re.I), "referral"),
    (re.compile(r"show cause|order to show cause|pending", re.I), "pending"),
    (re.compile(r"dismiss", re.I), "dismissal"),
    (re.compile(r"admonish|warning|warn", re.I), "warning"),
    (re.compile(r"monetary|sanction|public reprimand|censure|CLE|citation review", re.I), "sanctions"),
    (re.compile(r"no sanction", re.I), "other"),
]

def slugify(s, max_len=46):
    s = s.lower().replace("’", "").replace("'", "")
    s = re.sub(r"\bet al\.?\b", "", s)
    s = re.sub(r"\b\d+\b", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    parts = [p for p in s.split("-") if p not in {"inc", "llc", "corp", "corporation", "company", "co", "the", "et", "al", "usa"}]
    s = "-".join(parts) or "decision"
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s

def clean_case_name(s):
    s = re.sub(r"\s+\(2\)$", "", s).strip()
    return s

def clean_text(s):
    s = s.replace("\x0c", "\n")
    lines = []
    skip_editor = False
    for line in s.splitlines():
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if "WESTLAW" in stripped or "Thomson Reuters" in stripped or "No claim to original U.S. Government Works" in stripped:
            continue
        if stripped.startswith("Editor's Note:"):
            skip_editor = True
            continue
        if skip_editor:
            if re.match(r"^(Attorneys and Law Firms|ORDER|OPINION|MEMORANDUM|Before|PER CURIAM|BACKGROUND|[A-Z][A-Z ]+ JUDGE)", stripped):
                skip_editor = False
            else:
                continue
        if re.match(r"^(?:Page )?\d+$", stripped):
            continue
        if re.search(r"^(Case|Appellate Case:).+Page(?:ID)?", stripped):
            # Header/footer; keep substantive lines that sometimes occur on same OCR line impossible to separate elsewhere.
            continue
        lines.append(stripped)
    s = "\n".join(lines)
    s = re.sub(r"(?<=\w)-\s+\n\s*(?=\w)", "", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    # Raw extraction often breaks every line; convert single line breaks to spaces.
    s = re.sub(r"(?<![.!?:;\)])\n(?=\S)", " ", s)
    s = re.sub(r"\n(?=[a-z0-9\(\[\"“])", " ", s)
    return s.strip()

STRONG_CONDUCT_PAT = re.compile(
    r"hallucinat\w*|fabricat\w*|fictitious|non[- ]existent|nonexistent|does not exist|do not exist|no such case exists|not a real case|fake|phantom|bogus|imaginary legal authorit\w*|false quot\w*|misquot\w*|errant citations|citation errors|invalid cites|made up|completely made up|do not appear(?:[^.]{0,80})?(?:quote|case|record|transcript|authority)",
    re.I,
)
CONDUCT_PAT = re.compile(
    r"hallucinat\w*|fabricat\w*|fictitious|non[- ]existent|nonexistent|does not exist|do not exist|no such case exists|not a real case|fake|phantom|bogus|imaginary legal authorit\w*|false quot\w*|misquot\w*|misrepresent\w*|unsupported proposition|do not support|does not support|do not contain|does not contain|do not appear|does not appear|erroneous legal authority|citation errors|errant citations|false citation|incorrect citation|inaccurate citation|unverified citation|invalid cites|made up|completely made up",
    re.I,
)
AI_PAT = re.compile(r"ChatGPT|Claude|Gemini|Copilot|generative artificial intelligence|artificial intelligence|GenAI|GAI|AI tool|A\.I\.", re.I)
OUTCOME_PAT = re.compile(r"sanction\w*|show cause|warn\w*|admonish\w*|strike\w*|stricken|dismiss\w*|referr\w*|reprimand\w*|censure\w*|costs|fees|barred|disciplin\w*|contempt", re.I)

def word_window(text, pos, before=90, after=170):
    spans = list(re.finditer(r"\S+", text))
    if not spans:
        return ""
    wi = 0
    for i, m in enumerate(spans):
        if m.start() <= pos < m.end():
            wi = i
            break
        if m.start() > pos:
            wi = max(0, i - 1)
            break
    a = max(0, wi - before)
    b = min(len(spans), wi + after)
    frag = text[spans[a].start():spans[b - 1].end()]
    # Try not to start in a broken citation/header if a sentence boundary is nearby.
    rel = spans[wi].start() - spans[a].start()
    starts = [m.end() for m in re.finditer(r"(?<=[.!?])\s+", frag[:rel])]
    if starts and starts[-1] < rel and rel - starts[-1] < 700:
        frag = frag[starts[-1]:]
    if not re.search(r"[.!?]['\")\]]?$", frag):
        end = max(frag.rfind(". "), frag.rfind("? "), frag.rfind("! "))
        if end > 300:
            frag = frag[: end + 1]
        else:
            frag = frag + " ..."
    return re.sub(r"\s+", " ", frag).strip()

def raw_word_window(text, pos, before=100, after=180):
    spans = list(re.finditer(r"\S+", text))
    if not spans:
        return ""
    wi = 0
    for i, m in enumerate(spans):
        if m.start() <= pos < m.end():
            wi = i
            break
        if m.start() > pos:
            wi = max(0, i - 1)
            break
    a = max(0, wi - before)
    b = min(len(spans), wi + after)
    frag = text[spans[a].start():spans[b - 1].end()]
    return re.sub(r"\s+", " ", frag).strip()

def pick_passage(raw_text, lead):
    text = clean_text(raw_text)
    # Prefer the main document in bundled Kebe PDF, not the later agreed order.
    if "ORDER (I) GRANTING IN PART" in text and "STIPULATION AND AGREED ORDER" in text:
        text = text[text.find("ORDER (I) GRANTING IN PART"):]
    matches = []
    for pat, base in [(STRONG_CONDUCT_PAT, 14), (CONDUCT_PAT, 10), (AI_PAT, 6), (OUTCOME_PAT, 4)]:
        for m in pat.finditer(text):
            pos = m.start()
            local = text[max(0, pos - 900): min(len(text), pos + 1600)]
            score = base
            score += 8 * len(CONDUCT_PAT.findall(local))
            score += 4 * len(AI_PAT.findall(local))
            score += 5 * len(OUTCOME_PAT.findall(local))
            # Avoid table of authorities/copyright headings.
            if pos < 250:
                score -= 4
            matches.append((score, pos))
    if not matches:
        return None
    matches.sort(reverse=True)
    strong_positions = [m.start() for m in STRONG_CONDUCT_PAT.finditer(text) if m.start() > 250]
    conduct_positions = [m.start() for m in CONDUCT_PAT.finditer(text) if m.start() > 250]
    outcome_positions = [m.start() for m in OUTCOME_PAT.finditer(text)]
    best_pos = matches[0][1]
    # Prefer the first concrete description of the defective filing over later sanctions-law discussion.
    if strong_positions:
        conduct_pos = strong_positions[0]
    elif conduct_positions:
        conduct_pos = conduct_positions[0]
    else:
        conduct_pos = best_pos
    if outcome_positions:
        # Pick an outcome after conduct if available, otherwise nearest meaningful one.
        after = [p for p in outcome_positions if p >= conduct_pos]
        outcome_pos = min(after, key=lambda p: p - conduct_pos) if after else min(outcome_positions, key=lambda p: abs(p - conduct_pos))
    else:
        outcome_pos = conduct_pos
    frag1 = word_window(text, conduct_pos, 75, 165)
    frag2 = ""
    if abs(outcome_pos - conduct_pos) > 1400:
        frag2 = word_window(text, outcome_pos, 45, 100)
    passage = frag1 if not frag2 else frag1 + " ... " + frag2
    words = passage.split()
    if len(words) > 390:
        passage = " ".join(words[:390]) + " ..."
    if len(words) < 55:
        passage = raw_word_window(text, conduct_pos, 95, 190)
    return passage.strip()

def document_type(raw_text):
    head = clean_text(raw_text)[:2500].upper()
    if "REPORT AND RECOMMENDATION" in head:
        return "report-and-recommendation"
    if "MEMORANDUM OPINION" in head:
        return "memorandum-opinion"
    if "OPINION & ORDER" in head or "OPINION AND ORDER" in head:
        return "opinion"
    if "ORDER AND JUDGMENT" in head or "ORDER" in head:
        return "order"
    if "OPINION" in head:
        return "opinion"
    return "order"

def extract_citation(raw_text):
    # Treat only caption/header citations as the decision citation; otherwise body
    # citations to authorities can be mistaken for the row's citation.
    text = clean_text("\n".join(raw_text.splitlines()[:35]))
    patterns = [
        r"\b20\d{2}\s+WL\s+\d+\b",
        r"\b20\d{2}\s+N\.?Y\.?\s+Slip\s+Op\.?\s+\d+\s*\(?[A-Z]?\)?",
        r"\b20\d{2}\s+OK\s+\d+\b",
        r"\b20\d{2}\s+Ohio\s+\d+\b",
        r"\b20\d{2}-Ohio-\d+\b",
        r"\b\d+\s+F\.\s?Supp\.\s?\d*d?\s+\d+\b",
        r"\b---\s+F\.Supp\.3d\s+----\s+\(20\d{2}\)",
        r"\b---\s+N\.Y\.S\.3d\s+----\s+\(20\d{2}\)",
        r"\b20\d{2}\s+IL\s+App\s+\([^)]*\)\s+\d+(?:-U)?\b",
        r"\b20\d{2}\s+Del\.\s+LEXIS\s+\d+\b",
        r"\b20\d{2}\s+Mass\.\s+LEXIS\s+\d+\b",
    ]
    found = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            val = re.sub(r"\s+", " ", m.group(0)).strip()
            if val not in found:
                found.append(val)
    return "; ".join(found[:2]) if found else None

def citation_for(raw_text, date_filed):
    citation = extract_citation(raw_text)
    if not citation:
        return None
    year = date_filed[:4]
    parts = [p.strip() for p in citation.split(";") if year in p]
    return "; ".join(parts) if parts else None

def extract_docket(raw_text, lead):
    def polish(val):
        if not val:
            return None
        val = re.sub(r"\s+", " ", val.replace("–", "-")).strip(" .,:;|")
        patterns = [
            r"\b\d{1,2}:\d{2}-(?:cv|cr|bk|ap|mc)-[0-9A-Za-z-]+",
            r"\b\d{1,2}:\d{2}-CV-\d{3,6}-[A-Z]+(?:-[A-Z]+)*\b",
            r"\bCV-\d{2}-\d{5}-[A-Z]{2,5}-[A-Z]{2,5}\b",
            r"\bCIV-\d{2}-\d{3,5}-[A-Z]+\b",
            r"\b\d{4,6}[- ](?:CV|C|CA|DR|CJ|EDA|CAAP|COA|A|XP|FD|SC|PR|GN)[- ][0-9A-Z-]{2,}(?: [A-Z]{1,4})?",
            r"\b[1-9]\s+CA-[A-Z]{2}\s+\d{2}-\d{4,5}(?:\s+[A-Z]{1,3})?",
            r"\b[1-9]D20\d{2}-\d{4}\b",
            r"\bD-\d-[A-Z]{2}-\d{2}-\d{6}\b",
            r"\bFD-\d{4}-\d+\b",
            r"\bC-\d{2}-CV-\d{2}-\d{6}\b",
            r"\bN\d{2}C-\d{2}-\d{3}(?:\s+[A-Z]{2,4})?\b",
            r"\b\d{2,4}\s+C\s+\d{3,6}\b",
            r"\b\d{2,4}\s+Civ\.\s+\d{3,6}\b",
            r"\b\d{2}-\d{4,5}\b",
        ]
        for pat in patterns:
            m = re.search(pat, val, re.I)
            if m:
                return re.sub(r"\s+", " ", m.group(0)).strip()
        bad = re.compile(r"Plaintiff|Defendant|Petitioner|Respondent|Judge|Court|Appeal from|Motion|sanction|Citationize|Index|Classification|initiated|terminate|remanded|granted|denied|s and|v$", re.I)
        if bad.search(val):
            return None
        if len(val) <= 38 and re.search(r"\d", val):
            return val
        return None

    raw_head = "\n".join(raw_text.splitlines()[:90])
    for line in raw_head.splitlines():
        if re.search(r"(Case|Civil Action|Cause|Docket|No\.|Number|Index)", line, re.I):
            got = polish(line)
            if got:
                return got
    text = clean_text(raw_text)[:3500]
    pats = [
        r"(?:Case|Civil Action|CAUSE|Docket|No\.|NUMBER|Index)\s*(?:No\.|Number|NUMBER|NO\.|#|:)?\s*[:#]?\s*([A-Z0-9][A-Z0-9:\-–/. ]{2,45})",
        r"\bNo\.\s*([A-Z0-9][A-Z0-9:\-–/. ]{2,45})",
    ]
    for pat in pats:
        m = re.search(pat, text, re.I)
        if m:
            val = m.group(1)
            val = re.split(r"\s{2,}|\|| Filed |\n| MEMORANDUM| ORDER| OPINION", val)[0]
            val = val.strip(" .,:;|-")
            val = val.replace("–", "-")
            val = polish(val)
            if val and not re.match(r"20\d{2}$", val):
                return val
    # Fall back to No. in lead case name.
    m = re.search(r"No\.\s*([^()]+)", lead.get("Case Name", ""), re.I)
    if m:
        return polish(m.group(1).strip())
    return None

def ai_tool(raw_text, lead):
    tool = (lead.get("AI Tool") or "").strip()
    if tool and tool.lower() not in {"implied", "unidentified", "unknown", ""}:
        return tool
    text = raw_text[:20000]
    for name in ["ChatGPT", "Claude", "Gemini", "Copilot", "LexisNexis brief analysis", "GenAI", "GAI"]:
        if re.search(re.escape(name), text, re.I):
            return name
    if re.search(r"generative artificial intelligence", text, re.I):
        return "generative artificial intelligence"
    if re.search(r"artificial intelligence", text, re.I):
        return "artificial intelligence"
    return None

def actor_from(lead):
    p = (lead.get("Party(ies)") or "").lower()
    if "pro se" in p or "self" in p:
        return "litigant-in-person"
    if "prosecutor" in p:
        return "prosecutor"
    if "judge" in p:
        return "judge"
    if "expert" in p:
        return "expert"
    if "firm" in p:
        return "firm"
    if "lawyer" in p or "counsel" in p or "attorney" in p:
        return "lawyer"
    return "other"

def outcome_from(lead):
    out = lead.get("Outcome") or ""
    # No sanction must beat generic sanction.
    if re.search(r"no sanction", out, re.I):
        return "other"
    for pat, value in OUTCOME_MAP:
        if pat.search(out):
            return value
    if lead.get("Professional Sanction", "").lower() == "yes":
        return "referral"
    if (lead.get("Monetary Penalty") or "").strip():
        return "sanctions"
    return "other"

def penalty_from(lead):
    s = lead.get("Monetary Penalty") or ""
    m = re.search(r"([0-9][0-9,]*(?:\.\d+)?)\s*([A-Z]{3})?", s)
    if not m:
        return None, None
    amount = float(m.group(1).replace(",", ""))
    if amount.is_integer():
        amount = int(amount)
    return amount, (m.group(2) or "USD")

def conduct_from(lead):
    h = lead.get("Hallucination Items") or lead.get("Details") or ""
    if h:
        h = re.sub(r"\s*\|\|\s*", "; ", h)
        h = re.sub(r"\s*\|\s*", ": ", h)
        h = re.sub(r"\s+", " ", h).strip()
        if len(h) > 296:
            h = h[:296].rsplit(" ", 1)[0] + "…"
        return h
    return "The filing contained authorities or citation statements that the court found unsupported, erroneous, or subject to AI-use inquiry."

def outcome_phrase(lead):
    outcome = (lead.get("Outcome") or "").strip()
    low = outcome.lower()
    phrases = []
    if "no sanction" in low:
        phrases.append("declined to impose sanctions")
    if "admonish" in low:
        phrases.append("admonished the filer")
    if "warning" in low or re.search(r"\bwarn", low):
        phrases.append("warned the filer")
    if "order to amend" in low or "amend brief" in low:
        phrases.append("ordered correction of the brief")
    if "show cause" in low:
        phrases.append("ordered the filer to show cause")
    if "adverse costs" in low or "costs" in low or "attorney" in low and "fees" in low:
        phrases.append("awarded costs or fees")
    if "monetary" in low or "fine" in low:
        phrases.append("imposed a monetary sanction")
    if "bar referral" in low or "referral" in low:
        phrases.append("referred the matter for professional discipline")
    if "public reprimand" in low:
        phrases.append("issued a public reprimand")
    if "censure" in low:
        phrases.append("issued a public censure")
    if "citation review" in low or "cle" in low:
        phrases.append("ordered remedial review or training")
    if "dismiss" in low:
        phrases.append("dismissed the filing, appeal, or claims")
    if not phrases:
        phrases.append("addressed the defective filing")
    # Deduplicate while preserving order.
    seen = set()
    phrases = [p for p in phrases if not (p in seen or seen.add(p))]
    if len(phrases) == 1:
        return phrases[0]
    return ", ".join(phrases[:-1]) + ", and " + phrases[-1]

def disposition_from(lead, court_short):
    actor = actor_from(lead)
    return f"The court {outcome_phrase(lead)} after identifying fabricated, erroneous, or unsupported authority in a filing by a {actor}."[:239]

def summary_from(lead, court_name):
    actor = actor_from(lead).replace("litigant-in-person", "self-represented litigant")
    outcome = (lead.get("Outcome") or "addresses the filing issue").strip().rstrip(".")
    conduct = conduct_from(lead).split(";")[0]
    # Strip category labels for readability.
    conduct = re.sub(r"^(Fabricated|False Quotes|Misrepresented): [^:]+: ", "", conduct)
    if len(conduct) > 155:
        conduct = conduct[:155].rsplit(" ", 1)[0].rstrip(" ,;:.…") + "…"
    else:
        conduct = conduct.rstrip(" ,;:.…")
    case = clean_case_name(lead["Case Name"]).rstrip(".")
    txt = (f"{court_name} on {lead['Date']} addresses {case}. "
           f"The court {outcome_phrase(lead)} after a {actor} filing raised AI-related or fabricated-citation concerns, including {conduct}.")
    words = txt.split()
    if len(words) > 60:
        txt = " ".join(words[:60]).rstrip(" ,;:") + "."
    elif len(words) < 40:
        txt += " The decision documents the court’s response to the defective legal authorities in the proceeding."
    return txt

def authorities_from(passage):
    auth = []
    # Capture case names with reporter/citation tail when in the passage.
    for m in re.finditer(r"\b([A-Z][A-Za-z0-9'’&.\- ]{1,55}\s+v\.\s+[A-Z][A-Za-z0-9'’&.\- ]{1,65}(?:,\s*(?:No\.|\d|__|---)[^.;()]{0,90}(?:\([^)]*\))?)?)", passage):
        val = re.sub(r"\s+", " ", m.group(1)).strip(" ,;.")
        if len(val) > 8 and val not in auth:
            auth.append(val)
    for m in re.finditer(r"\b(?:Fed\. R\. Civ\. P\.|Federal Rule of Civil Procedure|Bankruptcy Rule|Rule|22 NYCRR|N\.D\.R\.App\.P\.|MCR|A\.R\.S\.)\s*[0-9][A-Za-z0-9.()\-–]*(?:\([a-z0-9]+\))*", passage):
        val = re.sub(r"\s+", " ", m.group(0)).strip(" ,;.")
        if val not in auth:
            auth.append(val)
    return auth[:10]

SPECIAL_TRACKER = {
    60: "oba-v-reeves",
    108: "gleason-v-marcus",
}
DOCKET_OVERRIDES = {
    3: "05-24-01449-CV",
    11: "A26A0698; A26A0699; A26A0700",
    17: "25-cv-03285-NYW-MDB",
    21: "A25-0906",
    24: "129,066",
    25: "S072692",
    26: "A26A0506",
    35: "ED113978",
    60: None,
    63: "25A-XP-2508",
    65: "23 Civ. 5016 (NSR)(JCM)",
    71: "FD-2021-987",
    84: "2237 September Term, 2025",
    89: "2025-02380",
    94: "2384CV01461-BLS2",
    97: "1:25-cv-10258 (SDA)",
    99: "1:26cv77",
    101: "2026-01135; 2026-00170",
    104: "23-14082-SMG",
    110: "900514-25",
}
SKIP = {
    8: "The document addresses ordinary unsupported authorities and contains no substantive AI or fabricated-citation discussion.",
    23: "The extractable document text only asks whether the pro se plaintiff used GAI and does not substantively discuss fabricated citations.",
    46: "CourtListener exact-name search returned zero results for the Reason lead; no primary document obtained.",
    93: "CourtListener search for the Reason lead was throttled; no primary document obtained.",
}

rows = []
skips = []
ids = set()
for idx, lead in enumerate(LEADS, 1):
    if idx in SKIP:
        skips.append({"index": idx, "case_name": lead["Case Name"], "reason": SKIP[idx]})
        continue
    source = lead.get("Source") or ""
    if not source.startswith("/documents/"):
        skips.append({"index": idx, "case_name": lead["Case Name"], "reason": "No Charlotin mirror path and CourtListener did not yield a usable document."})
        continue
    pdfs = list(pathlib.Path("work/agents/t1-s3-sources").glob(f"{idx:03d}-*.pdf"))
    txtp = pathlib.Path(f"work/agents/t1-s3-text-raw/{idx:03d}.txt")
    if len(pdfs) != 1 or not txtp.exists():
        skips.append({"index": idx, "case_name": lead["Case Name"], "reason": "Fetched PDF or extracted text missing."})
        continue
    raw = txtp.read_text(encoding="utf-8", errors="ignore")
    passage = pick_passage(raw, lead)
    if not passage or len(passage) < 40:
        skips.append({"index": idx, "case_name": lead["Case Name"], "reason": "No substantive extractable passage about the AI/fabricated-citation issue."})
        continue
    court_name, court_code, level, state, prefix = COURTS.get(lead["Court"], (lead["Court"], None, "other", None, slugify(lead["Court"], 18)))
    # Override bankruptcy from text when the lead court label is the district.
    if "UNITED STATES BANKRUPTCY COURT" in raw[:3000] and lead["Court"] == "S.D. Florida":
        court_name, court_code, level, state, prefix = "United States Bankruptcy Court for the Southern District of Florida", "flsb", "federal-bankruptcy", "FL", "flsb"
    amount, currency = penalty_from(lead)
    tool = ai_tool(raw, lead)
    cid = f"{prefix}-2026-{slugify(clean_case_name(lead['Case Name']))}"
    n = 2
    base_cid = cid
    while cid in ids:
        cid = f"{base_cid}-{n}"
        n += 1
    ids.add(cid)
    note = "Read from the Charlotin CC0 public mirror of the court-authored document; official copy is pending."
    if idx == 104:
        note += " The bundled PDF also contains a June 30, 2026 agreed order establishing the later fee and Rule 9011 sanction amounts; this row covers the May 13, 2026 sanctions order."
    row = {
        "decision_id": cid,
        "case_name": clean_case_name(lead["Case Name"]),
        "court": court_name,
        "court_code": court_code,
        "court_level": level,
        "state": state,
        "date_filed": lead["Date"],
        "citation": citation_for(raw, lead["Date"]),
        "docket_number": DOCKET_OVERRIDES[idx] if idx in DOCKET_OVERRIDES else extract_docket(raw, lead),
        "document_type": document_type(raw),
        "topics": ["fabricated-citations"],
        "primary_topic": "fabricated-citations",
        "court_used_ai": False,
        "ai_tool_named": tool,
        "disposition": disposition_from(lead, court_name),
        "ai_passage": passage,
        "cited_authorities": authorities_from(passage),
        "summary": summary_from(lead, court_name),
        "incident": {
            "conduct": conduct_from(lead),
            "outcome": outcome_from(lead),
            "actor": actor_from(lead),
            "monetary_penalty": amount,
            "currency": currency,
            "ai_tool": tool,
        },
        "tracker_slug": SPECIAL_TRACKER.get(idx),
        "courtlistener_url": None,
        "text_sha256": hashlib.sha256(pdfs[0].read_bytes()).hexdigest(),
        "source_url": BASE + source,
        "archive_url": None,
        "fetched_at": FETCHED_AT,
        "verification": "mirror-read",
        "lead_source": ["charlotin-cc0"],
        "notes": note,
    }
    # Clean optional empty strings.
    for k in ["citation", "docket_number"]:
        if row[k] == "":
            row[k] = None
    rows.append(row)

outp = pathlib.Path("work/agents/decisions-t1-s3.jsonl")
outp.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
pathlib.Path("work/agents/t1-s3-meta/skips.json").write_text(json.dumps(skips, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"wrote {len(rows)} rows, {len(skips)} skips, fetched_at {FETCHED_AT}")
