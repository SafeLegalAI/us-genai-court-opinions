---
license: cc-by-4.0
pretty_name: "US court decisions on generative AI — coded corpus (SafeLegalAI)"
language:
  - en
size_categories:
  - n<1K
tags:
  - courts
  - judicial-opinions
  - generative-ai
  - chatgpt
  - hallucination
  - evidence
  - public-domain
  - legal
  - law
  - ai-regulation
  - ai-safety
  - ai-governance
  - safelegalai
configs:
  - config_name: decisions
    default: true
    data_files:
      - split: train
        path: data/decisions.parquet
  - config_name: litigation
    data_files:
      - split: train
        path: data/litigation.parquet
---

# US court decisions on generative AI

**566 court-authored US documents (opinions, orders, concurrences, dissents, administrative orders) that address generative AI or the fabricated authorities courts associate with it — `ai_mention` says whether the court itself names AI — each coded by topic, with the public-domain passage quoted, plus 9 legal-AI litigation dockets with dated milestones.**

Built 2026-09-08 by [SafeLegalAI](https://safelegalai.com) (Cognesio LLP). Canonical pages: [safelegalai.com/courts](https://safelegalai.com/courts) · repository, pipeline and issues: [https://github.com/SafeLegalAI/us-genai-court-opinions](https://github.com/SafeLegalAI/us-genai-court-opinions) · this mirror: [https://huggingface.co/datasets/safelegalaidata/us-genai-court-opinions](https://huggingface.co/datasets/safelegalaidata/us-genai-court-opinions).

| table | rows | one row is |
|---|---|---|
| `decisions` | 566 | one court-authored document discussing generative AI |
| `litigation` | 9 | one proceeding with a legal-AI company or product as a party |

Every row carries `source_url`, `fetched_at` and, where the Wayback Machine accepted the page, `archive_url`; `url` links the canonical page on safelegalai.com; `notice` carries the terms below. Full schemas: `schema/`.

A `decisions` row is one court-authored document: `case_name`, `court`, `court_level`, `state`, `date_filed`, `citation`, `docket_number`, `document_type`, `topics[]` (fabricated-citations · court-ai-use · evidence-authentication · discovery-ediscovery · privilege-work-product · unauthorized-practice · criminal-justice-algorithms · pro-se-ai-use · competence-fees · rules-by-opinion · substantive-ai-law), `primary_topic`, `court_used_ai`, `ai_mention` (explicit · implied · none — whether the court itself names AI, infers it or only says the authorities do not exist), `ai_tool_named` (only when the court names it), `disposition`, the verbatim public-domain `ai_passage`, `cited_authorities[]`, a 40–60-word `summary`, `incident{}` (conduct/outcome/actor/penalty when the row is a fabricated-citation decision; `outcome` is the most severe consequence the court imposed in that document, on a defined ladder from strike-off down to filing-struck, warning, pending and none) and `tracker_slug` (its canonical page in the SafeLegalAI incident tracker). A `litigation` row is one proceeding in which a legal-AI company or product is a party, with dated `milestones[]`.

### `decisions` by `primary_topic`

| value | rows |
|---|---|
| fabricated-citations | 507 |
| pro-se-ai-use | 18 |
| rules-by-opinion | 10 |
| evidence-authentication | 7 |
| criminal-justice-algorithms | 6 |
| substantive-ai-law | 5 |
| discovery-ediscovery | 4 |
| court-ai-use | 4 |
| competence-fees | 3 |
| privilege-work-product | 2 |

### `decisions` by `verification`

| value | rows |
|---|---|
| fetched-and-read | 300 |
| mirror-read | 266 |

### `decisions` by `ai_mention`

| value | rows |
|---|---|
| explicit | 435 |
| none | 118 |

### `litigation` by `status`

| value | rows |
|---|---|
| judgment | 3 |
| dismissed | 2 |
| active | 1 |
| settled | 1 |
| consent-order | 1 |
| on-appeal | 1 |

### `litigation` by `qualifier`

| value | rows |
|---|---|
| upl-consumer | 3 |
| database-terms | 2 |
| copyright-training | 2 |
| trade-secret-vendor | 1 |
| regulator-consumer | 1 |

### `litigation` by `court`

| value | rows |
|---|---|
| U.S. District Court for the Northern District of California | 2 |
| Supreme Court of British Columbia | 1 |
| Federal Trade Commission | 1 |
| U.S. District Court for the Southern District of Illinois | 1 |
| Bundesgerichtshof | 1 |
| U.S. District Court for the District of Delaware; U.S. Court of Appeals for the Third Circuit | 1 |
| Cour d’appel de Paris, Pôle 5, Chambre 1 | 1 |
| U.S. District Court for the District of Minnesota | 1 |

## Quality and known limits

This release is the first after an independent audit. On 8 September 2026 a 50-row random sample was re-read by an agent that had not written the rows: every quoted passage was verbatim and every case, court and date was right, but 22 of the 50 rows (44%) had at least one error in a coding column — the outcome enum used loosely ("other" as a catch-all; "strike-off", which means removed from the roll, used for a filing being struck), docket fields holding caption fragments, a generic "AI" label recorded as a named tool, and passages that never reached the court's AI reference. Because the errors were systematic, every row was then re-read from the document by a second, independent pass against a written rubric (work/recode/RUBRIC.md); the changes were applied through a validated overlay with a field-level log (work/recode/applied-2026-09-08-*.jsonl).

- **2026-09-08** — Independent re-read of a 50-row random sample (seed 20260908). 22 rows with ≥1 coding error (44%); 0 passage or identification errors. Threshold for a full re-read was 5%.
- **2026-09-08** — Full second read of every row from the court document, six independent agents, one rubric. 555 of 569 rows re-coded; 14 could not be re-fetched (court hosts unreachable that day) and carry "Second read pending" in notes; 1 row withdrawn because the document was counsel's letter, not a court document. 3,025 field changes across 568 rows: 197 outcomes re-coded (58 from "other" to the new "none"; all 7 "strike-off" rows re-coded — none was a removal from the roll), 343 docket strings normalised, 95 generic "AI" labels moved out of the tool field into the new ai_mention column, 5 placeholder penalties set to null, topics changed on 133 rows.
- **2026-09-08** — Official-copy resolution: GovInfo (USCOURTS) API by docket with the quoted passage required to match; state-court archives by hand-briefed agents; CourtListener RECAP search within Free Law Project's published limits. (CourtListener: 106 searches on 8 Sep → 6 rows.) 300 of 566 rows now read from the court's own copy or the public RECAP archive (from 53). 266 remain read from a public copy of the court's PDF: the court does not publish the order online, or its site refuses the identified bot (69 rows, queued for hand download), or the host timed out.

The ai_mention column says whether the court itself names AI (435 rows), or only says the authorities do not exist or are misquoted (118); the corpus includes the last group because the pattern is the one courts associate with generative AI, and readers who want only decisions that name AI can filter on it. The outcome column is the most severe consequence the court imposed in that document, on a defined ladder; it is not a finding about any person. A quarterly 50-row independent re-read is standing practice and its result replaces this one.

## Method

Leads came from Damien Charlotin's AI Hallucination Cases Database (CC BY 4.0, damiencharlotin.com — confirmed by the author on 8 September 2026; the Zenodo record 10.5281/zenodo.21845901 is a third-party snapshot he does not stand behind and is not cited here), the CourtListener search index (discovery only, within its public rate limits; a partnership request to Free Law Project is pending), court-website searches and news reports; every document was then fetched from the issuing court's site, govinfo.gov or the public RECAP archive and read. Coding is conservative and the passage is quoted so readers can check it. Fabricated-citation decisions have one canonical page in the incident tracker; this corpus links to it rather than duplicating it.

**Attribution for leads.** Leads from Damien Charlotin's AI Hallucination Cases Database (CC BY 4.0), damiencharlotin.com; each decision re-read and coded by SafeLegalAI.

SafeLegalAI records what courts, regulators, legislatures and vendors' own public pages state; it does not infer, rank or advise. Coding columns are SafeLegalAI's good-faith reading for comparison, not findings about any person or body. Corrections and right of reply: [safelegalai.com/report](https://safelegalai.com/report).

## Licence and notices

Opinions, orders and rules of United States courts are public domain (17 U.S.C. § 105; *Banks v. Manchester* (1888); *Georgia v. Public.Resource.Org* (2020)). The compilation and coding are **CC BY 4.0** — attribute *SafeLegalAI (safelegalai.com), published by Cognesio LLP*. Code is Apache-2.0.

Provided as is, without warranty. Not legal advice. SafeLegalAI (Cognesio LLP) records what courts, regulators, legislatures and vendors' own public pages state; the linked official documents are the record. Names and marks belong to their owners. Anyone named may reply: https://safelegalai.com/report. Full terms: https://safelegalai.com/disclaimer See `DISCLAIMER.md` and `NOTICE` in this repository.

## Uses

**Suited to:** counting and comparing what the record shows (by court, jurisdiction, date, actor, outcome, status); building watch-lists and alerts from `source_url`/`fetched_at`; grounding retrieval or summarisation on cited primary documents; teaching and library guides that need a dated, sourced list.

**Not suited to:** ranking products, people or courts; inferring prevalence beyond what a court or regulator has itself stated; any use that treats a coding column as a finding of fact or law. Where a row names a person or organisation it does so as they appear in a public document; anyone named may request a correction or right of reply at https://safelegalai.com/report.

## Cite

> SafeLegalAI (Cognesio LLP), "US court decisions on generative AI", v0.2.1, 2026-09-08. https://huggingface.co/datasets/safelegalaidata/us-genai-court-opinions — CC BY 4.0. Canonical: https://safelegalai.com/courts

```bibtex
@dataset{safelegalai_us_genai_court_opinions_0_2_1,
  title        = {US court decisions on generative AI},
  author       = {{SafeLegalAI (Cognesio LLP)}},
  year         = {2026},
  version      = {0.2.1},
  url          = {https://safelegalai.com/courts},
  note         = {Mirror: https://huggingface.co/datasets/safelegalaidata/us-genai-court-opinions. Data CC BY 4.0. Built 2026-09-08.}
}
```
