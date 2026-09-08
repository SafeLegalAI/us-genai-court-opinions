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

**567 court-authored US documents (opinions, orders, concurrences, dissents, administrative orders) that substantively discuss generative AI, each coded by topic, with the public-domain passage quoted, plus 9 legal-AI litigation dockets with dated milestones.**

Built 2026-09-08 by [SafeLegalAI](https://safelegalai.com) (Cognesio LLP). Canonical pages: [safelegalai.com/courts](https://safelegalai.com/courts) · repository, pipeline and issues: [https://github.com/SafeLegalAI/us-genai-court-opinions](https://github.com/SafeLegalAI/us-genai-court-opinions) · this mirror: [https://huggingface.co/datasets/safelegalaidata/us-genai-court-opinions](https://huggingface.co/datasets/safelegalaidata/us-genai-court-opinions).

| table | rows | one row is |
|---|---|---|
| `decisions` | 567 | one court-authored document discussing generative AI |
| `litigation` | 9 | one proceeding with a legal-AI company or product as a party |

Every row carries `source_url`, `fetched_at` and, where the Wayback Machine accepted the page, `archive_url`; `url` links the canonical page on safelegalai.com; `notice` carries the terms below. Full schemas: `schema/`.

A `decisions` row is one court-authored document: `case_name`, `court`, `court_level`, `state`, `date_filed`, `citation`, `docket_number`, `document_type`, `topics[]` (fabricated-citations · court-ai-use · evidence-authentication · discovery-ediscovery · privilege-work-product · unauthorized-practice · criminal-justice-algorithms · pro-se-ai-use · competence-fees · rules-by-opinion · substantive-ai-law), `primary_topic`, `court_used_ai`, `ai_tool_named`, `disposition`, the verbatim public-domain `ai_passage`, `cited_authorities[]`, a 40–60-word `summary`, `incident{}` (conduct/outcome/actor/penalty when the row is a fabricated-citation decision) and `tracker_slug` (its canonical page in the SafeLegalAI incident tracker). A `litigation` row is one proceeding in which a legal-AI company or product is a party, with dated `milestones[]`.

### `decisions` by `primary_topic`

| value | rows |
|---|---|
| fabricated-citations | 522 |
| pro-se-ai-use | 10 |
| rules-by-opinion | 8 |
| criminal-justice-algorithms | 6 |
| substantive-ai-law | 5 |
| evidence-authentication | 5 |
| court-ai-use | 4 |
| discovery-ediscovery | 3 |
| competence-fees | 2 |
| privilege-work-product | 2 |

### `decisions` by `court_level`

| value | rows |
|---|---|
| federal-district | 319 |
| state-appellate | 145 |
| federal-appellate | 28 |
| state-supreme | 26 |
| state-trial | 26 |
| federal-bankruptcy | 11 |
| federal-specialty | 10 |
| other | 2 |

### `decisions` by `state`

| value | rows |
|---|---|
| CA | 53 |
| NY | 49 |
| TX | 32 |
| FL | 28 |
| IL | 27 |
| AZ | 21 |
| MI | 19 |
| OH | 18 |
| IN | 18 |
| PA | 16 |
| WA | 16 |
| AL | 13 |
| OR | 13 |
| MD | 12 |
| NV | 11 |

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

> SafeLegalAI (Cognesio LLP), "US court decisions on generative AI", v0.1.2, 2026-09-08. https://huggingface.co/datasets/safelegalaidata/us-genai-court-opinions — CC BY 4.0. Canonical: https://safelegalai.com/courts

```bibtex
@dataset{safelegalai_us_genai_court_opinions_0_1_2,
  title        = {US court decisions on generative AI},
  author       = {{SafeLegalAI (Cognesio LLP)}},
  year         = {2026},
  version      = {0.1.2},
  url          = {https://safelegalai.com/courts},
  note         = {Mirror: https://huggingface.co/datasets/safelegalaidata/us-genai-court-opinions. Data CC BY 4.0. Built 2026-09-08.}
}
```
