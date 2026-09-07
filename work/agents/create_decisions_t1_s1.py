import json, datetime
fetched_at = "2026-09-07T13:15:21.976-07:00"
rows = []
def add(**kw):
    base = dict(
        citation=None, docket_number=None, court_code=None, state=None,
        ai_tool_named=None, incident=None, tracker_slug=None,
        courtlistener_url=None, text_sha256=None, archive_url=None,
        notes=None,
    )
    base.update(kw)
    rows.append(base)

add(
 decision_id="dc-2026-douglas-v-deutsche-bank-national-trust",
 case_name="Douglas v. Deutsche Bank National Trust Company",
 court="District of Columbia Court of Appeals",
 court_code="dc", court_level="state-supreme", state="DC", date_filed="2026-09-03",
 docket_number="24-CV-1099", document_type="order",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 ai_tool_named="Google’s generative artificial intelligence search tool",
 disposition="The court struck Deutsche Bank's appellee brief and referred the matter to the Office of Disciplinary Counsel.",
 ai_passage="While reviewing appellee’s brief, the court discovered that it contained multiple citations to cases that the court was unable to locate or confirm as legitimate. On June 22, we issued an order requiring appellee to show cause “why the court should not strike its brief for citing nonexistent cases that are possibly the product of artificial intelligence (AI) hallucinations.” The next day, one of appellee’s attorneys at the firm, Loishirl W. Hall, filed a response in her own capacity. Ms. Hall confirmed that four of the brief’s cited authorities did not exist. She acknowledged that these citations were “not legitimate legal authority” and “should not have appeared in a brief filed with this Court.” Ms. Hall explained that she had “used Google’s generative artificial intelligence search tool to assist in locating case authority” and did not verify the existence or accuracy of those citations before filing the brief.",
 cited_authorities=["Abadie v. District of Columbia", "Cason v. Nat’l Consumer Co-op Bank", "Osborne v. District of Columbia", "Woods v. United States"],
 summary="The District of Columbia Court of Appeals strikes Deutsche Bank’s appellee brief after counsel admits that four cited authorities generated through Google’s AI search did not exist. The court also refers the matter to disciplinary counsel and stresses that signed appellate briefs require verified authorities.",
 incident={"conduct":"Counsel cited four nonexistent cases in an appellee brief after using Google’s generative AI search tool without verifying the authorities.","outcome":"referral","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":"Google’s generative artificial intelligence search tool"},
 tracker_slug="douglas-v-deutsche-bank-national-trust",
 courtlistener_url="https://www.courtlistener.com/opinion/10965874/douglas-v-deutsche-bank-national-trust-co-published-order/",
 text_sha256="e69cfc9a0871eeace25dbcf259a2fd6ca276d1d6f3519a4d7407c720d14fc538",
 source_url="https://www.dccourts.gov/sites/default/files/2026-09/Douglas%20v.%20Deutsche%20Bank%20Nat%27l%20Trt%20Co.%2024-CV-1099%20ORDER.pdf",
 fetched_at=fetched_at, verification="fetched-and-read", lead_source=["charlotin-cc0","courtlistener-search"],
 notes="Official D.C. Courts URL returned 403 to curl; read the matching public-domain PDF from CourtListener storage and recorded its SHA-256."
)

add(
 decision_id="hawapp-2026-state-v-presti",
 case_name="State of Hawaiʻi v. Cody Presti",
 court="Intermediate Court of Appeals of Hawaiʻi",
 court_code="hawapp", court_level="state-appellate", state="HI", date_filed="2026-08-31",
 citation=None, docket_number="CAAP-24-0000826", document_type="opinion",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court affirmed the judgment and declined to sanction the self-represented criminal appellant for nonexistent citations.",
 ai_passage="Of the eleven cases this court was unable to locate, six cases include citations that indicate a volume and reporter that correspond with a different case entirely: • On page 8 of the Opening Brief, Presti relies on “State V. Alves, 45. Haw.296,” but that citation leads to an unrelated case, State v. Pokini, 45 Haw. 295, 367 P.2d 499 (1961). • On page 17 of the Opening Brief, Presti relies on “State v. Bonds, 592 N.W.2d 262 (Minn. 1999),” but that citation leads to an unrelated case in another jurisdiction, Jackson v. DeWitt, 592 N.W.2d 262 (Wis. Ct. App. 1999). • On pages 28-29 of the Opening Brief, Presti relies on “State v. Pune, 94 Hawaiʻi 200 (2000),” but that citation leads to a table of fourteen unreported opinions that does not include State v. Pune. A Westlaw search of “State v. Pune” returns zero results in any jurisdiction. ... In these instances, the relied upon authority simply does not exist. We pause to note that Presti’s Opening Brief is just the next example of the alarming rise of citations to fake cases by attorneys and self-represented litigants in this jurisdiction and nationally.",
 cited_authorities=["State v. Alves", "State v. Pokini, 45 Haw. 295, 367 P.2d 499 (1961)", "State v. Bonds", "Jackson v. DeWitt, 592 N.W.2d 262 (Wis. Ct. App. 1999)", "State v. Pune", "State v. Branch, 636 P.2d 421 (Or. Ct. App. 1981)"],
 summary="The Hawaiʻi Intermediate Court of Appeals affirms a criminal judgment while documenting numerous nonexistent or misidentified cases in Cody Presti’s self-represented opening brief. The court explains sanction authority for fake citations but declines to apply civil Rule 11 procedures in the direct criminal appeal.",
 incident={"conduct":"Self-represented appellant relied on multiple nonexistent or mismatched appellate cases, including State v. Pune and State v. Alves.","outcome":"warning","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
 courtlistener_url="https://www.courtlistener.com/opinion/10964720/state-v-presti/",
 text_sha256="983e596930484529baeea338a537e03413d0827deb34b89415509f37bf3325f5",
 source_url="https://www.courts.state.hi.us/wp-content/uploads/2026/08/CAAP-24-0000826.pdf",
 fetched_at=fetched_at, verification="fetched-and-read", lead_source=["charlotin-cc0","courtlistener-search"],
 notes=None
)

add(
 decision_id="gand-2026-booker-v-kroger",
 case_name="Booker v. The Kroger Co.",
 court="United States District Court for the Northern District of Georgia",
 court_code="gand", court_level="federal-district", state="GA", date_filed="2026-08-28",
 docket_number="1:26-cv-02006-SDG", document_type="order",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court sanctioned plaintiff's counsel $8,000 and ordered proof of completed ethics and technology CLE training.",
 ai_passage="This matter is before the Court on its previous Order to Show Cause [ECF 53] directed to counsel for Plaintiff to explain why he should not be sanctioned for using fake or hallucinated case authorities, as well as misrepresenting the content of real case authorities, in his filings with the Court. Because Plaintiff’s counsel, as an officer of the Court, deliberately lied to this Court about his artificial intelligence (AI) use and because Plaintiff’s counsel’s response to the Order to Show Cause [ECF 58] lacks credibility, is evasive, and seeks to divert accountability from his own misconduct, sanctions are warranted. ... The Court’s Order to Show Cause highlighted four purported cases cited by Plaintiff’s counsel that represented the most egregious examples of fake, false, and misleading case authorities. Counsel for Plaintiff is ordered to pay a fine of $1,000 for each of these fake, false, and misleading case authorities. In addition, this fine will be doubled as a result of Plaintiff’s counsel’s lies to this Court. Accordingly, Plaintiff’s counsel’s total fine for his repeated Rule 11 violations is $8,000, payable to the registry of the Court.",
 cited_authorities=["Fed. R. Civ. P. 11"],
 summary="The Northern District of Georgia sanctions plaintiff’s counsel in Booker v. Kroger after finding fake, false and misleading case authorities and an untruthful denial of AI use. The order imposes an $8,000 court fine and requires documentation of completed ethics and technology CLE.",
 incident={"conduct":"Plaintiff’s counsel filed four fake, false or misleading case authorities and falsely told the court he had not used AI tools.","outcome":"fine","actor":"lawyer","monetary_penalty":8000,"currency":"USD","ai_tool":None},
 tracker_slug="booker-v-kroger",
 courtlistener_url="https://www.courtlistener.com/docket/73188597/66/booker-v-the-kroger-co/",
 text_sha256="ea403780c57123eac0dfa4f031df36280cd950922273c0674dadacbace1cc4c6",
 source_url="https://storage.courtlistener.com/recap/gov.uscourts.gand.358237/gov.uscourts.gand.358237.66.0.pdf",
 fetched_at=fetched_at, verification="fetched-and-read", lead_source=["charlotin-cc0","courtlistener-search"],
 notes="Court-authored PACER document read from CourtListener RECAP storage. A GovInfo package probe did not locate the order."
)

add(
 decision_id="nmd-2026-reyes-v-bailey",
 case_name="Reyes v. Bailey",
 court="United States District Court for the District of New Mexico",
 court_code="nmd", court_level="federal-district", state="NM", date_filed="2026-08-28",
 docket_number="2:24-cv-00831-KG-KRS", document_type="memorandum-opinion",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court denied Reyes's motion for sanctions and denied a motion to strike as moot.",
 ai_passage="Mr. Reyes appears to argue that Defendants have violated Rule 11 by “misrepresenting the record and the law.” Doc. 61 at 2. He contends that Defendants: (1) misrepresented that he hallucinated a case citation in his pleadings; (2) “failed to comply with 28 U.S.C. § 1446(a) by omitting critical state-court filings from the Notice of Removal”; (3) moved to quash the summons issued for improper service based on false factual assertions; (4) asserted an affirmative defense unsupported by existing law; and (5) failed to specifically controvert his statement of undisputed facts in their response to his motions for summary judgment, as required by Federal Rule of Civil Procedure 56. ... The Court rejects Mr. Reyes’s arguments and denies the motion. First, Mr. Reyes admits that he miscited a case in his Amended Complaint. See Doc. 65. Thus, Defendants’ contention that Mr. Reyes may have fabricated a case was reasonable.",
 cited_authorities=["Fed. R. Civ. P. 11", "28 U.S.C. § 1446(a)", "Fed. R. Civ. P. 56"],
 summary="The District of New Mexico denies self-represented plaintiff Charles Reyes’s Rule 11 motion. The court holds defendants reasonably said Reyes may have fabricated a case citation because Reyes admitted he miscited a case in his amended complaint, and the remaining alleged misrepresentations did not support sanctions.",
 incident={"conduct":"Self-represented plaintiff admitted misciting a case; defendants characterized the citation as possibly fabricated, and the court found that characterization reasonable.","outcome":"other","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
 courtlistener_url="https://www.courtlistener.com/docket/69106401/87/reyes-v-lcso/",
 text_sha256="a254ad5274b0457633043494557eafc903fdd71be9c83a76c14dd298b3b52eb0",
 source_url="https://storage.courtlistener.com/recap/gov.uscourts.nmd.505858/gov.uscourts.nmd.505858.87.0.pdf",
 fetched_at=fetched_at, verification="fetched-and-read", lead_source=["charlotin-cc0","courtlistener-search"],
 notes="Caption lists Bryce Bailey; CourtListener docket caption is Reyes v. LCSO."
)

add(
 decision_id="illappct-2026-noble-v-wmc-mortgage",
 case_name="Noble v. WMC Mortgage Corp.",
 court="Appellate Court of Illinois, First District",
 court_code="illappct", court_level="state-appellate", state="IL", date_filed="2026-08-28",
 citation="2026 IL App (1st) 251168-U", docket_number="1-25-1168", document_type="order",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court affirmed the denial of Noble's petition and noted a hallucinated citation in her brief.",
 ai_passage="Arguments that are unsupported by citation do not meet the requirements of Rule 341(h)(7) and are procedurally defaulted. Wing, 2016 IL App (1st) 153517, ¶11. We also note that Noble’s brief contains a “hallucinated” citation on page 10, which occurs when AI-generated responses are used and not verified. See In re Baby Boy, 2025 IL App (4th) 241427, ¶¶ 102-105. She cites Ferguson v. Georges, 389 Ill. App. 3d 543, 553-54 (2010) to state the standard of review for the circuit court’s denial of leave to amend. However, our research has determined that the citation is actually contained within People v. Mott, 389 Ill. App. 3d 539 (2009) and does not address the standard of review relied on.",
 cited_authorities=["Ill. S. Ct. R. 341(h)(7)", "Wing v. Chicago Transit Authority, 2016 IL App (1st) 153517", "In re Baby Boy, 2025 IL App (4th) 241427", "Ferguson v. Georges, 389 Ill. App. 3d 543 (2010)", "People v. Mott, 389 Ill. App. 3d 539 (2009)"],
 summary="The Illinois Appellate Court affirms denial of Sanja Noble’s petition and addresses a hallucinated citation in her self-represented brief. The order says Noble cited Ferguson v. Georges, but the reporter citation corresponded to People v. Mott and did not support the standard of review.",
 incident={"conduct":"Self-represented appellant cited Ferguson v. Georges at a reporter location that actually contained People v. Mott and did not support her standard-of-review point.","outcome":"warning","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
 tracker_slug="noble-v-wmc-mortgage",
 text_sha256="c3072690fa525569ed483a2c275938f849c2c5c8c6a60586d013ae8b321e737e",
 source_url="https://www.damiencharlotin.com/documents/2999/Noble_v._WMC_Mortgage_Corp_USA_28_August_2026.pdf",
 fetched_at=fetched_at, verification="link-only", lead_source=["charlotin-cc0"],
 notes="Could not locate the official Illinois Courts PDF by quick CourtListener and citation searches; read the court-authored PDF from the Charlotin mirror."
)

add(
 decision_id="cod-2026-adams-v-matrix-providers",
 case_name="Adams v. Matrix Providers Inc.",
 court="United States District Court for the District of Colorado",
 court_code="cod", court_level="federal-district", state="CO", date_filed="2026-08-27",
 docket_number="1:23-cv-01996-CNS-KAS", document_type="order",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court denied post-judgment motions, admonished counsel over questionable citations, and sanctioned counsel $1,000 for rule violations.",
 ai_passage="In her response to the show cause order, Ms. Pearson represents that the nonexistent case, Ricks v. Starbucks, was included in Plaintiff’s briefing inadvertently. By way of explanation, Ms. Pearson offers that at the time briefing was due, she was handling a significant family emergency and required additional help from an unnamed “colleague” and her paralegal to assist in finalizing the briefing. ... However, Ms. Pearson’s response also notes that, with respect to the other legal citations in her briefing, “[o]f these thirty-six [cases cited in the response to Matrix’s summary judgment motion], Ricks is the only case that the Court and [Matrix] believe is fake and potentially AI-generated.” ... Whether these misstatements were the result of the use of an AI legal search, or simply poor and unexacting legal judgment, is unclear. Regardless, they are highly concerning to the Court nonetheless.",
 cited_authorities=["Ricks v. Starbucks", "Amarsingh v. Frontier Airlines, Inc., No. 24-1391, 2026 WL 352016 (10th Cir. Feb. 9, 2026)", "Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023)"],
 summary="The District of Colorado denies Adams’s post-judgment motions and addresses counsel’s response to a show-cause order over a nonexistent Ricks v. Starbucks citation and other inaccurate authorities. The court admonishes counsel about possible AI-assisted research errors and separately imposes a $1,000 sanction for rule violations.",
 incident={"conduct":"Counsel included a nonexistent Ricks v. Starbucks citation and numerous inaccurate citations; the court said possible AI use was unclear.","outcome":"fine","actor":"lawyer","monetary_penalty":1000,"currency":"USD","ai_tool":None},
 tracker_slug="adams-v-matrix-providers",
 courtlistener_url="https://www.courtlistener.com/docket/67675545/134/adams-v-matrix-providers-inc/",
 text_sha256="834fa7968af6d009faed54d4b5e9477044c2e4198191cb3c8c6fa4f6a8c07471",
 source_url="https://storage.courtlistener.com/recap/gov.uscourts.cod.226664/gov.uscourts.cod.226664.134.0.pdf",
 fetched_at=fetched_at, verification="fetched-and-read", lead_source=["charlotin-cc0","courtlistener-search"],
 notes="The $1,000 sanction in this order is tied to Rule 11(c)(1), Local Rule 83.1(e), and practice standards; the court also admonishes counsel about citation issues."
)

add(
 decision_id="pasuperct-2026-kiser-v-desimone-auto-group",
 case_name="Kiser v. DeSimone Auto Group",
 court="Superior Court of Pennsylvania",
 court_code=None, court_level="state-appellate", state="PA", date_filed="2026-08-27",
 docket_number="2428 EDA 2025", document_type="memorandum-opinion",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court affirmed the judgment and deemed one issue waived because it was underdeveloped and partly supported by unlocatable precedent.",
 ai_passage="As Burton does not address either Pa.R.E. 404(B)(2) or res gestae, and as Appellants do not provide any discussion of ”Com v. Reid,” this Court’s review of Appellants’ argument to this point is substantially impaired. Further, in light of this unlocatable precedent, “this Court is left to guess whether this counterfeit authority is the product of a chatbot, or if there is a more nefarious explanation for the misinformation.” Commonwealth v. Shie, 307 A.3d 668, 2023 WL 6878610, at *7 n.7 (Pa. Super. 2023)(unpublished); see also Sanders v. United States, 176 Fed.Cl. 163, 169 (Fed. Cl. 2025)(observing \"[i]t is no secret that generative AI programs are known to 'hallucinate' nonexistent cases, and with the advent of AI, courts have seen a rash of cases in which both counsel and pro se litigants have cited such fake, hallucinated cases in their briefs\" (internal citation omitted)).",
 cited_authorities=["Pa.R.E. 404(B)(2)", "Com v. Reid, 770 A.2d 771 (Pa. Super. 2001)", "Commonwealth v. Burton, 770 A.2d 771 (Pa. Super. 1999)", "Commonwealth v. Shie, 307 A.3d 668, 2023 WL 6878610 (Pa. Super. 2023)", "Sanders v. United States, 176 Fed. Cl. 163 (Fed. Cl. 2025)"],
 summary="The Superior Court of Pennsylvania affirms judgment against Paige and Ty Kiser and identifies an unlocatable Com v. Reid citation in counsel’s appellate brief. The memorandum treats the unsupported argument as waived and quotes prior authority warning that counterfeit citations may be chatbot products.",
 incident={"conduct":"Appellants’ counsel relied on unlocatable Com v. Reid authority while arguing evidentiary error, impairing appellate review.","outcome":"warning","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
 tracker_slug="kiser-v-desimone-auto-group",
 text_sha256="a5d2a1a822a905e52165eb63fb512f084cd6fb91f253aa1b23a7278e9cebc948",
 source_url="https://www.damiencharlotin.com/documents/2995/Kiser_P._v._DeSimone_Auto_Group_USA_27_AUgust_2026.pdf",
 fetched_at=fetched_at, verification="link-only", lead_source=["charlotin-cc0"],
 notes="Could not locate the official Pennsylvania appellate PDF by quick CourtListener search; read the court-authored PDF from the Charlotin mirror."
)

add(
 decision_id="flsd-2026-james-v-conley",
 case_name="James v. Conley",
 court="United States District Court for the Southern District of Florida",
 court_code="flsd", court_level="federal-district", state="FL", date_filed="2026-08-27",
 docket_number="1:23-cv-24467-KMM", document_type="report-and-recommendation",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The magistrate judge recommended denying Rule 11 sanctions on safe-harbor grounds but referring plaintiff's counsel for disciplinary review.",
 ai_passage="In his Response, Plaintiff concedes that the Keys in the Fifth Amended Complaint that are the subject of the Motion were based on unverified AI-generated research, and although Plaintiff does not state so explicitly, the Keys were AI hallucinations. See id. at 6-7. As explained below, the Court finds Plaintiff’s counsel’s use of and repeated reliance on unverified AI-generated research to be irresponsible and in dereliction of counsel’s responsibilities as officers of the Court. ... While the Court declines to award Defendant monetary sanctions for the procedural reason noted above, the Court cannot ignore that Plaintiff’s counsel admitted to filing the Fifth Amended Complaint without first verifying whether the Keys — documents discovered through unverified AI-generated research — indeed existed and continued their reliance on the Keys for months, despite being unable to confirm their content.",
 cited_authorities=["Fed. R. Civ. P. 11", "Versant Funding LLC v. Teras Breakbulk Ocean Navigation Enters., LLC, No. 17-CV-81140, 2025 WL 1440351 (S.D. Fla. May 20, 2025)", "R. Regulating Fla. Bar 4-1.1"],
 summary="The Southern District of Florida recommends denying Miami-Dade County’s Rule 11 motion against James on safe-harbor grounds but says counsel relied for months on unverified AI-generated IACP Training Keys. The recommendation calls the Keys AI hallucinations and recommends referral of four signing attorneys.",
 incident={"conduct":"Plaintiff’s counsel pleaded and relied on unverified AI-generated IACP Training Keys that could not be confirmed to exist.","outcome":"referral","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
 tracker_slug="james-v-conley",
 courtlistener_url="https://www.courtlistener.com/docket/68032771/261/james-v-conley/",
 text_sha256="57d6ef2fb1eba559dda36bceb89d466474acbeed4f2c06e492667d43f0f2f441",
 source_url="https://storage.courtlistener.com/recap/gov.uscourts.flsd.658251/gov.uscourts.flsd.658251.261.0.pdf",
 fetched_at=fetched_at, verification="fetched-and-read", lead_source=["charlotin-cc0","courtlistener-search"],
 notes=None
)

add(
 decision_id="txnd-2026-williams-v-dfw-airport-board",
 case_name="Williams v. Dallas-Fort Worth International Airport Board",
 court="United States District Court for the Northern District of Texas",
 court_code="txnd", court_level="federal-district", state="TX", date_filed="2026-08-27",
 docket_number="4:26-cv-00433-P", document_type="memorandum-opinion",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court granted dismissal of the Section 1983 claims with prejudice and dismissed state-law claims without prejudice.",
 ai_passage="This cannot be undertaken at too broad a level of generality, id., and it certainly cannot be established by citation to nonexistent cases. Here, Plaintiffs make a borderline sanctionable attempt to identify “clearly established” law from five cases. ECF No. 18. Three of these cases—Iko v. Shreve, 122 F.3d 707 (4th Cir. 1997), Yates v. Terry, 817 F.3d 877 (4th Cir. 2016), and Dawkins v. Fields 354 F.3d 392 (5th Cir. 2003)—are either non-existent or mistakenly out-of-circuit and, in any event, inapposite. With respect to Dawkins, this Court cannot even find a case purporting to “clearly establish” law on the matter and wastes its limited judicial resources in doing so. ... The Court cautions that use of generative artificial intelligence that results in repeated misrepresentations of law may qualify for sanctions under Fed. R. Civ. P. 11(b)–(c).",
 cited_authorities=["Joseph ex rel. Estate of Joseph v. Bartlett, 981 F.3d 319 (5th Cir. 2020)", "Iko v. Shreve, 122 F.3d 707 (4th Cir. 1997)", "Yates v. Terry, 817 F.3d 877 (4th Cir. 2016)", "Dawkins v. Fields, 354 F.3d 392 (5th Cir. 2003)", "Fed. R. Civ. P. 11(b)-(c)", "Fletcher v. Experian Info. Sols., Inc., 168 F.4th 231 (2026)"],
 summary="The Northern District of Texas dismisses Williams’s Section 1983 claims and warns that plaintiffs’ qualified-immunity briefing relied on nonexistent or inapposite cases. The court identifies Dawkins, Iko and Yates problems and cautions that generative-AI misrepresentations of law may trigger Rule 11 sanctions.",
 incident={"conduct":"Plaintiffs cited nonexistent or misidentified cases, including Dawkins, Iko and Yates, to oppose qualified immunity.","outcome":"warning","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
 tracker_slug="williams-v-dfw-airport-board",
 courtlistener_url="https://www.courtlistener.com/docket/73163191/20/williams-v-dallas-fort-worth-international-airport-board/",
 text_sha256="8d9efb852e55ea3c644f0a493f957a1cac8621bddf44ec9a967ee77b16e523c5",
 source_url="https://storage.courtlistener.com/recap/gov.uscourts.txnd.417872/gov.uscourts.txnd.417872.20.0.pdf",
 fetched_at=fetched_at, verification="fetched-and-read", lead_source=["charlotin-cc0","courtlistener-search"],
 notes=None
)

add(
 decision_id="nhd-2026-turgeon-v-fhlmc",
 case_name="Turgeon v. Federal Home Loan Mortgage Corporation",
 court="United States District Court for the District of New Hampshire",
 court_code="nhd", court_level="federal-district", state="NH", date_filed="2026-08-26",
 docket_number="1:25-cv-00510-SM-TSM", document_type="order",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The district court affirmed dismissal of Turgeon's Chapter 13 petition and upheld striking her objection.",
 ai_passage="The court then questioned Turgeon regarding her Objection to the Trustee’s motion to dismiss. Specifically, the court asked Turgeon about her use of “false, hallucinated case citations” within her brief. The bankruptcy court explained to Turgeon that the citations she referenced and relied upon in her objection were inaccurate and misleading. Accordingly, her objection to the motion to dismiss would be stricken. Turgeon protested that she had been trying to act in “good faith.” The court responded: “it’s not going well for you because items are not getting noticed, []proper forms are not getting used, and you’re misleading the Court. So I really strongly urge you to get an attorney in this case and to go that route. If you continue to proceed pro se, we’ll continue to monitor the case accordingly.”",
 cited_authorities=[],
 summary="The District of New Hampshire affirms bankruptcy dismissal and recounts that the bankruptcy court struck Noella Turgeon’s objection because it contained false, hallucinated case citations. The order rejects Turgeon’s due-process challenge, noting the bankruptcy court warned her about misleading filings and gave leave to amend.",
 incident={"conduct":"Self-represented debtor filed an objection containing false, hallucinated case citations that the bankruptcy court found inaccurate and misleading.","outcome":"other","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
 tracker_slug="turgeon-v-fhlmc",
 courtlistener_url="https://www.courtlistener.com/docket/72009448/18/turgeon-v-federal-home-loan-mortgage-corporation/",
 text_sha256="206ffd976c752adfbbea092c1a06c333bc8305d2992be78fbebb2957e3146012",
 source_url="https://storage.courtlistener.com/recap/gov.uscourts.nhd.66674/gov.uscourts.nhd.66674.18.0.pdf",
 fetched_at=fetched_at, verification="fetched-and-read", lead_source=["charlotin-cc0","courtlistener-search"],
 notes="District court order quotes and reviews the bankruptcy court's handling of the hallucinated citations."
)

add(
 decision_id="mied-2026-potterf-v-wessels",
 case_name="Potterf v. Wessels",
 court="United States District Court for the Eastern District of Michigan",
 court_code="mied", court_level="federal-district", state="MI", date_filed="2026-08-26",
 docket_number="1:26-cv-10860-MFL-PTM", document_type="order",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court overruled objections, adopted the report and recommendation, denied plaintiffs' motions, and warned about future sanctions.",
 ai_passage="The Potterfs are not entitled to relief on any of their objections because they failed to take reasonable steps to ensure that the legal citations in the objections were accurate. As the Potterfs acknowledged during the virtual hearing on August 20, 2026, they used artificial intelligence to prepare their objections. Perhaps for that reason, their objections attribute false quotations or non-existent legal principles to their cited cases. For example: • The Potterfs quoted the Supreme Court as saying in United States v. Sineneng-Smith, 140 S. Ct. 1575, 1579 (2020), that federal courts “do not as a rule initiate torts or explore legal pathways on their own, but rather sit as arbiters of legal issues presented and argued by the parties.” ... That quotation does not appear in the Sineneng-Smith case in any form. • The Potterfs argued that “the Sixth Circuit clarified in United States v. Abdi, 827 F.3d 533, 538 (6th Cir. 2016) ...” That case does not appear to exist.",
 cited_authorities=["United States v. Sineneng-Smith, 140 S. Ct. 1575 (2020)", "United States v. Abdi, 827 F.3d 533 (6th Cir. 2016)", "Van Houten v. City of Fort Worth, 827 F.3d 533 (5th Cir.)", "Hill v. Synder, 814 F.3d 408 (6th Cir. 2016)", "Ability Center of Greater Toledo v. City of Sandusky, 385 F.3d 901 (6th Cir. 2004)", "Tindall v. Wayne County Friend of the Court, 269 F.3d 533 (6th Cir. 2001)"],
 summary="The Eastern District of Michigan denies the Potterfs’ objections after they acknowledge using artificial intelligence to prepare them. The court identifies false quotations, nonexistent cases and mischaracterized authorities, declines to grant relief on Rule 11-violating objections, and warns that future false citations may bring sanctions.",
 incident={"conduct":"Self-represented plaintiffs used AI to prepare objections with false quotations, nonexistent United States v. Abdi and Hill v. Synder citations, and mischaracterized cases.","outcome":"warning","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":"artificial intelligence"},
 tracker_slug="potterf-v-wessels",
 text_sha256="0599e9ae4b6c041251373b29b4af3b2a8b92950f0f9166a7c22bb849734f5aea",
 source_url="https://www.damiencharlotin.com/documents/2952/Potterf_v._Wessels_USA_26_August_2026.pdf",
 fetched_at=fetched_at, verification="link-only", lead_source=["charlotin-cc0"],
 notes="CourtListener found the docket but not this document in the first displayed RECAP results; read the court-authored PDF from the Charlotin mirror."
)

add(
 decision_id="azctapp-2026-fairrow-v-easten",
 case_name="Fairrow v. Easten",
 court="Arizona Court of Appeals, Division Two",
 court_code=None, court_level="state-appellate", state="AZ", date_filed="2026-08-26",
 docket_number=None, document_type="memorandum-opinion",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court affirmed the fee award and declined to award appellate fees as a sanction.",
 ai_passage="One such authority is Napp v. Napp, which Easten cites for the proposition that an award must be supported by a record sufficient to permit meaningful review. But that case does not exist—at least not at the citation provided by Easten. We suspect he intended to cite Breitbart-Napp v. Napp, 216 Ariz. 74 (App. 2007). In that case we vacated the trial court’s fee award because of the stale nature of the financial information upon which it was based and the court’s apparent decision to make the award based upon which party prevailed on the merits, an improper basis under § 25-324. Breitbart-Napp, 216 Ariz. 74, ¶ 39. Neither of those considerations apply here. Appels-Meehan v. Appels, 167 Ariz. 182 (App. 1991), upon which Easten also relies, did not involve a review of a trial court’s award of attorney fees.",
 cited_authorities=["Napp v. Napp", "Breitbart-Napp v. Napp, 216 Ariz. 74 (App. 2007)", "A.R.S. § 25-324", "Appels-Meehan v. Appels, 167 Ariz. 182 (App. 1991)"],
 summary="The Arizona Court of Appeals affirms a family-law fee award and notes that self-represented appellant Brently Easten relied on Napp v. Napp, a case the court says does not exist at the cited location. The court suspects Breitbart-Napp was intended and declines appellate-fee sanctions.",
 incident={"conduct":"Self-represented appellant cited Napp v. Napp for fee-award review, but the court found no such case at the provided citation.","outcome":"other","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
 text_sha256="abd52f90a03c2882226ab4fc1d6fdcc4b2d37cbbceea74c89c474382049de960",
 source_url="https://www.damiencharlotin.com/documents/2998/ALIYAH_FAIRROW_v._BRENTLY_EASTEN_USA_26_August_2026.pdf",
 fetched_at=fetched_at, verification="link-only", lead_source=["charlotin-cc0"],
 notes="CourtListener opinion search did not locate this Arizona memorandum decision; read the court-authored PDF from the Charlotin mirror. The decision does not itself name an AI tool."
)

add(
 decision_id="mdd-2026-johnson-v-nationstar",
 case_name="Johnson v. Nationstar Mortgage LLC",
 court="United States District Court for the District of Maryland",
 court_code="mdd", court_level="federal-district", state="MD", date_filed="2026-08-26",
 docket_number="1:25-cv-00855-JRR", document_type="memorandum-opinion",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court granted defendants' motions to dismiss and declined further action over the latest hallucinated citation.",
 ai_passage="Notwithstanding the foregoing admonition, it appears Plaintiff has once again cited a “hallucinated” case derived perhaps from use of a generative artificial intelligence (“AI”) tool (e.g., ChatGPT, Gemini, etc.). Specifically, Plaintiff cites to “Cooke v. Carrington Mortg. Servs., No. 22-1425 (4th Cir. 2023),” see ECF No. 57 at p. 3. Plaintiff contends this case stands for the proposition that “servicer-imposed charges tied to improper insurance placement constitute a concrete injury.” ... Based on the court’s review, this case does not exist. The court has checked the Fourth Circuit case number—22-1425, and Westlaw citation—2023 WL 3010355—offered by Plaintiff to identify this case; neither directs the court to the referenced opinion. ... While this court has already cautioned Plaintiff that continued citation to hallucinated authorities or the like risks issuance of an order to show cause why he should not face sanctions under Rule 11, the court declines to take further action in the instant matter where Plaintiff’s case will be dismissed in full.",
 cited_authorities=["Cooke v. Carrington Mortg. Servs., No. 22-1425 (4th Cir. 2023)", "Mezu v. Mezu, 267 Md. App. 354 (2025)", "Noland v. Land of the Free, L.P., 336 Cal. Rptr. 3d 897 (Cal. App. 2025)", "Fed. R. Civ. P. 11"],
 summary="The District of Maryland dismisses Johnson’s mortgage-related claims and flags another hallucinated citation from the self-represented plaintiff. The court says Cooke v. Carrington Mortgage Services, as cited to the Fourth Circuit and Westlaw, does not exist, but declines further Rule 11 action because the case is dismissed.",
 incident={"conduct":"Self-represented plaintiff cited nonexistent Cooke v. Carrington Mortgage Services Fourth Circuit and Westlaw authorities after a prior Rule 11 warning.","outcome":"warning","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
 tracker_slug="johnson-v-nationstar",
 text_sha256="c2bc86219428dce58bd3ee99f2f467088f0e26284a232b2c507939335949f2a6",
 source_url="https://www.damiencharlotin.com/documents/2949/Johnson_v._Nationstar_Mortgage_LLC_USA_26_August_2026.pdf",
 fetched_at=fetched_at, verification="link-only", lead_source=["charlotin-cc0"],
 notes="CourtListener search found the docket but did not surface this PDF in the displayed RECAP result; read the court-authored PDF from the Charlotin mirror."
)

add(
 decision_id="ilnd-2026-shelbert-v-baxter-international",
 case_name="Shelbert v. Baxter International, Inc.",
 court="United States District Court for the Northern District of Illinois",
 court_code="ilnd", court_level="federal-district", state="IL", date_filed="2026-08-26",
 docket_number="1:26-cv-06266", document_type="memorandum-opinion",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court granted in part and denied in part a motion to strike affirmative defenses and admonished plaintiff's counsel.",
 ai_passage="The presumable conclusion was that Tyler had AI review Baxter’s Answer and had it generate his Motion to Strike. While there is not yet a proscription prohibiting this conduct, there is a proscription of filing a brief with citations to cases that do not stand for the asserted proposition. Perez-Castillo v. Blanche, 177 F.4th 837, 848 (7th Cir. 2026). Indeed, “[u]nder this circuit’s standards for professional conduct, lawyers promise that they will not knowingly misrepresent, mischaracterize, misquote, or miscite facts or authorities in any oral or written communication to the court.” ... The Seventh Circuit opinion in Instituto supports neither of these propositions. See Instituto, 858 F.2d at 1265-72. Indeed, the words “affirmative defense” are not even in the opinion. The Court admonishes Tyler for repeatedly citing to a Seventh Circuit decision for a false proposition. AI generated content routinely contains errors—including those that may be difficult to readily ascertain.",
 cited_authorities=["Perez-Castillo v. Blanche, 177 F.4th 837 (7th Cir. 2026)", "Instituto Nacional de Comercializacion Agricola (Indeca) v. Continental Illinois National Bank & Trust Co., 858 F.2d 1264 (7th Cir. 1988)", "Instituto Nacional De Comercializacion Agricola (Indeca) v. Cont’l Illinois Nat. Bank & Tr. Co., 576 F. Supp. 985 (N.D. Ill. 1983)"],
 summary="The Northern District of Illinois resolves Shelbert’s motion to strike Baxter’s defenses and admonishes plaintiff’s counsel for citing Instituto for propositions the Seventh Circuit opinion does not contain. The court says the motion appeared AI-generated and warns both parties against false or hallucinated citations.",
 incident={"conduct":"Plaintiff’s counsel repeatedly cited Instituto for affirmative-defense propositions not found in the Seventh Circuit opinion; the court suspected AI-assisted drafting.","outcome":"warning","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
 tracker_slug="shelbert-v-baxter-international",
 text_sha256="efa875b46f8cbf38ba11f72a0a7940462964769019e821a14e04ab675abcdcc4",
 source_url="https://www.damiencharlotin.com/documents/2951/Shelbert_v._Baxter_International_USA_26_August_2026.pdf",
 fetched_at=fetched_at, verification="link-only", lead_source=["charlotin-cc0"],
 notes="CourtListener search found the docket but not this memorandum opinion PDF in available RECAP documents; read the court-authored PDF from the Charlotin mirror."
)

add(
 decision_id="njd-2026-kurelko-v-ballard",
 case_name="Kurelko v. Ballard",
 court="United States District Court for the District of New Jersey",
 court_code="njd", court_level="federal-district", state="NJ", date_filed="2026-08-25",
 docket_number="3:25-cv-11917-ZNQ-JBD", document_type="order",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court denied Kurelko's motions to disqualify the New Jersey Office of the Attorney General.",
 ai_passage="Plaintiff’s first motion to disqualify contains several inaccurate or non-existent case citations and quotations. See [Dkt. 15.] “‘[I]t is improper and unacceptable for litigants—including pro se litigants—to submit ‘non-existent judicial opinions with fake quotes and citations.’” Fagan v. Barnhiser, Civ. No. 24-06012 (CCC), 2025 WL 2654994, at *2 (D.N.J. Sept. 17, 2025) (quoting Anonymous v. New York City Dep’t of Educ., Civ. No. 24-4232, 2024 WL 3460049, at *7 (S.D.N.Y. July 18, 2024) (further citations omitted)). “While some Courts have opted to sanction pro se litigants for this conduct, others have chosen to warn, rather than sanction, in these situations.” Id. (citation omitted). At this time, the Court will not impose sanctions. But plaintiff is now on notice: The Court “admonishes [p]laintiff for his improper conduct and warns that he will be subject to sanctions, including monetary penalties, should he [engage in similar conduct] again in the future.” Id.",
 cited_authorities=["Fagan v. Barnhiser, Civ. No. 24-06012 (CCC), 2025 WL 2654994 (D.N.J. Sept. 17, 2025)", "Anonymous v. New York City Dep’t of Educ., Civ. No. 24-4232, 2024 WL 3460049 (S.D.N.Y. July 18, 2024)"],
 summary="The District of New Jersey denies Kurelko’s motions to disqualify state counsel and notes his first motion contained inaccurate or nonexistent case citations and quotations. The court declines sanctions at that time, admonishes the self-represented plaintiff, and warns that similar conduct may bring monetary penalties.",
 incident={"conduct":"Self-represented plaintiff filed a disqualification motion with inaccurate or nonexistent case citations and quotations.","outcome":"warning","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
 text_sha256="9fb7fda497717436e439f18e38db5be4da8b14772de1c749116e5c776e5cfd73",
 source_url="https://www.damiencharlotin.com/documents/2944/KURELKO_v._BALLARD_JR._USA_25_August_2026.pdf",
 fetched_at=fetched_at, verification="link-only", lead_source=["charlotin-cc0"],
 notes="CourtListener returned a 429 during this lead's search; after waiting, used the Charlotin mirror. The order does not name an AI tool."
)

add(
 decision_id="mowd-2026-anddone-v-gaines",
 case_name="AndDone, LLC v. Gaines",
 court="United States District Court for the Western District of Missouri",
 court_code="mowd", court_level="federal-district", state="MO", date_filed="2026-08-25",
 docket_number="4:25-cv-00346-RK", document_type="order",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 disposition="The court granted Rule 37 fees and default judgment against Gaines, and denied alternative default-judgment motions as moot.",
 ai_passage="On November 21, 2025, AndDone filed a motion requesting an order that Gaines show cause why she should not be sanctioned for violations of Federal Rule of Civil Procedure 11 for misrepresentations to the Initial Court including citations to nonexistent cases and quotations contained in a November 18 filing, (Doc. 53). (Doc. 57.) ... The Initial Court also ordered Gaines to show cause why she should not be sanctioned for the Rule 11 violations identified in AndDone’s motion for order to show cause by December 12, 2025. (Doc. 59.) Gaines did not provide further written discovery responses as ordered, she did not appear for her deposition, and she did not respond to the Initial Court’s show cause order.",
 cited_authorities=["Fed. R. Civ. P. 11", "Fed. R. Civ. P. 37"],
 summary="The Western District of Missouri enters default judgment against Shante Gaines and recounts an earlier Rule 11 show-cause order over citations to nonexistent cases and quotations in a November 2025 filing. The court notes Gaines did not respond to the show-cause order or comply with discovery obligations.",
 incident={"conduct":"Self-represented defendant filed a November 2025 submission with misrepresentations, citations to nonexistent cases, and quotations, then did not answer a Rule 11 show-cause order.","outcome":"pending","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
 courtlistener_url="https://www.courtlistener.com/docket/70418866/84/anddone-llc-v-gaines/",
 text_sha256="4fb5a625728427da9b8a0332b00b1738890794dfa8c7d3001433e6dde719f276",
 source_url="https://storage.courtlistener.com/recap/gov.uscourts.mowd.183519/gov.uscourts.mowd.183519.84.0.pdf",
 fetched_at=fetched_at, verification="fetched-and-read", lead_source=["charlotin-cc0","courtlistener-search"],
 notes="This order recounts a prior show-cause order rather than deciding Rule 11 sanctions."
)

add(
 decision_id="azd-2026-ruiz-v-magellan-financial",
 case_name="Ruiz v. Magellan Financial & Insurance Services",
 court="United States District Court for the District of Arizona",
 court_code="azd", court_level="federal-district", state="AZ", date_filed="2026-08-24",
 docket_number="2:23-cv-02090-DWL", document_type="order",
 topics=["fabricated-citations"], primary_topic="fabricated-citations", court_used_ai=False,
 ai_tool_named="ChatGPT",
 disposition="The court issued a formal public reprimand to plaintiff's counsel and required her to report the discipline where required.",
 ai_passage="The first issue to be addressed is whether Ms. Tate’s conduct violated any procedural or ethical rules. It did. Ms. Tate acknowledges that she filed three different briefs in this action that contained fake AI-generated quotations and filed a fourth brief that contained an inaccurate AI-generated case summary. ... In the course of preparing this Motion, Ms. Tate utilized ChatGPT to prepare the draft brief. ChatGPT cited the Ansell v. Green Acres Contracting Co., 347 F.3d 515 (3d Cir. 2003) case to support the proposition that evidence of favorable treatment of the plaintiff or others does not preclude discrimination and may be excluded as irrelevant or misleading. ... Ms. Tate also utilized ChatGPT to assist with the Brief on Impeachment. ... While Ms. Tate confirmed the cases stood for the proposition for which she understood them to when she first prompted ChatGPT to include them in the draft brief, Ms. Tate mistakenly did not correct the misquotations from the Antonakeas or Osazuwa cases.",
 cited_authorities=["Ansell v. Green Acres Contracting Co., 347 F.3d 515 (3d Cir. 2003)", "United States v. Antonakeas, 255 F.3d 714 (9th Cir. 2001)", "United States v. Osazuwa, 564 F.3d 1169 (9th Cir. 2009)", "Fed. R. Civ. P. 11(b)(2)"],
 summary="The District of Arizona publicly reprimands Elizabeth Tate after finding she filed three briefs with fake AI-generated quotations and a fourth with an inaccurate AI-generated case summary. The order says she used ChatGPT, violated Rule 11 and ethics duties, and must report the discipline where required.",
 incident={"conduct":"Counsel filed three briefs with fake AI-generated quotations and a fourth with an inaccurate AI-generated summary after using ChatGPT.","outcome":"sanctions","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":"ChatGPT"},
 tracker_slug="ruiz-v-magellan-financial",
 courtlistener_url="https://www.courtlistener.com/docket/67863214/179/ruiz-v-magellan-financial-insurance-services/",
 text_sha256="c65f2c3bfbca35bfec9dc6c276031409068ab7a26914fcf194a39e5dbbf584ab",
 source_url="https://storage.courtlistener.com/recap/gov.uscourts.azd.1348340/gov.uscourts.azd.1348340.179.0.pdf",
 fetched_at=fetched_at, verification="fetched-and-read", lead_source=["charlotin-cc0","courtlistener-search"],
 notes=None
)

add(
 decision_id="utd-2026-ferm-v-agritech-properties",
 case_name="Ferm v. Agritech Properties",
 court="United States District Court for the District of Utah",
 court_code="utd", court_level="federal-district", state="UT", date_filed="2026-08-25",
 docket_number="4:26-cv-00029-DN-PK", document_type="order",
 topics=["pro-se-ai-use"], primary_topic="pro-se-ai-use", court_used_ai=False,
 disposition="The court adopted the report and recommendation, dismissed for lack of personal jurisdiction, and denied remaining motions as moot.",
 ai_passage="Objection also shows signs of drafting by artificial intelligence. Federal courts often strike briefs that do not comply with local rules, which the Tenth Circuit has upheld. Instead, this order confine review to Mr. Ferm’s one meritorious objection. ... The remainder of Mr. Ferm’s Objection is “too long, too verbose, too vague, and too repetitive” to be considered specific enough for de novo review. The last 37 pages of Mr. Ferm’s objection devolves into a series of bullets points that are a clear example of “A.I. Slop.” Mr. Ferm “is cautioned against the possible use of artificial intelligence to draft memorandums.” Christoffersen v. Nucor Corp., No. 4:25-CV-00118-DN-PK, 2026 WL 1623190, at *2 n.15 (D. Utah June 5, 2026).",
 cited_authorities=["Christoffersen v. Nucor Corp., No. 4:25-CV-00118-DN-PK, 2026 WL 1623190 (D. Utah June 5, 2026)", "Carey v. Breakell, No. 4:25-CV-00108-AMA-PK, 2026 WL 2199063 (D. Utah July 30, 2026)", "Hack v. Preston, No. 4:25-CV-00096-DN, 2026 WL 2279536 (D. Utah Aug. 7, 2026)"],
 summary="The District of Utah adopts a recommendation dismissing Ferm’s case and addresses signs that his objection was drafted with artificial intelligence. The court confines review to one specific objection, describes the remaining pages as AI slop, and cautions the self-represented plaintiff against possible AI-drafted memoranda.",
 incident=None,
 text_sha256="7e56e65016a68775039c363082c1301db780a77d1f33bcad24ac5f72fee53138",
 source_url="https://www.damiencharlotin.com/documents/2956/Ferm_v._Agritech_USA_25_August_2026.pdf",
 fetched_at=fetched_at, verification="link-only", lead_source=["charlotin-cc0"],
 notes="Included as pro-se AI use rather than fabricated-citations because this order describes AI slop and possible AI drafting, not a specific fabricated authority. The lead date is 2026-08-24; the PDF was filed 2026-08-25."
)

with open('work/agents/decisions-t1-s1.jsonl','w',encoding='utf-8') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False, separators=(',',':'))+'\n')
print(len(rows))
