# Agent brief — US court decisions on generative AI (read AGENT-BRIEF-COMMON.md first, then `schema/decisions.schema.json`)

**Dataset.** Every court-authored US document filed on or after 2022-11-30 that **substantively** discusses generative AI or large language models (at least a paragraph of analysis, or a holding) — opinions, memorandum opinions, orders, concurrences, dissents, administrative orders adopted by opinion, reports and recommendations. Coded by topic; the AI passage quoted verbatim (US court documents are public domain, so quote generously: the passage that a reader needs to see, typically 60–400 words, up to 4,000 characters).

**Inclusion rule.** Include if the court itself writes about generative AI/LLMs/ChatGPT/"AI-generated" content. Exclude: mere mention of "artificial intelligence" in a party's product description; patents on AI; standing orders that are not decisions (those are in `us-court-ai-orders` — but an *opinion* or *administrative order issued as an opinion* adopting a rule is `rules-by-opinion`). General AI law (copyright/fair use, authorship, AI-CSAM, platform liability) is included **only** as `substantive-ai-law` when the decision is one legal audiences cite (Thomson Reuters v. Ross; Bartz v. Anthropic; Kadrey v. Meta; Thaler v. Perlmutter; U.S. v. Anderegg) — do not sweep in every AI copyright ruling.

**Topics** (choose all that apply; `primary_topic` is the one the decision is mostly about):
- `fabricated-citations` — sanctions/show-cause/warnings for hallucinated or misquoted authorities. Fill the `incident{}` object (conduct, outcome, actor, penalty, tool). If the case is already at safelegalai.com/tracker/<slug> (check `work/tracker-slugs.txt`), set `tracker_slug`.
- `court-ai-use` — the court discloses or discusses using AI itself (e.g. *Snell v. United Specialty Ins.*, 11th Cir. 2024, Newsom J. concurring; *Ross v. United States*, D.C. 2025; *Deleon*). Set `court_used_ai: true` only when the court says it used a tool.
- `evidence-authentication` — AI-generated/altered/enhanced evidence, deepfake challenges, FRE 901/902/702. (The `ai-evidence-in-court` dataset holds the detailed coding; here just record the decision.)
- `discovery-ediscovery` — TAR/genAI in discovery, AI-assisted review, privilege logs.
- `privilege-work-product` — privilege over AI chats/prompts (e.g. *U.S. v. Heppner*, S.D.N.Y. 2026).
- `unauthorized-practice` — AI services and UPL, non-lawyer AI advice.
- `criminal-justice-algorithms` — risk assessment, forensic software, AI in sentencing/policing with court analysis.
- `pro-se-ai-use` — self-represented litigants' AI use without sanction (courts explaining, tolerating or setting conditions).
- `competence-fees` — attorney competence, fee reductions for AI-assisted work, billing.
- `rules-by-opinion` — a court adopting an AI rule by opinion/administrative order (e.g. *2026 OK CR 7*; Ark. Sup. Ct. Admin. Order 25 (2025)).
- `substantive-ai-law` — see inclusion rule.

**Discovery.** (1) Your slice's lead file in `work/leads/` (Charlotin rows (CC BY 4.0 — attribute per dataset.json `attribution`) or CourtListener search hits with `download_url`s). (2) CourtListener anonymous search for discovery only, ≤100 requests total, e.g. `https://www.courtlistener.com/api/rest/v4/search/?q=%22generative+artificial+intelligence%22+OR+%22large+language+model%22+OR+ChatGPT&type=o&filed_after=2022-11-30&order_by=dateFiled+desc&court=<ids>` — take `download_url` (court site) as `source_url`; if only `local_path` exists, the PDF is at `https://storage.courtlistener.com/<local_path>` (allowed, ≤1 request/5 s) and `courtlistener_url` is `https://www.courtlistener.com/opinion/<cluster_id>/x/`. (3) Court websites' own opinion search (`site:<court host> "generative AI"` via web_search; `nycourts.gov/reporter`, `oscn.net`, `courts.ca.gov/opinions`, `txcourts.gov`, `flcourts.gov`, state supreme court sites). (4) News/blogs only as leads.

**Writing.** `decision_id`: `<court_code or court-slug>-<yyyy>-<short-case-slug>` e.g. `ca11-2024-snell-v-united-specialty`, `nysd-2023-mata-v-avianca`. `disposition` one sentence. `cited_authorities`: the authorities the AI passage itself cites. `summary` 40–60 words: court, date, what the court decided about AI, outcome. `text_sha256` of the PDF/HTML you read if you fetched it.

**Do not** write rows for non-US courts; do not duplicate a decision another slice owns (slices are split by court set/topic in your task); if a case has several documents (show-cause order, then sanctions opinion), write one row per court-authored document only when each substantively discusses AI — otherwise one row for the final decision and mention the others in `notes`.
