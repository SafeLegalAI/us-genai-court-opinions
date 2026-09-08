# Re-coding rubric — every decision row, re-read against the document (8 Sep 2026)

An independent 50-row audit found a 44% error rate: `strike-off` used for "filing struck" (the enum means struck off the roll), `other` as a dumping ground, `pro-se-ai-use` used where the substance was fabricated citations, docket fields holding sentence fragments, conduct descriptions that misstate counts, tools named that the court never named, and passages that never mention AI. You are re-coding your slice from the document itself. **Write to an overlay file, never to the source files** (other jobs are editing them): `work/recode/recode-<SLICE>.jsonl`, one JSON object per row with `decision_id` and only the fields below. A merge step applies them.

## For each row
1. Fetch the document at `source_url` (if `mirror_url` exists, `source_url` is already the official copy). Identify as `SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)`, ≤1 req/s; `pdftotext -layout`. Never Westlaw/Lexis/Justia/Google Scholar/Casetext. If the fetch fails, record `{"decision_id":…,"recode_status":"unfetchable","recode_notes":"…"}` and move on.
2. Read the parts that matter: caption (case name, court, docket, date), the passage(s) about AI/fabricated authority, and the disposition/ordering paragraphs.
3. Emit:

```
decision_id, recode_status: "recoded",
case_name            – as in the caption, short form (e.g. "Potterf v. Wessels"), no "et al" unless needed to disambiguate
court                – full official court name
docket_number        – canonical docket only, e.g. "1:26-cv-10860" · "No. 25-72454-SCS; Adv. No. 25-07035-SCS" · "B346730" · "S26A0459". No judge initials unless part of the court's own format, no party names, no sentence fragments. null if none printed.
citation             – reporter/neutral citation if printed on the document, else null
date_filed           – date on the document (filed/decided), ISO
document_type        – opinion · order · memorandum-opinion · report-and-recommendation · concurrence · dissent · administrative-order · other
ai_mention           – "explicit" (the court itself names AI / ChatGPT / a chatbot / LLM / generative AI / "hallucinated" or "hallucination") · "implied" (the court does not name AI but the *court* says the fabrication pattern suggests or is consistent with AI, or a party admitted AI use as recorded by the court) · "none" (the court never mentions AI, hallucination, chatbots or any tool — it only says the authorities do not exist / are misquoted)
ai_passage           – verbatim quotation (≤ 900 chars) that contains the court's AI reference if ai_mention is explicit/implied; otherwise the passage about the non-existent authorities. Use "..." for omissions. No paraphrase. Straight quotes.
primary_topic        – see topics
topics               – one or more of: fabricated-citations (the decision addresses authorities that do not exist or do not say what was claimed — regardless of who filed them; this is the topic for the 'pro se cited fake cases' situation) · pro-se-ai-use (ONLY when the substance is a self-represented party's AI use other than fabricated authorities, e.g. AI-drafted pleadings struck for other reasons, requests for AI assistance) · court-ai-use · evidence-authentication · discovery-ediscovery · privilege-work-product · unauthorized-practice · criminal-justice-algorithms · competence-fees · rules-by-opinion · substantive-ai-law
court_used_ai        – true only when the court says it used an AI tool itself
disposition          – one sentence, what the court ORDERED/decided (grant/deny/strike/dismiss/sanction/refer), including the non-AI operative outcome if any ("Motion to dismiss granted; plaintiff warned that further fabricated citations will draw sanctions.")
incident             – only when topics includes fabricated-citations (else null):
  actor              – lawyer · litigant-in-person · firm · judge · expert · other (who put the defective authority before the court)
  ai_tool            – exactly the product the court names as used ("ChatGPT", "Google Gemini", "Centient AI", "First Drafts"…), including a product the court records a party as having used or admitted to ("she explained that she used 'First Drafts'"). A generic label ("AI", "GAI", "generative artificial intelligence") is not a tool → null (ai_mention carries that the court names AI). Null also when the product appears only inside a citation to another case, in a hypothetical ("a tool such as ChatGPT") or in a denial. Never infer.
  conduct            – 1–2 sentences, specific and countable where the court is: how many authorities, in which filing(s), what was wrong (nonexistent / misquoted / misattributed), and any admission. No adjectives.
  outcome            – the MOST SEVERE that the court actually imposed in THIS document, by this order: strike-off (removed from roll/disbarred) > suspension (from practice) > referral (to a bar/regulator/disciplinary body/AG) > fine (money payable to the court) > costs-order (fees/costs payable to a party) > sanctions (any other formal sanction: CLE, admonition entered as sanction, filing bar, order to serve on client, show-cause resolved WITH a sanction) > dismissal (case/claim dismissed and the court ties it to the conduct) > filing-struck (the offending filing struck/disregarded, nothing more) > warning (caution/admonishment/certification order, show-cause discharged without sanction) > pending (show-cause issued, sanctions reserved) > none (the court noted the defective authorities and imposed NO consequence for them in this document — it decided the motion/appeal on other grounds and moved on) > other (explain in conduct — should be rare).
  monetary_penalty   – number only when a sum is fixed in this document; null otherwise (never 1 or 0 as a placeholder)
  currency           – "USD" when monetary_penalty is set, else null
recode_notes         – anything the merge should know (e.g. "document is a later order; earlier show-cause at ECF 12", "mirror PDF is a docket sheet, not the opinion")
```

## Rules
- Code what the court states. A party's brief is not the court. If the court reports a party's admission ("counsel admitted using ChatGPT"), that is the court stating it.
- One document = one row. If the mirror PDF is not a court-authored document (e.g. a party filing or a docket sheet), set `recode_status: "not-court-document"` and explain.
- Do not look up the case elsewhere to "improve" the coding; the row describes this document.
- Speed matters less than being right; each row you emit will be trusted.

Finish with counts: recoded / unfetchable / not-court-document; how many `ai_mention: none`; how many outcomes changed from the original (compare with the row's current `incident.outcome`); and any row where the mirror document differs from the case named.
