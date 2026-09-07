import json

fetched_at = "2026-09-07T13:15:21.976-07:00"

source = "https://www.damiencharlotin.com"

rows = []


def add(**kw):
    base = dict(
        citation=None,
        docket_number=None,
        court_code=None,
        state=None,
        ai_tool_named=None,
        incident=None,
        tracker_slug=None,
        courtlistener_url=None,
        text_sha256=None,
        archive_url=None,
        notes=None,
        lead_source=["charlotin-cc0"],
        fetched_at=fetched_at,
        verification="link-only",
    )
    base.update(kw)
    rows.append(base)


secondary_note = "Official source not obtained after CourtListener throttling; read the court-authored document from the Charlotin mirror and marked link-only."


add(
    decision_id="cand-2026-full-standard-properties-v-sj-6070",
    case_name="Full Standard Properties, LLC v. SJ 6070, LLC",
    court="United States District Court for the Northern District of California",
    court_code="cand",
    court_level="federal-district",
    state="CA",
    date_filed="2026-08-20",
    docket_number="25-cv-09451-BLF",
    document_type="order",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court discharged an order to show cause after plaintiff's counsel reimbursed $14,500 in fees tied to nonexistent cases.",
    ai_passage="The Court also ordered Plaintiff’s counsel to show cause why he should not be sanctioned in an amount sufficient to reimburse Defendant for expenses it incurred in addressing nonexistent cases cited by Plaintiff in opposition to the first attorneys’ fees motion. See Order to Show Cause, ECF 30. The parties have resolved that issue informally, and Plaintiff’s counsel has reimbursed Defendant for attorneys’ fees in the amount of $14,500. Accordingly, the Court will discharge the order to show cause.",
    cited_authorities=["Order to Show Cause, ECF 30"],
    summary="The Northern District of California grants in part a renewed fee motion and discharges a sanctions order. The order records that plaintiff’s counsel reimbursed SJ 6070 $14,500 for expenses incurred addressing nonexistent cases cited in opposition to an earlier attorneys’ fees motion.",
    incident={
        "conduct": "Plaintiff’s counsel cited nonexistent cases in opposition to the first attorneys’ fees motion, causing defendant to incur response expenses.",
        "outcome": "costs-order",
        "actor": "lawyer",
        "monetary_penalty": 14500,
        "currency": "USD",
        "ai_tool": None,
    },
    tracker_slug="full-standard-properties-v-sj-6070",
    text_sha256="2ef1b3bde965743df62758bd0f5f9b0b396c9df4978d62d4d21c70b6561b2dc4",
    source_url=source + "/documents/2941/Full_Standard_Properties_USA_20_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="calsuperct-2026-perez-v-schaal",
    case_name="Perez v. Schaal",
    court="Superior Court of California, County of Sacramento",
    court_level="state-trial",
    state="CA",
    date_filed="2026-08-21",
    docket_number="25CV019484",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court ruled on the demurrer and warned the self-represented plaintiff to verify all citations and quotations.",
    ai_passage="Plaintiff quotes Adorh Farms, Co. v. Love (1967) 255 Cal.App.2d 366 at p. 371: “The filing of an answer … effected a waiver of the right to demur.” (Opp., at p. 8: 19–21.) This is at best an incomplete statement of law. “A party objecting to a complaint or cross-complaint may demur and answer at the same time.” (Code Civ. Proc., § 430.30, subd. (c); see § 472a, subd. (a) [“A demurrer is not waived by an answer filed at the same time.”].) More importantly, although the Adorh Farms opinion exists,[3] it does not contain the quoted language. Nor can the court find the quoted language in any other case reported in California or elsewhere. This quotation may be the result of irresponsible use of generative artificial intelligence (“AI”). ... The Court declines to begin the process of imposing sanctions at this time but strongly cautions Plaintiff to take better care in making only good-faith, well-researched, legally sound arguments in future. All citations and quotations submitted to the Court must be verified. Future submissions of fabricated authority may result in sanctions.",
    cited_authorities=["Adorh Farms, Co. v. Love, 255 Cal.App.2d 366 (1967)", "Code Civ. Proc. § 430.30", "Code Civ. Proc. § 472a", "Noland v. Land of the Free, L.P., 114 Cal.App.5th 426 (2025)", "Hopkins & Carley v. Gens, 200 Cal.App.4th 1401 (2011)"],
    summary="The Sacramento Superior Court rules on a demurrer and addresses Joseph Perez’s unsupported quotation from Adorh Farms. The court says the quotation does not appear in that opinion or any reported case, flags possible generative AI use, declines sanctions, and warns future fabricated authority may be sanctioned.",
    incident={
        "conduct": "Self-represented plaintiff attributed a quotation about waiver of demurrer to Adorh Farms, but the court could not find it in that or any reported case.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="2da85cb60cab4db3fe5ff8328cf32bc9d84485775b01d1651f3eb11640e10d1c",
    source_url=source + "/documents/3004/Perez_v._Schaal_USA_21_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="ded-2026-disruptive-resources-v-ballistic-barrier",
    case_name="Disruptive Resources, LLC v. Ballistic Barrier Products Inc.",
    court="United States District Court for the District of Delaware",
    court_code="ded",
    court_level="federal-district",
    state="DE",
    date_filed="2026-08-20",
    docket_number="1:24-cv-00321-JCG",
    document_type="opinion",
    topics=["competence-fees"],
    primary_topic="competence-fees",
    court_used_ai=False,
    ai_tool_named="Strongsuit",
    disposition="The court declined Rule 11 sanctions but warned counsel that future AI mistakes in the case may result in sanctions.",
    ai_passage="After Plaintiff’s counsel disclosed to the Court that the previously filed Joint Claim Construction Brief (“Joint Brief”) (D.I. 105) featured multiple errors due to his use of generative artificial intelligence (“AI”), the Court ordered counsel to show cause in writing as to why the Court should not impose sanctions for counsel’s conduct pursuant to Federal Rule of Civil Procedure 11(b),(c). ... Counsel stated that he used the AI system “Strongsuit” to generate an initial outline of Plaintiff’s reply brief and to pull statements from a deposition that supported Plaintiff’s position on claim construction. ... Plaintiff sought to strike the problematic section of its reply brief, causing Defendants to also strike their subsequent briefing that responded to the inaccurate AI-generated arguments put forth by Plaintiff. ... The Court expects that these events and this Opinion shall serve as a cautionary warning and learning experience for counsel moving forward. The Court warns counsel that any future incidents involving AI mistakes in this case may result in sanctions. Upon consideration of the circumstances as described by counsel, and his appreciation for the gravity of filing erroneous legal arguments drafted by generative AI without proper review, the Court declines to sanction counsel for his conduct.",
    cited_authorities=["Fed. R. Civ. P. 11", "McCarthy v. United States Drug Enforcement Administration, 171 F.4th 245 (3d Cir. 2026)", "Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023)"],
    summary="The District of Delaware addresses plaintiff’s counsel’s disclosure that StrongSuit generated erroneous claim-construction briefing. The court notes counsel’s candor, withdrawn sections, and defense burden, declines Rule 11 sanctions, and warns that future AI mistakes in the case may result in sanctions.",
    tracker_slug="disruptive-resources-v-ballistic-barrier",
    text_sha256="cd04918cf72a72d1424adc4fda9e708d1ff69e0c9e30039fbcfa2c5822c88cf2",
    source_url=source + "/documents/2925/Disruptive_Resources_LLC_v._Ballistic_Barrier_Products_USA_20_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="cacd-2026-dotson-v-bob-evans-farms",
    case_name="Dotson v. Bob Evans Farms, LLC",
    court="United States District Court for the Central District of California",
    court_code="cacd",
    court_level="federal-district",
    state="CA",
    date_filed="2026-08-20",
    docket_number="2:25-cv-11993-MWC-DSR",
    document_type="order",
    topics=["fabricated-citations"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court denied reconsideration and ordered plaintiff's counsel to show cause about monetary sanctions and a state bar referral.",
    ai_passage="At three different points in his Application, Plaintiff attributes quoted language to Mission Power, 883 F. Supp. at 492, which appears nowhere in the body of the cited case. See Appl. at 7:10–7:15, 10:5–10:8, 10:17–10:22. The discrepancies between the quoted language and the language of the cited case are so significant as to abrogate any assumption that the misattributions are the result of typographical error. Plaintiff’s repeated inclusion of quotations misattributed to Mission Power, which are present in the language of an entirely different case, 1 “bear the hallmarks of hallucinated cases created by artificial intelligence (‘AI’) tools.” Cummins v. Becerra, No. 1:25-CV-01853-DC-AC, 2026 WL 373336, at *1 (E.D. Cal. Feb. 10, 2026) ... Accordingly, the Court SETS an ORDER TO SHOW CAUSE Re: Monetary Sanctions and State Bar Referral of Todd M. Friedman for breach of the duty of candor to the Court.",
    cited_authorities=["Mission Power Engineering Co. v. Continental Casualty Co., 883 F. Supp. 488 (C.D. Cal. 1995)", "Horne v. Wells Fargo Bank, N.A., 969 F. Supp. 2d 1203 (C.D. Cal. 2013)", "Cummins v. Becerra, 2026 WL 373336 (E.D. Cal. Feb. 10, 2026)", "Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023)"],
    summary="The Central District of California denies Michael Dotson’s reconsideration application and identifies three quotations misattributed to Mission Power. The court says the language appears in Horne instead, describes the errors as AI-hallucination hallmarks, and orders counsel to show cause about sanctions and bar referral.",
    incident={
        "conduct": "Plaintiff’s counsel repeatedly attributed quoted language to Mission Power that the court found in a different case, Horne v. Wells Fargo.",
        "outcome": "pending",
        "actor": "lawyer",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="64e72447510a303d3b5bee6f1b6468005d57689a6306736cced012b53e48c94b",
    source_url=source + "/documents/2939/Dotson_v._Evans_USa_20_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="cacd-2026-kasengela-v-kaiser-foundation",
    case_name="Kasengela v. Kaiser Foundation Hospitals",
    court="United States District Court for the Central District of California",
    court_code="cacd",
    court_level="federal-district",
    state="CA",
    date_filed="2026-08-20",
    citation="2026 WL 2447454",
    docket_number="2:26-cv-01666-WLH-CTS",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court remanded the action and admonished the self-represented plaintiff over non-existent quotations in briefing.",
    ai_passage="Lastly, the Court underscores its Standing Order to remind Plaintiff that the inclusion of non-existent quotations in Plaintiff's briefing submitted to this Court is unacceptable. (See Opp'n at 3-4; Order Re Amended Civil Case Standing Order, Dkt. No. 65 at 18-20 (“caution[ing] that unqualified reliance on AI-generated content can result in filings that rely on misrepresentations and hallucinated, nonexistent caselaw”)). While the Court understands that Plaintiff is proceeding pro se, the Court does not condone the submission of misstated case law from any litigant and is concerned by Plaintiff's doubling-down in her Reply where she claims that Kaiser pointed out her incorrect quotations in bad faith to improperly attack her, rather than correcting her citations. ... Quoting paraphrased language generated from artificial intelligence tools, published on websites explaining case law (e.g., law.cornell.edu), or from personal manipulation without appropriate signals (e.g., without bracketing, ellipses, etc.) as if those quotations came directly from the cases themselves is squarely prohibited. If Plaintiff were a lawyer, the Court would be imposing significant sanctions for this conduct.",
    cited_authorities=["Order Re Amended Civil Case Standing Order, Dkt. No. 65", "Chapman v. Horace Mann Property & Casualty Insurance Co., 2025 WL 3724904 (C.D. Cal. Aug. 14, 2025)"],
    summary="The Central District of California grants Cecile Kasengela’s remand motion while addressing non-existent quotations in her self-represented briefing. The court reiterates its standing order on AI-generated hallucinated caselaw, rejects her accusation against Kaiser, and says a lawyer would face significant sanctions.",
    incident={
        "conduct": "Self-represented plaintiff submitted non-existent quotations and misstated case law, then accused Kaiser of bad faith instead of correcting the citations.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="5bfa5f1b3f49058e381742f01536e776d944842a7259a4e85401c8fc9c680f2f",
    source_url=source + "/documents/2923/CECILE_KASENGELA_v_KAISER_FOUNDATION_HOSPITALS_et_al_USA_20_August_2026.pdf",
    notes="Official source not obtained after CourtListener throttling; read the court-authored text from the Charlotin mirror. The mirror text appears to include Westlaw slip-copy formatting.",
)


add(
    decision_id="caed-2026-lohbeck-v-amazon",
    case_name="Lohbeck v. Amazon.com Services, LLC",
    court="United States District Court for the Eastern District of California",
    court_code="caed",
    court_level="federal-district",
    state="CA",
    date_filed="2026-08-21",
    docket_number="2:26-cv-02007-DC-CSK",
    document_type="report-and-recommendation",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The magistrate judge recommended dismissal and warned the self-represented plaintiff about misquotations suggesting AI use.",
    ai_passage="Defendant argues Plaintiff has violated Federal Rule of Procedure 11 by misusing generative artificial intelligence (“generative AI”). See Def. Sanctions Opp. at 6-7 (ECF No. 21). Specifically, Defendant argues Plaintiff’s writing contains generative AI hallmarks and that for each case Plaintiff cites with a parenthetical, the quoted language is absent from the cited opinion. ... Defendant is correct that in Plaintiff’s motion for sanctions, Plaintiff attributes quotations to two different cases, but the language Plaintiff quoted does not actually appear in either case. See Def. Sanctions Opp. at 6-7; Pl. Sanctions Mot. at 1. The Court has concerns that Plaintiff’s submissions to the Court have misquotations of cases, which suggest an irresponsible use of generative AI. “Such misquotations, miscitations, and misrepresentations often indicate the presence of artificial intelligence-generated hallucinations.” Doe 1 v. Lai, 2026 WL 1004947, at *1 (C.D. Cal. Feb. 17, 2026). ... Though the Court is concerned by Plaintiff’s misquotations in his sanctions motion that indicate the irresponsible use of generative AI, given Plaintiff’s pro se status, the Court declines at this time Defendant’s invitation to impose sanctions.",
    cited_authorities=["Fed. R. Civ. P. 11", "Doe 1 v. Lai, 2026 WL 1004947 (C.D. Cal. Feb. 17, 2026)", "Lohbeck v. CSL Plasma, Inc., No. 2:26-cv-01493-DJC-CSK"],
    summary="The Eastern District of California recommends dismissal of Stephen Lohbeck’s claims and considers Amazon’s Rule 11 argument. The magistrate judge finds two quotations in Lohbeck’s sanctions motion do not appear in the cited cases, declines sanctions because he is self-represented, and warns that future false authority may be sanctionable.",
    incident={
        "conduct": "Self-represented plaintiff’s sanctions motion attributed quotations to two cases, but the quoted language did not appear in either opinion.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="14902aaa12616361b7133377cf905bce9578bb2db40f3d8e3d31e8700d2dcdeb",
    source_url=source + "/documents/2937/Lohbeck_v._Amazon_USA_21_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="pasuperct-2026-kaspryak-v-stadarskyy",
    case_name="Kaspryak v. Stadarskyy",
    court="Superior Court of Pennsylvania",
    court_level="state-appellate",
    state="PA",
    date_filed="2026-08-19",
    citation="2026 PA Super 185",
    docket_number="2781 EDA 2025",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed dismissal of the partition action and held the appellant waived claims through unsupported and fabricated authority.",
    ai_passage="Specifically, Appellant cites to “General Fin. Co. v. Archetto, 167 A.2d 306 (Pa. Super. 1961)” and “Lowrey v. Eastaff, 860 A.2d 533 (Pa. Super. 2004).” See id. (some formatting altered). These citations are so nonsensical and disconnected from Appellant’s claims that we conclude that they are hallucinated citations. To the extent that Appellant has employed generative artificial intelligence (“generative AI” or “GAI”) tools to draft her brief, as indicated by her repeated misrepresentations of the meaning of valid statutes and precedential opinions as well as her reliance on hallucinated authority, we note that the use of GAI to draft legal filings (including by pro se litigants), without verification of the accuracy of the content so produced, may lead to misstatements and/or misrepresentations of legal authority. ... We note that the Atlantic Reporter citation “167 A.2d 306” leads to a Pennsylvania Supreme Court opinion, Slott v. Plastic Fabricators, Inc., 167 A.2d 306 (Pa. 1961), not to a Pennsylvania Superior Court opinion captioned “General Fin. Co. v. Archetto” as Appellant states. ... In fact, “Lowrey v. Eastaff” appears to be an entirely fabricated caption, coupled with a hallucinated citation.",
    cited_authorities=["General Fin. Co. v. Archetto, 167 A.2d 306 (Pa. Super. 1961)", "Lowrey v. Eastaff, 860 A.2d 533 (Pa. Super. 2004)", "Saber Healthcare Group, LLC v. Duchene, 350 A.3d 966 (Pa. Super. 2025)", "Slott v. Plastic Fabricators, Inc., 167 A.2d 306 (Pa. 1961)", "General Finance Corp. v. Archetto, 176 A.2d 73 (R.I. 1961)", "Commonwealth v. duPont, 860 A.2d 525 (Pa. Super. 2004)"],
    summary="The Superior Court of Pennsylvania affirms dismissal of Zoryana Kaspryak’s partition action. The court finds that two citations in her self-represented reply brief are hallucinated, explains that the reporter citations lead to different cases, and concludes her claims are waived for unsupported and fabricated authority.",
    incident={
        "conduct": "Self-represented appellant cited General Fin. Co. v. Archetto and Lowrey v. Eastaff with reporter citations that led to different cases or a fabricated caption.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="85a77d5ed3cb9a5bc69d64c171251ec8b596312c677ba1ae35da792c4fe19b05",
    source_url=source + "/documents/2913/Kaspryak_Z._v._Stadarskyy_USA_19_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="nvd-2026-kelly-v-finra",
    case_name="Kelly v. Financial Industry Regulatory Authority",
    court="United States District Court for the District of Nevada",
    court_code="nvd",
    court_level="federal-district",
    state="NV",
    date_filed="2026-08-19",
    docket_number="2:25-cv-01195-APG-DJA",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court dismissed the second amended complaint and warned Kelly that citing fake cases generated by AI can lead to sanctions.",
    ai_passage="FINRA states that Kelly’s opposition to its motion to dismiss contains several nonexistent case citations and quotations that do not appear in Kelly’s cited caselaw. I reviewed the citations in the first few pages of Kelly’s opposition and found several quotes that did not appear in the cited cases. These false quotes appear on page 2, lines 11-12; page 3, lines 3-4; and page 9, line 20 to page 10, line 5 of Kelly’s opposition. ... There has been a rise in fake authority cited in briefs, usually as the result of using generative AI software, like ChatGPT, to draft pleadings. Chavez-DeRemer v. NAB, LLC, No. 2:21-CV-00984-JAD-EJY, 2025 WL 2308676, at *3 (D. Nev. Aug. 11, 2025). Generative AI often invents fake cases and legal precedent in its drafting, and using it is no excuse for not verifying the veracity of citations. ... Going forward, Kelly is reminded of his duty under Federal Rule of Civil Procedure 11(b)(2) and that citing fake cases drafted by generative AI violates this rule. Failure to comply in the future may result in sanctions.",
    cited_authorities=["Fed. R. Civ. P. 11", "Golden Eagle Distributing Corp. v. Burroughs Corp., 801 F.2d 1531 (9th Cir. 1986)", "Whiting v. City of Athens, Tenn., 170 F.4th 455 (6th Cir. 2026)", "Chavez-DeRemer v. NAB, LLC, 2025 WL 2308676 (D. Nev. Aug. 11, 2025)"],
    summary="The District of Nevada dismisses William Lee Kelly’s second amended complaint against FINRA and warns him about AI-generated fake authority. The court finds several false quotes and nonexistent citations in his opposition and explains that future Rule 11 violations may lead to monetary or nonmonetary sanctions.",
    incident={
        "conduct": "Self-represented plaintiff’s opposition contained several nonexistent case citations and false quotations that did not appear in the cited cases.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="738fd8112072ef8f65eefda935972b03cdb7f69b59676b235d25eeca1bc7798b",
    source_url=source + "/documents/2924/Kelly_v._Financial_Industry_Regulatory_Authority_USA_19_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="iowactapp-2026-wilkinson-v-schmelzer",
    case_name="Wilkinson v. Schmelzer",
    court="Court of Appeals of Iowa",
    court_level="state-appellate",
    state="IA",
    date_filed="2026-08-19",
    docket_number="25-0799",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed, declined AI-use sanctions, and awarded appellate attorney fees and costs on other grounds.",
    ai_passage="In her resistance to Brett’s motion for remand and request for sanctions, Lacey asked our supreme court to impose sanctions on Brett for purported use of generative AI in his limited-remand motion and briefs. ... The twist is that, absent the presence of a hallucinated case, it is difficult to differentiate poor human drafting from unverified generative AI. Here, we can find no hallucinated case. And it is impossible for us to say with certainty whether Brett’s single reference to the nonexistent “Iowa R. App. P. 6.1004(3)” was a simple typo or the result of unchecked AI use. Thus, we decline to apply sanctions for Brett’s purported use of AI. But regardless of whether Brett’s briefs were directly drafted by him or a faraway datacenter, he is bound by the same duty to verify his briefs’ accuracy and compliance with our appellate rules.",
    cited_authorities=["Luke v. Department of Health & Human Services, 2025 WL 2237311 (Iowa Ct. App. Aug. 6, 2025)", "Iowa R. App. P. 6.1004(3)", "Iowa R. App. P. 6.903"],
    summary="The Court of Appeals of Iowa affirms a custody order and addresses a sanctions request based on alleged AI use. The court finds no hallucinated case, says it cannot determine whether a nonexistent appellate rule citation is a typo or unchecked AI output, and declines AI-use sanctions.",
    incident={
        "conduct": "Self-represented appellant cited nonexistent Iowa R. App. P. 6.1004(3), but the court could not tell whether it was a typo or unchecked AI output.",
        "outcome": "other",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="3eb7fd6e6ab6607789cfe5699a02019f458cd68edacb3808dfe6188944c72ff8",
    source_url=source + "/documents/2918/Brett_Thomas_Wilkinson_v._Lacey_Schmelzer_USA_19_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="ilnd-2026-snisko-v-cascade-funding",
    case_name="Snisko v. Cascade Funding Mortgage Trust HB4",
    court="United States District Court for the Northern District of Illinois",
    court_code="ilnd",
    court_level="federal-district",
    state="IL",
    date_filed="2026-08-19",
    docket_number="25 CV 13339",
    document_type="memorandum-opinion",
    topics=["fabricated-citations"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed the bankruptcy court and ordered appellant's counsel to show cause why he should not be sanctioned.",
    ai_passage="Appellant’s brief is replete with false quotations and erroneous statements of law. By way of example, appellant cites In re Chi., Milwaukee, St. Paul & Pac. R.R. Co., 6 F.3d at 1188, for the proposition that the applicable standard of review is de novo. [17] at 18. True, a bankruptcy court’s legal conclusions are reviewed de novo. But this proposition cannot be found in the cited case. To the contrary, In re Chi., Milwaukee, St. Paul & Pac. R.R. Co. makes clear that the proper standard of review for a permissive-abstention case is abuse of discretion. 6 F.3d at 1188. Another example includes apparent quotations that do not appear in the cited cases. See, e.g., [17] at 32 (falsely quoting In re Tarnow, 749 F.2d 464, 465 (7th Cir. 1984)); [17] at 23 (falsely quoting In re Aguirre, 37 F.4th 427, 431 (7th Cir. 2022)); [17] at 26 (falsely quoting In re Boughton, 60 B.R. 373, 376 (N.D. Ill. 1986)); [17] at 39 (falsely quoting In re Chi., Milwaukee, St. Paul & Pac. R.R. Co., 6 F.3d at 1192)). ... I order appellant’s counsel, Martin Spencer, to show cause why he should not be sanctioned for the fabricated legal citations and other misrepresentations.",
    cited_authorities=["In re Chi., Milwaukee, St. Paul & Pacific Railroad Co., 6 F.3d 1184 (7th Cir. 1993)", "In re Tarnow, 749 F.2d 464 (7th Cir. 1984)", "In re Aguirre, 37 F.4th 427 (7th Cir. 2022)", "In re Boughton, 60 B.R. 373 (N.D. Ill. 1986)", "In re Pajian, 785 F.3d 1161 (7th Cir. 2015)", "In re K&R Mining, Inc., 135 B.R. 269 (Bankr. N.D. Ohio 1991)", "Secrease v. Western & Southern Life Insurance Co., 800 F.3d 397 (7th Cir. 2015)"],
    summary="The Northern District of Illinois affirms a bankruptcy abstention order and identifies false quotations and erroneous legal statements in Peter Snisko’s appellate brief. The court says counsel doubled down after appellee flagged the errors and orders attorney Martin Spencer to show cause regarding fabricated citations and other misrepresentations.",
    incident={
        "conduct": "Appellant’s counsel filed false quotations and erroneous statements of law, then repeated them in reply after appellee identified the errors.",
        "outcome": "pending",
        "actor": "lawyer",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="19b253feed1d8468651cca0df96177abc90529f66a1b05cbabdffbe68c3c2b61",
    source_url=source + "/documents/2910/Snisko_v._Cascade_Funding_Mortgage_Trust_HB4_USA_19_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="calctapp-2026-marriage-of-dillon",
    case_name="In re Marriage of Dillon",
    court="California Court of Appeal, Fourth Appellate District, Division One",
    court_level="state-appellate",
    state="CA",
    date_filed="2026-08-19",
    docket_number="D085064",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed the order, declined sanctions, but denied respondent prevailing-party costs because of hallucinated citations.",
    ai_passage="Wife miscited three cases in her respondent’s brief by attributing to them quotations or legal propositions that do not appear in the cited opinions.3 The miscitations appear to be the result of Wife’s use of generative artificial intelligence without sufficient verification. We have disregarded the arguments in Wife’s brief that are based on the miscited authorities.4 Husband “has considered, but chosen not, to seek sanctions for violations of the relevant rules of court.” (See rule 8.204(a)(1)(B) [requiring that assertions of law in a brief be supported by citation to legal authority]; Noland v. Land of the Free, L.P. (2025) 114 Cal.App.5th 426, 445 [“relying on fabricated legal authority is sanctionable”]; Sheerer v. Panas (2026) 119 Cal.App.5th 367, 371 [it is “a requirement of all attorneys and self-represented litigants responsible for briefs filed in this Court” to “verify citations”].) We decline to sanction Wife. We do, however, find it appropriate because of the hallucinated citations to deny her prevailing party costs on appeal.",
    cited_authorities=["Wilkison v. Wiederkehr, 101 Cal.App.4th 822 (2002)", "Brown v. Grimes, 192 Cal.App.4th 265 (2011)", "In re Marriage of Iberti, 55 Cal.App.4th 1434 (1997)", "Cal. Rules of Court, rule 8.204(a)(1)(B)", "Noland v. Land of the Free, L.P., 114 Cal.App.5th 426 (2025)", "Sheerer v. Panas, 119 Cal.App.5th 367 (2026)", "Cal. Rules of Court, rule 8.278"],
    summary="The California Court of Appeal affirms an order in Marriage of Dillon and addresses three miscited cases in the respondent’s self-represented brief. The court disregards arguments based on the hallucinated citations, declines sanctions because none were sought, and denies prevailing-party costs on appeal.",
    incident={
        "conduct": "Self-represented respondent attributed quotations or propositions to Wilkison, Brown, and Iberti that did not appear in those opinions.",
        "outcome": "costs-order",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="c2e08e2a44efff4c76b5d77206ac6f652a53432050e887d17e98fd8cea827bfe",
    source_url=source + "/documents/2917/Marriage_of_Dillon_USA_18_AUgust_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="gactapp-2026-mitchell-v-hig-realty-credit",
    case_name="Mitchell v. HIG Realty Credit Fund, L.P.",
    court="Court of Appeals of Georgia",
    court_level="state-appellate",
    state="GA",
    date_filed="2026-08-19",
    docket_number="A26A0854",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed summary judgment and warned Mitchell that future fictitious or inapplicable citations may result in sanctions.",
    ai_passage="As an initial matter, we note that in his appellate briefing, Mitchell cites five cases that are either fictitious or have nothing to do with the propositions for which they are cited.1 These defects suggest that Mitchell’s briefs were “drafted with the use of unchecked generative AI,”2 and his reliance on non-existent law is a clear impediment to the work of this Court.3 We elect not to sanction Mitchell because HIG has not complained and does not appear to have been hampered in responding to Mitchell’s arguments.4 Nevertheless, we caution Mitchell that any future filings in this Court containing citations to fictitious or plainly inapplicable cases may result in the imposition of sanctions.5 ... Mitchell purports to cite Walker v. Pierce, 315 Ga. App. 524 (2012), and Crenshaw v. Ga. Dep’t of Human Resources, 263 Ga. 722 (1994), which do not exist. He also cites Henson v. Columbus Bank & Trust Co., 144 Ga. App. 80 (240 SE2d 284) (1977), and Stamps v. Nelson, 290 Ga. App. 277 (659 SE2d 697) (2008), which do exist, but have nothing to do with the issues raised in this appeal.",
    cited_authorities=["Walker v. Pierce, 315 Ga. App. 524 (2012)", "Crenshaw v. Georgia Department of Human Resources, 263 Ga. 722 (1994)", "Henson v. Columbus Bank & Trust Co., 144 Ga. App. 80 (1977)", "Stamps v. Nelson, 290 Ga. App. 277 (2008)", "Slay v. Ross, 379 Ga. App. 1 (2026)", "Shahid v. Essam, 376 Ga. App. 145 (2025)", "Court of Appeals Rule 7(e)(2)"],
    summary="The Court of Appeals of Georgia affirms summary judgment for HIG Realty Credit Fund and warns Trentiss Mitchell about citations in his self-represented appellate briefing. The court identifies two non-existent cases and two unrelated cases, says the defects suggest unchecked generative AI, and declines sanctions.",
    incident={
        "conduct": "Self-represented appellant cited two nonexistent cases and two unrelated cases for propositions in his appellate brief.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="71eefc9d5bb356b69a2be63a74fd3a6c60ddd8894f3512f50fee48cf286fa345",
    source_url=source + "/documents/2914/TRENTISS_MITCHELL_v._HIG_REALTY_CREDIT_FUND_USA_19_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="washctapp-2026-muriel-v-farris",
    case_name="In re Marriage of Muriel and Farris",
    court="Court of Appeals of Washington, Division Two",
    court_level="state-appellate",
    state="WA",
    date_filed="2026-08-18",
    docket_number="60903-7-II",
    document_type="opinion",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed the parenting plan and awarded fees for time spent responding to a brief citing a nonexistent case.",
    ai_passage="However, we award appellate attorney fees to Rebekah under RAP 18.9(a) for her time spent reviewing and responding to Jonathan’s response brief. Here, Jonathan’s brief twice cites to Marriage of Sanjuan to support his arguments, but as Rebekah points out in her reply brief, no such case exists. We surmise that Jonathan used artificial intelligence (AI) to assist in writing his brief, which resulted in an “AI hallucination.”13 While Jonathan is entitled to use AI to write his response brief, he is still required to conduct a reasonable inquiry and confirm that the claims he advances are well-grounded in fact and in law. In re Estate of Little, 9 Wn. App. 2d 262, 274 n.4, 444 P.3d 23 (stating that “[w]e hold a pro se litigant to the same standard as an attorney”), review denied, 194 Wn.2d 1006 (2019). In citing to a hallucinated case, Jonathan has submitted a frivolous filing that “is so totally devoid of merit.” A.T., 11 Wn. App. 2d at 171. Accordingly, we award Rebekah appellate attorney fees for time spent reviewing and responding to Jonathan’s response brief in an amount to be determined by the commissioner pursuant to RAP 18.1(f).",
    cited_authorities=["Marriage of Sanjuan", "RAP 18.9(a)", "In re Estate of Little, 9 Wn. App. 2d 262 (2019)", "A.T., 11 Wn. App. 2d 156", "RAP 18.1(f)"],
    summary="The Washington Court of Appeals affirms a parenting plan and awards Rebekah Muriel fees for responding to Jonathan Farris’s response brief. The court says the brief twice cited nonexistent Marriage of Sanjuan, surmises AI-assisted drafting, deems the filing frivolous, and sets the fee amount for the commissioner.",
    incident={
        "conduct": "Response brief twice cited nonexistent Marriage of Sanjuan; the court surmised AI-assisted drafting and deemed the filing frivolous.",
        "outcome": "costs-order",
        "actor": "other",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    tracker_slug=None,
    text_sha256="80df6d4e05c05ac8751eefb1db2d549ea732a44e0c6de7dee1b5fb0a25821d23",
    source_url=source + "/documents/2894/Muriel_v._Farris_USA_18_August_2026.pdf",
    notes=secondary_note + " The opinion attributes the response brief to Jonathan; the source lead identifies a lawyer.",
)


add(
    decision_id="txwd-2026-perez-v-blanche",
    case_name="Garcia Perez v. Blanche",
    court="United States District Court for the Western District of Texas",
    court_code="txwd",
    court_level="federal-district",
    state="TX",
    date_filed="2026-08-18",
    docket_number="1:26-cv-00786-RP",
    document_type="order",
    topics=["fabricated-citations"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court ordered additional briefing and cautioned petitioner's counsel that future hallucinated citations may result in sanctions.",
    ai_passage="He then cites a variety of cases supporting this contention, the majority of which do not exist.4 The Court will nonetheless consider Petitioner’s due process argument, as it will not punish Petitioner for his counsel’s mistakes. ... The Court notes that an alarming number of cases cited by Petitioner for support in his Reply are nonexistent, “hallucinated” cases, such as Kostak v. Garland, No. 24-cv-11024-ADB, 2025 WL 2472136, at *4–6 (D. Mass. May 22, 2025); Martinez Lopez v. Garland, No. 1:25-cv-00069, 2026 WL 1200000, at *4–5 (D. Colo. Mar. 24, 2026); Cruz-Reyes v. Decker, No. 1:25-cv-01719-MKV, 2025 WL 332315, at *4–6 (S.D.N.Y. Jan. 21, 2025); Castanon Nava v. Garland, No. 2:25-cv-01308-JHC, 2026 WL 1234567, at *5–7 (W.D. Wash. Feb. 11, 2026); Duarte Escobar v. Garland, No. 1:25-cv-00963-MSN-LRV, 2025 WL 7061234, at *2–4 (E.D. Va. Dec. 2, 2025). ... None of these cases exist on Westlaw or on the purported courts’ dockets. Indeed, Petitioner also hallucinates a case purportedly written by this Court: Garcia v. Mullin, No. 1:25-cv-00836-RP, 2026 WL 1045678, at *2–4 (W.D. Tex. Mar. 9, 2026). Petitioner’s counsel is strongly cautioned that future inaccurate citations “hallucinated” by generative artificial intelligence tools may result in sanctions.",
    cited_authorities=["Kostak v. Garland, 2025 WL 2472136 (D. Mass. May 22, 2025)", "Martinez Lopez v. Garland, 2026 WL 1200000 (D. Colo. Mar. 24, 2026)", "Cruz-Reyes v. Decker, 2025 WL 332315 (S.D.N.Y. Jan. 21, 2025)", "Castanon Nava v. Garland, 2026 WL 1234567 (W.D. Wash. Feb. 11, 2026)", "Duarte Escobar v. Garland, 2025 WL 7061234 (E.D. Va. Dec. 2, 2025)", "Garcia v. Mullin, 2026 WL 1045678 (W.D. Tex. Mar. 9, 2026)", "Fed. R. Civ. P. 11(b)"],
    summary="The Western District of Texas orders more briefing in a habeas case and cautions Gilberto Garcia Perez’s counsel. The order says most cases cited in petitioner’s reply do not exist, lists six hallucinated authorities including one purportedly from the same court, and warns future inaccurate AI citations may be sanctionable.",
    incident={
        "conduct": "Petitioner’s counsel cited multiple nonexistent immigration cases in reply, including a fabricated decision purportedly issued by the same district court.",
        "outcome": "warning",
        "actor": "lawyer",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="5c8ec9f9a145bde469c9df023b6e518c8f7c4bfe9be8036a42e10166d5233c34",
    source_url=source + "/documents/2919/Perez_v._Blanche_USA_18_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="wawd-2026-ledoux-v-outliers-summary-judgment",
    case_name="LeDoux v. Outliers, Inc.",
    court="United States District Court for the Western District of Washington",
    court_code="wawd",
    court_level="federal-district",
    state="WA",
    date_filed="2026-08-18",
    docket_number="3:24-cv-05808-TMC",
    document_type="order",
    topics=["fabricated-citations", "evidence-authentication"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="Claude or ChatGPT",
    disposition="The court granted defendants' summary judgment motion and excluded an expert report after finding hallucinated citations undermined reliability.",
    ai_passage="The Court also issued sua sponte sanctions against Plaintiff’s attorney, Ms. Jocelyn Stewart, for generating numerous false citations with artificial intelligence and submitting them to the Court without verification. Dkt. 265. Multiple such citations existed in the expert reports of Mr. James Kababick and Dr. Ronald Shippee, where Plaintiff admitted that “she used Claude or ChatGPT to ‘generate a formatted citation table’ for academic articles and ‘provided the same AI-generated citation table to both experts as an appendix, and neither expert caught the errors in the citation data before signing their reports.’” Dkt. 265 at 7 (quoting Dkt. 245 at 17–18). ... The Court agrees with Defendants and finds that Dr. Holguin’s multiple hallucinated citations “shatter[] his credibility with this Court.” Kohls v. Ellison, No. 24-CV-3754 (LMP/DLM), 2025 WL 66514, at *4 (D. Minn. Jan. 10, 2025). ... This level of involvement from counsel in drafting (with AI) the list of materials supposedly relied upon by Dr. Holguin, and Dr. Holguin’s lack of diligence in verifying the sources that he represented were the basis for his opinion, prevent Plaintiff from meeting her burden to show that Dr. Holguin’s opinion is “based on sufficient facts or data,” is “the product of reliable principles and methods,” or “reflects a reliable application of the principles and methods to the facts of the case.” Fed. R. Evid. 702(b)–(d).",
    cited_authorities=["Dkt. 265", "Dkt. 245", "Kohls v. Ellison, 2025 WL 66514 (D. Minn. Jan. 10, 2025)", "Concord Music Group, Inc. v. Anthropic PBC, 2025 WL 1482734 (N.D. Cal. May 23, 2025)", "Fed. R. Evid. 702"],
    summary="The Western District of Washington grants summary judgment for Outliers and addresses AI-generated citation tables used in expert materials. The court recounts sanctions against counsel, finds Dr. Holguin’s hallucinated citations undermine his report’s reliability, and excludes that expert opinion under Rule 702 and Daubert.",
    incident={
        "conduct": "Counsel used Claude or ChatGPT to generate false academic citation tables supplied to experts; Dr. Holguin’s report also contained hallucinated citations.",
        "outcome": "sanctions",
        "actor": "lawyer",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": "Claude or ChatGPT",
    },
    tracker_slug="ledoux-v-outliers",
    text_sha256="e5098ff93fc925099a3bfa7b654fc9ae0c899ff9279b6cfc19e3bc45a15c845d",
    source_url=source + "/documents/2902/Ledoux_v._Outliers_USA_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="illappct-2026-sani-v-institute-for-human-reproduction",
    case_name="Sani v. Institute for Human Reproduction",
    court="Appellate Court of Illinois, First District",
    court_level="state-appellate",
    state="IL",
    date_filed="2026-08-18",
    citation="2026 IL App (1st) 252264-U",
    docket_number="1-25-2264",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed dismissal and admonished the self-represented appellant about nonexistent or unsupported citations.",
    ai_passage="We are particularly troubled by the fact that one of her case citations in her opening brief (as IHR notes) does not exist: “Helm v. Illinois Cent. R.R.” does not appear in any reported case in this state, and the precise citation (again, as IHR points out), “142 Ill. App. 3d 108 (1986),” is for a criminal case entitled, “People v. Hardy,” which again contains no discussion of judicial notice. Although we do not know for certain whether this citation was the result of an artificial intelligence (AI) “hallucination,” Sani should be aware that this court is growing increasingly impatient with the patently improper practice of submitting citations of authority that neither exist nor even arguably support the claim on appeal. See, e.g., Scott v. Illinois Human Rights Comm'n, 2026 IL App (1st) 251462, ¶ 56 (imposing a $15,000 fine on an attorney whose brief contained “10 false citations”). Although Sani is proceeding pro se, she must comply with the same rules and will be held to the same standards as licensed attorneys.",
    cited_authorities=["Helm v. Illinois Cent. R.R., 142 Ill. App. 3d 108 (1986)", "People v. Hardy, 142 Ill. App. 3d 108 (1986)", "Scott v. Illinois Human Rights Commission, 2026 IL App (1st) 251462"],
    summary="The Illinois Appellate Court affirms dismissal of Lemna Sani’s complaint and admonishes her about a nonexistent citation in her self-represented opening brief. The court says Helm v. Illinois Central Railroad does not exist and that the reporter citation leads to People v. Hardy, an unrelated criminal case.",
    incident={
        "conduct": "Self-represented appellant cited nonexistent Helm v. Illinois Cent. R.R.; the reporter citation led to People v. Hardy and did not address judicial notice.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="3efa1dc1479694f4c7338edbdca5b02de7424d4753d444d3b2fbabd7882a66df",
    source_url=source + "/documents/2922/Sani_v_Institute_for_Human_Reproduction_USA_18_August_2026.pdf",
    notes="Official source not obtained after CourtListener throttling; read the court-authored text from the Charlotin mirror. The mirror text appears to include Westlaw formatting.",
)


add(
    decision_id="texapp-2026-kourradi-v-christopher",
    case_name="Kourradi v. Christopher",
    court="Court of Appeals of Texas, First District",
    court_level="state-appellate",
    state="TX",
    date_filed="2026-08-18",
    docket_number="01-26-00014-CV",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court struck Kourradi's fourth brief and dismissed the appeal for want of prosecution.",
    ai_passage="The brief also included incomplete legal citations accompanied by unintelligible numeric strings (e.g., “2990836”). We again struck Kourradi’s appellate brief and ordered Kourradi to file a corrected brief. We admonished Kourradi to ensure that record references and citations to authorities are accurate. See Campbell v. Campbell, No. 03-25-00388-CV, 2026 WL 179402, at *2 n.3 (Tex. App.—Austin Jan. 22, 2026, no pet.) (mem. op.) (admonishing appellant to “take care not to include hallucinated citations, quotations, or authorities of any kind in the materials that he submits for filing in this Court”). ... More concerningly, we are unable to locate the following legal authorities on which Kourradi relies when using the citation format he provides: • Ruth Wheeler v. John Collier Hinson, No. 07-10-00308-CV, 2011 WL 1905858 (Tex. App.—Amarillo May 19, 2011, no pet.) (mem. op.) • David Lee Carpenter, Jr. v. Sharon K. Carpenter, No. 09-11-00414-CV, 2012 WL 2370823 (Tex. App.—Beaumont July 5, 2012, no pet.) (mem. op.) • Brazos Valley Roadrunners, LLC v. Brian Niles, No. 03-21-00523-CV, 2022 WL 1938866, at *4 (Tex. App.—Austin June 1, 2022, no pet.) (mem. op.) ... The database identifiers are non-existent, and the appellate case numbers point us to appeals that involve parties different from the parties listed in the citations provided by Kourradi. ... The nature of the errors suggests that each of the foregoing legal citations is, at best, partially fabricated.",
    cited_authorities=["Campbell v. Campbell, 2026 WL 179402 (Tex. App.—Austin Jan. 22, 2026)", "Ruth Wheeler v. John Collier Hinson, 2011 WL 1905858", "David Lee Carpenter, Jr. v. Sharon K. Carpenter, 2012 WL 2370823", "Brazos Valley Roadrunners, LLC v. Brian Niles, 2022 WL 1938866", "George Jamil Wehbe v. State, 2011 WL 1742356", "Tex. R. App. P. 38.1", "Tex. R. App. P. 38.9", "Tex. R. App. P. 42.3"],
    summary="The Texas First Court of Appeals strikes Manny Kourradi’s fourth self-represented brief and dismisses the appeal. The memorandum identifies multiple unlocatable or mismatched Westlaw-style citations, says the errors are at best partially fabricated, and treats the defective briefing as grounds for dismissal.",
    incident={
        "conduct": "Self-represented appellant filed repeated briefs with unlocatable or mismatched Westlaw-style citations and appellate case numbers.",
        "outcome": "dismissal",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="42b2c481b3cfa5cc8a391eb3720b1f93c9bfeedbf9114ba23de0a31b9c9273e2",
    source_url=source + "/documents/2915/Manny_Kourradi_v._Wyatt_Brian_Christophe_USA_18_August_2026.pdf",
    notes=secondary_note,
)


add(
    decision_id="indctapp-2026-brankle-v-schmell",
    case_name="Brankle v. Schmell",
    court="Court of Appeals of Indiana",
    court_level="state-appellate",
    state="IN",
    date_filed="2026-08-14",
    docket_number="26A-PL-887",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="ChatGPT or other form of artificial intelligence",
    disposition="The court affirmed a $1,546 expenses award and remanded for appellate attorneys' fees.",
    ai_passage="Brankle’s motion is totally without merit. First, Commercial Court Rules are inapplicable to this case[,] and Brankle should not cite to them again. Brankle’s repeated citations to rules that do not exist or fictitious cases leads the Court to opine that Brankle is using ChatGPT or other form of artificial intelligence to prepare his numerous motions, responses, and notices to the Court which is a violation of Ind. Trial Rule 11(A). ... First, Brankle claims the motion to compel was substantially justified. A party is “substantially justified” in filing a motion to compel “if reasonable persons could conclude that a genuine issue existed as to whether a person was bound to comply with the requested discovery.” Yount v. Carpenter Co. Inc., 219 N.E.3d 127, 132 (Ind. Ct. App. 2023) (quoting Huber v. Montgomery Cnty. Sheriff, 940 N.E.2d 1182, 1186 (Ind. Ct. App. 2010)). A motion riddled with citations to hallucinated authorities is hardly “substantially justified.” ... Brankle does not address the trial court’s findings that he cited to inapplicable Commercial Court Rules and hallucinated authorities.",
    cited_authorities=["Ind. Trial Rule 11(A)", "Ind. Trial Rule 37(A)(4)", "Yount v. Carpenter Co. Inc., 219 N.E.3d 127 (Ind. Ct. App. 2023)", "Huber v. Montgomery County Sheriff, 940 N.E.2d 1182 (Ind. Ct. App. 2010)", "Indiana Appellate Rule 46(A)(8)(a)"],
    summary="The Court of Appeals of Indiana affirms the denial of David Brankle’s motion to compel and a $1,546 expenses award. The memorandum quotes the trial court’s finding that Brankle cited nonexistent rules and fictitious cases suggesting ChatGPT use, and holds hallucinated authorities cannot substantially justify the motion.",
    incident={
        "conduct": "Self-represented litigant cited nonexistent Commercial Court Rules and fictitious cases in a motion to compel and related filings.",
        "outcome": "costs-order",
        "actor": "litigant-in-person",
        "monetary_penalty": 1546,
        "currency": "USD",
        "ai_tool": "ChatGPT or other form of artificial intelligence",
    },
    text_sha256="0f98b2251291e09c3d463d74d7a69c4016d33c01dd0208becf04a3bd45da9830",
    source_url=source + "/documents/2920/Brankle_v._Schmell_USA_14_August_2026.pdf",
    notes=secondary_note,
)


existing = []
with open("work/agents/decisions-t1-s1.jsonl", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            existing.append(json.loads(line))

seen = {r["decision_id"] for r in existing}
merged = existing + [r for r in rows if r["decision_id"] not in seen]

with open("work/agents/decisions-t1-s1.jsonl", "w", encoding="utf-8") as f:
    for row in merged:
        f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")

print(len(merged))
