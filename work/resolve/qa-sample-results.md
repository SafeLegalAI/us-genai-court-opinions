# QA sample results

| decision_id | verification | grade | field | as coded | should be | evidence quote |
|---|---|---|---|---|---|---|
| ncwd-2026-smith-v-polk-county | fetched-and-read | PASS | all checked | — | — | — |
| in-re-ap-ohio-2026 | fetched-and-read | ERROR | primary_topic/topics; incident | `pro-se-ai-use`; no incident | `fabricated-citations`; add incident: actor=`litigant-in-person`, outcome=`warning`, ai_tool=`artificial intelligence` | “false citations not only will be disregarded by this court, but may result in sanctions” |
| ca5-2026-guerra-quezada-v-united-states | fetched-and-read | PASS | all checked | — | — | — |
| fladistctapp-2026-hulse-gibson-v-hulse | fetched-and-read | PASS | all checked | — | — | — |
| njd-2026-kurelko-v-ballard | fetched-and-read | PASS | all checked | — | — | — |
| pangelinan-guam-2026 | fetched-and-read | ERROR | primary_topic/topics; incident | `pro-se-ai-use`; no incident | `fabricated-citations`; add incident: actor=`litigant-in-person`, outcome=`warning`, ai_tool=`generative artificial intelligence` | “two nonexistent citations may be attributed to generative artificial intelligence use” |
| ark-rule-220-2025 | fetched-and-read | PASS | all checked | — | — | — |
| indctapp-2026-holstein-v-holstein | fetched-and-read | PASS | all checked | — | — | — |
| mathis-fl-2026 | fetched-and-read | ERROR | primary_topic/topics; incident | `pro-se-ai-use`; no incident | `fabricated-citations`; add incident: actor=`litigant-in-person`, outcome=`warning`, ai_tool=`artificial intelligence` | “the husband cites two cases which do not exist” |
| illappct-2026-scott-v-illinois-human-rights-commission | fetched-and-read | PASS | all checked | — | — | — |
| dc-2026-douglas-v-deutsche-bank-national-trust | fetched-and-read | PASS | all checked | — | — | — |
| insd-2026-harris-v-wray | fetched-and-read | PASS | all checked | — | — | — |
| ca11-2024-snell-v-united-specialty | fetched-and-read | PASS | all checked | — | — | — |
| nhd-2026-turgeon-v-fhlmc | fetched-and-read | ERROR | incident.outcome | `other` | `strike-off` | “objection to the motion to dismiss would be stricken” |
| ca6-2025-smith-v-pam-transport | fetched-and-read | PASS | all checked | — | — | — |
| texas-rule-2026 | mirror-read | PASS | all checked | — | — | — |
| cod-2026-y-s-v-john-doe | mirror-read | PASS | all checked | — | — | — |
| nvd-2026-seeto-v-kendall | mirror-read | ERROR | docket_number; disposition | `2:25-cv-00038-JAD-EJY Order Denying Motions`; warning-only disposition | `2:25-cv-00038-JAD-EJY`; disposition should say both motions were denied and then warn about citation defects | “Case No.: 2:25-cv-00038-JAD-EJY”; “I deny his motion for summary judgment” |
| nmd-2026-rasheem-carter-v-uzglobal | mirror-read | ERROR | incident.conduct | “four fabricated case citations” | Sixteen total nonexistent cases across the March response brief and two motions to compel | “sixteen total cases across the March response brief and two motions to compel that did not exist” |
| calctapp-2026-samuel-k-v-winsley-focia | mirror-read | ERROR | docket_number; incident.conduct | `No. 24STRO08015)`; “three citation defects” | `B346730`; lower court `Los Angeles County Super. Ct. No. 24STRO08015`; conduct should reflect 12 quotations, 11 fabricated | “B346730”; “In total, Focia's opening brief contains 12 quotations, 11 of which are fabrications” |
| mied-2026-hardy-v-genesee-county-community | mirror-read | ERROR | disposition | Struck consolidation motion and “gave ... a final warning” | Struck motion to consolidate and denied renewed motion to compel; no new final warning in this order | “Court STRIKES Hardy’s motion to consolidate”; “DENIES Hardy’s renewed motion to compel” |
| arizctapp-2026-in-re-termination-of-parental-rights | mirror-read | PASS | all checked | — | — | — |
| minnctapp-2026-young-v-young | mirror-read | PASS | all checked | — | — | — |
| tnwd-2026-reaves-law-firm-pllc-v-baker-donelson-bearman | mirror-read | ERROR | incident.monetary_penalty/currency | `1`, `USD` | `null`, `null`; fees/costs were ordered later after accounting, not fixed at $1 | “Defendants must file an accounting of their costs and attorneys’ fees” |
| cacd-2026-tqj-v-jennifer-esquivel | mirror-read | PASS | all checked | — | — | — |
| insd-2026-jana-james-v-national-board-of | mirror-read | ERROR | docket_number; disposition; incident.outcome | `6). As relief`; warning-only disposition; outcome=`other` | `No. 1:23-cv-01607-JPH-TAB`; disposition should include summary judgment for NBOME; outcome=`warning` | “No. 1:23-cv-01607-JPH-TAB”; “GRANTS NBOME’s motion for summary judgment” |
| nysupct-2026-doe-j-v-trustees-of-columbia-university | mirror-read | ERROR | docket_number; incident.outcome | `002 003 004`; outcome=`other` | `Index No. 166690/2025`; outcome=`warning` | “INDEX NO. 166690/2025”; “it does wish to issue a warning” |
| nced-2026-curry-v-capital-one-auto-finance | mirror-read | ERROR | docket_number; disposition | `P. 12(b)(6). The focus is on`; disposition only mentions leave denial | `No. 5:25-CV-164-BO-KS`; disposition should say motion to dismiss granted and leave to amend denied | “No. 5:25-CV-164-BO-KS”; “motion to dismiss is granted and leave to amend is denied” |
| ga-2026-hannah-renee-payne-v-state | mirror-read | ERROR | docket_number | `S26A0459 Hannah Renee Payne v. The State On Appeal` | `No. S26A0459`; lower-court `No. 2019CR0173714` | “No. S26A0459”; “No. 2019CR0173714” |
| iowactapp-2026-christ-apostolic-temple-dwight-reed-and-jordan | mirror-read | MINOR | ai_tool_named; incident.ai_tool | `GAI` | Use document wording `generative artificial intelligence`; no specific product named | “generative artificial intelligence to prepare his briefs” |
| nmd-2026-neri-v-board-of-education-for-albuquerque-public-schools | mirror-read | ERROR | ai_tool_named; incident.ai_tool | `null`; `null` | `Centient AI` for the AI-linked filing described in the incident | “sources from Centient AI” |
| ned-2026-kadlaskar-v-uscis | mirror-read | PASS | all checked | — | — | — |
| wawd-2026-ledoux-v-outliers-summary-judgment | mirror-read | PASS | all checked | — | — | — |
| asbca-2026-endure-industries-v-defense-health-agency | mirror-read | ERROR | incident.conduct | Refers to nonexistent `LLC v. United States` / `Corp. v. United States` | Should identify fake `BMS, Inc. v. United States` and related `Johns-Manville` support problem | “BMS, Inc. v. United States, 12 Cl. Ct. 33 (1987)” |
| utd-2026-regan-wilkes-v-canyons-school-district | mirror-read | ERROR | incident.conduct | “opposition” with `J.M. v. Francis Howell` | Nonexistent case law was in the Amended Complaint; listed cases were `F.C.`, `A.D.`, and `A.S.` | “Amended Complaint relies on non-existent case law” |
| txsd-2026-kenneth-hawkins-v-i-c-system | mirror-read | PASS | all checked | — | — | — |
| kyctapp-2026-pamela-blair-v-sanctuary-bluff-homeowners-association | mirror-read | MINOR | incident.conduct | Garbled authority `Co. v. Thompson, 11` | Use full authority name `Goodyear Tire & Rubber Co. v. Thompson, 11 S.W.3d 575` | “Goodyear Tire & Rubber Co. v. Thompson, 11 S.W.3d 575” |
| tnmd-2026-in-re-bfi-waste-systems | mirror-read | PASS | all checked | — | — | — |
| nvd-2026-kim-elizabeth-harwell-v-westcare-nevada | mirror-read | PASS | all checked | — | — | — |
| nmd-2026-sample-v-hilton-worldwide-holdings | mirror-read | ERROR | ai_tool_named; incident.ai_tool | `GAI`; `GAI` | `null`; document warns about fabricated/nonexistent authority but does not mention AI/GAI | “citations to nonexistent cases may result in sanctions” |
| pamd-2026-marble-v-o-malley | mirror-read | PASS | all checked | — | — | — |
| iowactapp-2026-state-of-iowa-ex-rel-j-g-v-mynesia-a-anderson | mirror-read | ERROR | incident.outcome | `other` | `dismissal` | “the only available remedy is dismissal” |
| ilnd-2026-hatch-v-college-ave-student-loans | mirror-read | PASS | all checked | — | — | — |
| dcd-2026-andre-lamont-goddard-jr-v-city-university-of-seattle | mirror-read | MINOR | incident.conduct | “five citation defects involving mischaracterized authority, incorrect statutory or rule text” | Five nonexistent cases; reporter numbers returned unrelated cases, not statutory/rule text | “includes citation to several cases that do not appear to exist” |
| ca10-2026-ryan-michael-jarvis-v-county-of-teton-wyoming | mirror-read | PASS | all checked | — | — | — |
| fladistctapp4-2026-innocent-v-meraki-installers | mirror-read | ERROR | primary_topic; incident.conduct | `fabricated-citations`; conduct includes nonexistent/hallucinated authorities | This document concerns trial-transcript quotations not found in the record; do not code nonexistent legal authorities | “multiple quotations from the trial transcript contained in Appellant’s initial brief that do not appear to be found anywhere in the actual trial transcript” |
| azctapp-2026-boettcher-v-boettcher | mirror-read | ERROR | incident.outcome | `other` | `strike-off` | “We strike the apparently false quotation” |
| vaed-2026-burnley-v-valentin | mirror-read | PASS | all checked | — | — | — |
| vaeb-2026-in-re-mahar | mirror-read | ERROR | docket_number | `25-72454-SCS; Adv. No. 25-07027-SCS` | `Case No. 25-72454-SCS; APN/Adv. Proc. No. 25-07035-SCS` | “Case No. 25-72454-SCS”; “APN 25-07035-SCS” |
| ncwd-2026-ebony-sherisse-lucas-v-charles-w-scharf | mirror-read | ERROR | date_filed | `2026-02-24` | `2026-02-25` filed date | “Filed 02/25/2026” |

## Counts

- PASS: 25
- MINOR: 3
- ERROR: 22
- Error rate: 22/50 = 44.0%

## Error rate by verification state

| verification | total | PASS | MINOR | ERROR | ERROR rate |
|---|---:|---:|---:|---:|---:|
| fetched-and-read | 15 | 11 | 0 | 4 | 4/15 = 26.7% |
| mirror-read | 35 | 14 | 3 | 18 | 18/35 = 51.4% |

## Three most common error kinds

1. Incident coding errors (missing incidents, wrong outcome, conduct, tool, or penalty): 16 rows.
2. Docket/date metadata extraction errors: 8 rows.
3. Incomplete or overstated dispositions / wrong primary topic: 8 rows combined.

No material `ai_passage` quotation mismatches were found; only PDF/layout spacing and column-order artifacts were disregarded.
