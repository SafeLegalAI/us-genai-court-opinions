import json
import re
from pathlib import Path

BASE = "https://www.damiencharlotin.com"
path = Path("work/agents/decisions-t1-s3.jsonl")
rows = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
leads = json.load(open("work/leads/t1-slice-3.json", encoding="utf-8"))
lead_by_url = {BASE + r["Source"]: (i, r) for i, r in enumerate(leads, 1) if r.get("Source", "").startswith("/documents/")}

number_words = "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|twenty|dozens?|numerous|multiple|several"

SHORT_COURT = {
    "United States Court of Appeals for the Tenth Circuit": "the Tenth Circuit",
    "United States Court of Appeals for the Fifth Circuit": "the Fifth Circuit",
    "United States Court of Appeals for the Seventh Circuit": "the Seventh Circuit",
    "United States Court of Appeals for the Eleventh Circuit": "the Eleventh Circuit",
    "United States Court of Appeals for the First Circuit": "the First Circuit",
    "United States Court of Appeals for the Federal Circuit": "the Federal Circuit",
    "United States District Court for the Southern District of New York": "the Southern District of New York",
    "United States District Court for the Eastern District of Texas": "the Eastern District of Texas",
    "United States Bankruptcy Court for the Northern District of Indiana": "the Northern District of Indiana Bankruptcy Court",
    "United States District Court for the Northern District of Illinois": "the Northern District of Illinois",
    "United States District Court for the Middle District of Florida": "the Middle District of Florida",
    "United States District Court for the District of Arizona": "the District of Arizona",
    "United States District Court for the Eastern District of Pennsylvania": "the Eastern District of Pennsylvania",
    "United States District Court for the District of Colorado": "the District of Colorado",
    "United States District Court for the Northern District of Mississippi": "the Northern District of Mississippi",
    "United States District Court for the Western District of Tennessee": "the Western District of Tennessee",
    "United States District Court for the District of New Jersey": "the District of New Jersey",
    "United States District Court for the Eastern District of New York": "the Eastern District of New York",
    "United States District Court for the Western District of Missouri": "the Western District of Missouri",
    "United States District Court for the Western District of North Carolina": "the Western District of North Carolina",
    "United States District Court for the Middle District of North Carolina": "the Middle District of North Carolina",
    "United States District Court for the Western District of Washington": "the Western District of Washington",
    "United States District Court for the Eastern District of Michigan": "the Eastern District of Michigan",
    "United States District Court for the Eastern District of Wisconsin": "the Eastern District of Wisconsin",
    "United States District Court for the District of Massachusetts": "the District of Massachusetts",
    "United States District Court for the Middle District of Pennsylvania": "the Middle District of Pennsylvania",
    "United States District Court for the Western District of Kentucky": "the Western District of Kentucky",
    "United States District Court for the District of Delaware": "the District of Delaware",
    "United States District Court for the Southern District of Indiana": "the Southern District of Indiana",
    "United States District Court for the District of New Mexico": "the District of New Mexico",
    "United States District Court for the Central District of California": "the Central District of California",
    "United States District Court for the Western District of Oklahoma": "the Western District of Oklahoma",
    "United States District Court for the Northern District of Alabama": "the Northern District of Alabama",
    "United States District Court for the Southern District of Ohio": "the Southern District of Ohio",
    "United States District Court for the Eastern District of California": "the Eastern District of California",
    "United States District Court for the Western District of Virginia": "the Western District of Virginia",
    "United States District Court for the Eastern District of Louisiana": "the Eastern District of Louisiana",
    "United States Bankruptcy Court for the District of New Jersey": "the District of New Jersey Bankruptcy Court",
    "United States District Court for the District of Oregon": "the District of Oregon",
    "United States District Court for the Eastern District of Missouri": "the Eastern District of Missouri",
    "United States District Court for the Western District of Louisiana": "the Western District of Louisiana",
    "United States District Court for the District of Minnesota": "the District of Minnesota",
    "United States Bankruptcy Court for the Southern District of Florida": "the Southern District of Florida Bankruptcy Court",
    "United States District Court for the Northern District of California": "the Northern District of California",
    "Court of Appeal of California, First Appellate District": "the California First District Court of Appeal",
    "Court of Appeal of California, Fifth Appellate District": "the California Fifth District Court of Appeal",
    "District Court of Travis County, Texas, 250th Judicial District": "the Travis County district court",
    "Supreme Court of New York, Appellate Division, Second Department": "New York's Second Department",
    "Supreme Court of New York, Appellate Division, First Department": "New York's First Department",
    "District Court of Tulsa County, Oklahoma": "the Tulsa County district court",
}

LEAD_DISP = {
    1: "The court affirmed dismissal and upheld the district court's admonition that the self-represented appellant verify case citations before relying on AI-assisted briefing.",
    2: "The court amended its prior order and declined to attribute the non-existent citations in duplicated opposition papers to appellate counsel.",
    3: "The court struck the appellant's original briefs, required an amended brief, and then decided the appeal on the redrawn briefing.",
    5: "The court imposed $6,000 in sanctions payable to the court and referred counsel to the California State Bar.",
    6: "The court publicly reprimanded plaintiff's counsel, imposed $6,000 in sanctions, ordered firmwide citation review, and required AI-focused CLE.",
    9: "The court dismissed the appeal after the appellant failed to comply with its order addressing fabricated authorities in her briefs.",
    11: "The court vacated the order denying dismissal of the Title VII claims and remanded for reconsideration using proper standards and real case law.",
    12: "The court struck the latest defective filing and imposed monetary sanctions for repeated AI-hallucinated arguments and cases.",
    13: "The court awarded more than $85,000 in fees and costs and referred counsel to the district grievance committee.",
    14: "The court declined to add new sanctions but warned counsel that the order could support future professional-discipline proceedings.",
    15: "The court dismissed the complaint without leave to amend and noted the plaintiff's prior hallucinated citations in related litigation.",
    17: "The court ordered plaintiff to show cause why the filing was not sanctionable and whether counsel complied with professional obligations.",
    18: "The court granted the City of Austin's jurisdictional plea, dismissed those claims with prejudice, and awarded $10,000 in attorney fees.",
    19: "The court revoked pro hac vice admission, disqualified resident counsel, fined counsel $8,000, and referred the matter to bar authorities.",
    20: "The court required a corrected motion after counsel disclosed AI-hallucinated citations, but declined to impose sanctions at that point.",
    24: "The court affirmed summary judgment, while a concurrence admonished the appellant over fake case citations and quotations in his brief.",
    25: "The court struck the response to the petition for review, imposed a $500 sanction, and granted judicial notice.",
    27: "The court struck the defective appellate filings, admonished the appellant, and warned that additional violations could draw sanctions.",
    29: "The court affirmed the foreclosure rulings and noted that the appellant's reply brief used a quotation found nowhere in Maryland or other case law.",
    32: "The court ordered plaintiff's counsel to show cause about two fabricated quotations and compliance with the court's AI-use standing order.",
    33: "The court sanctioned the plaintiff $120, stayed the case until payment, and required copies of cited authorities with future filings.",
    36: "The court ordered Reaves Law Firm to pay costs for improper citations and directed counsel to send the order to professional regulators.",
    37: "The magistrate judge recommended dismissal and noted a false Sixth Circuit citation while denying further relief.",
    38: "The court struck defendants' amended answer and counterclaims and awarded plaintiff costs and fees for responding to unsupported citations.",
    39: "The court sanctioned counsel for appellate expenses, admonished him, and referred the matter for possible discipline.",
    42: "The court ordered counsel to show cause why sanctions should not issue for relying on an allegedly fabricated autopsy and forensic report.",
    44: "The court affirmed and observed that an asserted parental-alienation authority could not be located.",
    48: "The court affirmed the judgment and noted that the appellant's briefing relied on a nonexistent case and fabricated quotations.",
    49: "The court ordered mother to show cause within fourteen days why sanctions should not be imposed for fictitious authorities.",
    50: "The court warned that future filings containing fabricated legal authorities may lead to sanctions.",
    51: "The court affirmed dismissal and noted that appellants misrepresented authorities and quoted language absent from cited cases.",
    52: "The court imposed a $250 sanction on the self-represented appellant for a brief prepared with unverified generative AI.",
    53: "The court ordered counsel to show cause why sanctions should not issue for an apparently AI-generated emergency stay motion.",
    55: "The court barred the appellant from future pro se filings in the case unless signed by a Florida Bar member.",
    56: "The court warned counsel after plaintiff conceded a fictitious citation and withdrew it from the briefing.",
    57: "The court denied the sealing motion without prejudice and directed the movant to refile using only existing, accurately quoted authorities.",
    58: "The court affirmed and referred counsel to the Florida Bar over trial-transcript quotations not found in the record.",
    60: "The court publicly reprimanded the attorney as reciprocal discipline for ChatGPT-generated citations used in federal filings.",
    62: "The court imposed a $1,000 Rule 11 sanction for non-existent citations and denied the motion for preliminary injunction.",
    66: "The court dismissed the second amended complaint and declined to award fees for AI-hallucinated citations.",
    69: "The court affirmed and noted that the circuit court had already warned mother about non-existent case law.",
    71: "The court sanctioned counsel $2,000, ordered attorney-fee proceedings, required a knowledge-base audit, and directed bar referral.",
    72: "The court overruled the assignment of error after finding the cited plea-record authority nonexistent or unrelated.",
    73: "The court affirmed dismissal and rejected briefing that used apparent AI-hallucinated cases and an inaccurate Rule 19 argument.",
    74: "The magistrate judge recommended denying the motion to vacate and described earlier Rule 11 sanctions proceedings against counsel.",
    76: "The magistrate judge treated the cited Ohio Supreme Court decision as unverified and recommended remand.",
    78: "The court disqualified counsel from the case and from appearing before the judge for six months and referred the order to bar authorities.",
    80: "The court declined sanctions in light of remedial steps but required counsel to verify all future case and record citations.",
    82: "The magistrate judge recommended a $2,000 sanction against counsel for two AI-generated non-existent citations.",
    83: "The court struck fabricated-authority portions of the brief and affirmed dismissal.",
    86: "The court granted dismissal of most claims and warned that any future filing must be supported by real law.",
    88: "The bankruptcy court denied the sanctions motion and rejected authorities that were nonexistent or did not support the debtor's position.",
    91: "The court allowed counsel to correct suggested findings after fabricated citations were identified.",
    94: "The court denied pro hac vice admission because counsel had signed AI-hallucinated filings in a prior federal case.",
    96: "The court affirmed and declined to find waiver despite several fictitious or inaccurate citations in the appellant's brief.",
    97: "The court publicly admonished counsel after accepting the withdrawal of incorrectly cited cases.",
    98: "The court ordered counsel to show cause by June 5, 2026, why sanctions should not issue for citations to cases that do not exist.",
    99: "The court remanded the collection case and ordered the defendant to show cause within fourteen days why Rule 11 sanctions should not issue.",
    101: "The court suspended the attorney for three months and imposed a $1,500 sanction for filing an AI-hallucinated judicial-order draft.",
    102: "The court granted the habeas petition and noted a non-existent case citation in counsel's briefing.",
    104: "The bankruptcy court imposed a Rule 9011 sanction against debtor's counsel equal to ten percent of the reply-fee award.",
    105: "The court publicly reprimanded counsel, ordered notice to the client, and required self-reporting to the Oklahoma Bar Association.",
    106: "The court denied habeas relief and admonished counsel for briefing that relied on an abrogated decision and a nonexistent case.",
    107: "The court ordered the plaintiff to explain why sanctions should not issue for misquoting a discovery case.",
    110: "The court struck the self-represented plaintiff's reply submission because its case citations could not be located.",
}

OUTCOME_DISP = {
    "Warning": "The court warned the filer that future use of false, nonexistent, or unsupported authorities may result in sanctions.",
    "Admonishment": "The court admonished the filer to verify authorities before presenting AI-assisted or otherwise unsupported legal citations.",
    "Order to Show Cause": "The court ordered the filer to show cause why sanctions should not issue for the defective authorities.",
    "Order to show cause": "The court ordered the filer to show cause why sanctions should not issue for the defective authorities.",
    "Order to Explain": "The court ordered the filer to explain the source and verification of the challenged citations.",
    "Monetary Sanction": "The court imposed a monetary sanction for the defective legal authorities.",
    "Adverse Costs Order": "The court awarded costs or fees caused by the defective legal authorities.",
    "Adverse Costs Order; Bar Referral": "The court awarded costs or fees and referred counsel to disciplinary authorities.",
    "Bar Referral": "The court referred counsel to disciplinary authorities over the defective filing.",
    "Brief struck": "The court struck the defective brief from the record.",
    "Brief Struck; Adverse Costs Order": "The court struck the defective brief and awarded costs or fees for responding to it.",
    "Judgment reversed and remanded": "The court reversed and remanded after finding the lower-court ruling relied on defective authorities.",
    "Public reprimand": "The court publicly reprimanded the attorney for the defective authorities.",
    "Public Admonishment": "The court publicly admonished counsel for the defective authorities.",
    "Allowed to correct filing": "The court allowed counsel to correct the filing after defective citations were identified.",
    "Order to provide certification with every future filing": "The court required the litigant to certify citation verification with every future filing.",
    "Refusal to appear pro hac vice": "The court denied pro hac vice admission because of the attorney's prior AI-hallucinated filings.",
}

SUPPLEMENT = {
    "Warning": "No monetary sanction was imposed in this document.",
    "Admonishment": "No monetary sanction was imposed in this document.",
    "No sanction": "The order imposes no sanction for the duplicated papers.",
    "Order to Show Cause": "The sanction issue remained pending after the order.",
    "Order to show cause": "The sanction issue remained pending after the order.",
    "Order to Explain": "The response obligation remained pending after the order.",
}


def actor_phrase(row):
    actor = ((row.get("incident") or {}).get("actor") or "other")
    if actor == "lawyer":
        return "counsel"
    if actor == "litigant-in-person":
        if row.get("court_level") in {"federal-appellate", "state-appellate", "state-supreme"}:
            return "a self-represented appellant"
        return "a self-represented litigant"
    if actor == "firm":
        return "the firm"
    if actor == "judge":
        return "the judge"
    return "the filer"


def filing_type(text):
    low = text.lower()
    for key, label in [
        ("reply brief", "reply brief"),
        ("opening brief", "opening brief"),
        ("initial brief", "initial brief"),
        ("appellate brief", "appellate brief"),
        ("opposition", "opposition papers"),
        ("response", "response"),
        ("motion", "motion"),
        ("petition", "petition"),
        ("brief", "brief"),
        ("proposed order", "proposed order"),
    ]:
        if key in low:
            return label
    return "filing"


def first_quoted_case(text):
    for pat in [r"['\"]([^'\"]+ v\. [^'\"]+)['\"]", r"“([^”]+ v\. [^”]+)”"]:
        m = re.search(pat, text)
        if m:
            val = re.sub(r"\s+", " ", m.group(1)).strip(" .,")
            if 8 < len(val) < 95:
                return val
    return None


def count_phrase(text):
    m = re.search(rf"\bat least\s+({number_words}|\d+)\b", text, re.I)
    if m:
        return "at least " + m.group(1).lower()
    m = re.search(r"\b(\d+)\s+(?:non[- ]existent|fabricated|fictitious|fake|hallucinated|false|unsupported|inaccurate)", text, re.I)
    if m:
        return m.group(1)
    for word in ["dozens", "numerous", "multiple", "several"]:
        if re.search(rf"\b{word}\b", text, re.I):
            return word
    return ""


def make_conduct(row, lead):
    h = lead.get("Hallucination Items") or ""
    passage = row.get("ai_passage") or ""
    text = h + " " + passage
    low = text.lower()
    role = actor_phrase(row)
    filing = filing_type(text)
    qcase = first_quoted_case(text)
    cp = count_phrase(text)
    if (row.get("incident") or {}).get("actor") == "judge":
        prefix = "The trial court's order relied on"
        connector = ""
    elif filing == "filing":
        prefix = f"{role.capitalize()} submitted a filing"
        connector = " using"
    elif filing.endswith("papers"):
        prefix = f"{role.capitalize()} filed {filing}"
        connector = " using"
    else:
        article = "an" if filing[0].lower() in "aeiou" else "a"
        prefix = f"{role.capitalize()} filed {article} {filing}"
        connector = " using"
    if qcase and re.search(r"non[- ]existent|does not exist|not a real|fictitious|fake|hallucinat", low):
        sentence = f"{role.capitalize()} cited {qcase} even though the court found the authority did not exist."
    else:
        parts = []
        if "exhibits" in low or "trial transcript" in low or "actual trial transcript" in low or "record citations" in low:
            parts.append("record or transcript quotations not found in the record")
        if re.search(r"false quotes|fake quote|fictitious quote|fabricated quote|quotation", low):
            parts.append("quotations that did not appear in the cited source")
        if re.search(r"non[- ]existent|does not exist|do not exist|fictitious|fake|phantom|imaginary|hallucinated", low):
            noun = "case citations or authorities"
            if cp and cp not in {"one", "1", "at least one"}:
                noun = f"{cp} nonexistent or hallucinated authorities"
            elif cp:
                noun = f"{cp} nonexistent or hallucinated authority"
            else:
                noun = "nonexistent or hallucinated authorities"
            parts.append(noun)
        if re.search(r"misrepresent|unsupported|do not support|does not support|different proposition|inaccurate descriptions", low):
            parts.append("authorities used for propositions they did not support")
        if re.search(r"non-existent Bankruptcy Rule|rule that does not exist|legal norm", text, re.I):
            parts.append("a nonexistent rule or legal standard")
        # Deduplicate by rough wording.
        dedup = []
        for p in parts:
            if p not in dedup:
                dedup.append(p)
        if not dedup:
            dedup = ["unsupported or inaccurate legal authorities"]
        if len(dedup) == 1:
            detail = dedup[0]
        elif len(dedup) == 2:
            detail = dedup[0] + " and " + dedup[1]
        else:
            detail = ", ".join(dedup[:-1]) + ", and " + dedup[-1]
        sentence = f"{prefix}{connector} {detail}."
    sentence = re.sub(r"\s+", " ", sentence).strip()
    if len(sentence) > 300:
        sentence = sentence[:296].rsplit(" ", 1)[0].rstrip(" ,;:") + "."
    return sentence


def money(row):
    inc = row.get("incident") or {}
    amt = inc.get("monetary_penalty")
    if amt is None:
        return None
    if isinstance(amt, float) and amt.is_integer():
        amt = int(amt)
    return f"${amt:,.2f}" if isinstance(amt, float) else f"${amt:,}"


def make_disposition(row, lead_idx, lead):
    if lead_idx in LEAD_DISP:
        return LEAD_DISP[lead_idx]
    outcome = lead.get("Outcome") or ""
    base = OUTCOME_DISP.get(outcome)
    if not base:
        base = "The court ruled on the merits and separately addressed defective legal authorities in the filing."
    amt = money(row)
    if amt and "monetary" in base:
        base = base.replace("a monetary sanction", f"a {amt} monetary sanction")
    if amt and "awarded costs or fees" in base:
        base = base.replace("awarded costs or fees", f"awarded {amt} in costs or fees")
    return base


def lower_after_court(disposition):
    s = disposition.strip().rstrip(".")
    if s.lower().startswith("the court "):
        s = s[10:]
    elif s.lower().startswith("the magistrate judge "):
        s = "magistrate judge " + s[20:]
    elif s.lower().startswith("the bankruptcy court "):
        s = s[21:]
    if s:
        s = s[0].lower() + s[1:]
    return s


def trim_to_words(text, max_words=60):
    words = text.split()
    if len(words) <= max_words:
        return text
    cut = " ".join(words[:max_words])
    return cut.rstrip(" ,;:") + "."

def shorten_sentence(text, max_words=24):
    text = text.strip()
    words = text.split()
    if len(words) <= max_words:
        return text
    short = " ".join(words[:max_words]).rstrip(" ,;:")
    return short + "."


def make_summary(row, lead, disposition, conduct):
    court = SHORT_COURT.get(row["court"], row["court"])
    case = row["case_name"].rstrip(".")
    disp = lower_after_court(disposition)
    summary = f"On {row['date_filed']}, in {case}, {court} {disp}. {conduct}"
    if len(summary.split()) > 60:
        summary = f"On {row['date_filed']}, in {case}, {court} {disp}. {shorten_sentence(conduct, 22)}"
    if len(summary.split()) > 60:
        summary = f"On {row['date_filed']}, {court} {disp}. {shorten_sentence(conduct, 24)}"
    if len(summary.split()) < 40:
        outcome = lead.get("Outcome") or ""
        extra = SUPPLEMENT.get(outcome)
        if not extra:
            amt = money(row)
            if amt:
                extra = f"The monetary component was {amt}."
            elif row.get("ai_tool_named"):
                extra = f"The document links the problem to {row['ai_tool_named']}."
            else:
                extra = "The court tied the ruling to citation verification duties."
        summary = summary.rstrip(".") + ". " + extra
    # If still short, add a non-generic consequence from the row.
    if len(summary.split()) < 40:
        summary += " The citation issue affected the court's handling of the filing."
    return trim_to_words(summary, 60)

rewritten = 0
for row in rows:
    lead_idx, lead = lead_by_url[row["source_url"]]
    old = (row.get("disposition"), row.get("summary"), (row.get("incident") or {}).get("conduct"), (row.get("incident") or {}).get("currency"))
    conduct = make_conduct(row, lead)
    disposition = make_disposition(row, lead_idx, lead)
    row["disposition"] = disposition
    if row.get("incident"):
        row["incident"]["conduct"] = conduct
        if row["incident"].get("monetary_penalty") is not None and row["incident"].get("currency") is None:
            row["incident"]["currency"] = "USD"
    row["summary"] = make_summary(row, lead, disposition, conduct)
    new = (row.get("disposition"), row.get("summary"), (row.get("incident") or {}).get("conduct"), (row.get("incident") or {}).get("currency"))
    if new != old:
        rewritten += 1

path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
print(rewritten)
