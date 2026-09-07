import json

fetched_at = "2026-09-07T13:15:21.976-07:00"
source = "https://www.damiencharlotin.com"
secondary_note = "Official source not obtained after CourtListener throttling; read the court-authored document from the Charlotin mirror and marked link-only."
westlaw_note = "Official source not obtained after CourtListener throttling; read the court-authored text from the Charlotin mirror. The mirror text appears to include Westlaw formatting."

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
        notes=secondary_note,
        lead_source=["charlotin-cc0"],
        fetched_at=fetched_at,
        verification="link-only",
    )
    base.update(kw)
    rows.append(base)


add(
    decision_id="insd-2026-harris-v-wray",
    case_name="Harris v. Wray",
    court="United States District Court for the Southern District of Indiana",
    court_code="insd",
    court_level="federal-district",
    state="IN",
    date_filed="2026-08-14",
    citation="2026 WL 2374808",
    docket_number="1:26-cv-01342-JRO-MG",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court dismissed the complaint without prejudice, allowed amendment, and warned Harris about Rule 11 and AI-policy compliance.",
    ai_passage="In Harris's motion for extension of time to effect service of process, he cites Walsh v. Kreiger, No. 19-cv-1764, 2020 WL 6325983, at 2 (E.D. Wis. Oct. 28, 2020) (citing United States v. McLaughlin, 470 F.3d 698, 700 (7th Cir. 2006)), for the proposition that “good cause” not the stricter “excusable neglect” standard is the appropriate test for Fed. R. Civ. P. 4(m) extensions. Dkt. 15 at 3. While the Court has found McLaughlin and Walsh to be real cases, the Walsh citation is wholly incorrect. The docket number listed following Harris's Walsh cite is linked to a different case in the Eastern District of Wisconsin, and the Westlaw citation leads to nowhere. While Walsh v. Kreiger appears to be a real case and there is an October 28, 2020, order referencing Mclaughlin, the incorrect cite gives the Court pause. ... Because the Court dismisses Harris's complaint in its entirety, it will not order him to show cause at this time. However, Harris is accordingly warned of the possibility of sanctions if any future filings violate Rule 11(b).",
    cited_authorities=["Walsh v. Kreiger, No. 19-cv-1764, 2020 WL 6325983 (E.D. Wis. Oct. 28, 2020)", "United States v. McLaughlin, 470 F.3d 698 (7th Cir. 2006)", "Fed. R. Civ. P. 4(m)", "Fed. R. Civ. P. 11"],
    summary="The Southern District of Indiana dismisses Darryl Harris’s complaint without prejudice and warns him about an incorrect citation in a service-extension motion. The court says the Walsh docket number linked to a different case, the Westlaw citation led nowhere, and future Rule 11 violations may be sanctioned.",
    incident={
        "conduct": "Self-represented plaintiff cited Walsh v. Kreiger with a docket number linked to another case and a Westlaw citation that led nowhere.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="9817e328b82299f3d39502e28ac318afafc5f8132e6ef3088ae3da9fd920c3fd",
    source_url=source + "/documents/2901/Harris_v._Wray_USA_14_August_2026.pdf",
    notes=westlaw_note,
)


add(
    decision_id="ca5-2026-guerra-quezada-v-united-states",
    case_name="Guerra-Quezada v. United States",
    court="United States Court of Appeals for the Fifth Circuit",
    court_code="ca5",
    court_level="federal-appellate",
    state=None,
    date_filed="2026-08-14",
    docket_number="25-10372; 25-10555",
    document_type="opinion",
    topics=["fabricated-citations"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed one dismissal, remanded the other to dismiss without prejudice, and warned counsel about defective citations.",
    ai_passage="Appellants have not adequately briefed these claims: They are completely unsubstantiated by citations to the record, and the case citations in the briefing are systematically defective. Accordingly, Appellants have forfeited these arguments. ... Troubling to the court is the fact that the briefs filed in both cases by Appellants’ counsel contain significant inaccuracies. Both briefs quote Ng Fung Ho v. White, 259 U.S. 276, 284 (1922), for the proposition that “[N]o deportable alien may be expelled until it has first been determined . . . that he is in fact an alien.” This court’s research has failed to locate this quote in Ng Fung Ho or in any other opinion. Additionally, in Guerra-Vasquez’s opening brief, a parenthetical cites the correct part of Ng Fung Ho but misquotes the majority. Both briefs also attribute the phrase, “[i]t is wrong to deport a United States citizen,” to Ng Fung Ho, but that phrase does not appear in the opinion. ... Federal Rule of Appellate Procedure 28 requires all filed briefs to contain arguments supported by “citations to the authorities,” disallowing citation to nonexistent or fabricated cases. ... The court takes no action now for the foregoing deficiencies, but counsel must take this obligation seriously in the future.",
    cited_authorities=["Ng Fung Ho v. White, 259 U.S. 276 (1922)", "Doe v. McAleenan, 926 F.3d 910 (7th Cir. 2019)", "Afroyim v. Rusk, 387 U.S. 253 (1967)", "Perez v. Brownell, 356 U.S. 44 (1958)", "Fed. R. App. P. 28", "Fed. R. App. P. 32", "Fed. R. App. P. 38", "Fed. R. App. P. 46", "Garces v. Hernandez, 2025 WL 2401001 (5th Cir. Aug. 19, 2025)"],
    summary="The Fifth Circuit resolves consolidated immigration appeals and warns appellants’ counsel about systematically defective authorities. The opinion identifies quotations falsely attributed to Ng Fung Ho, an incorrect circuit attribution for Doe v. McAleenan, and a quotation from an Afroyim dissent misattributed to the majority.",
    incident={
        "conduct": "Appellants’ counsel filed briefs with false quotations, a misidentified circuit decision, and a quotation attributed to the wrong Supreme Court opinion.",
        "outcome": "warning",
        "actor": "lawyer",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    tracker_slug="guerra-quezada-v-united-states",
    text_sha256="86719d5f7b78bc786652112167654ec3ac58b72004367dd6d8d0c6bfebff6187",
    source_url=source + "/documents/2900/Quezada_v._USA_USA_14_August_2026.pdf",
)


add(
    decision_id="vtsuperct-2026-rivard-v-vermont-dept-corrections",
    case_name="Rivard v. Vermont Department of Corrections",
    court="Superior Court of Vermont, Windham Unit",
    court_level="state-trial",
    state="VT",
    date_filed="2026-08-14",
    citation="2026 WL 2479362",
    docket_number="26-CV-01521",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court granted a sanctions motion and imposed a prefiling injunction in Vermont Superior Court civil cases.",
    ai_passage="Plaintiff has himself been admonished by the Court for citing non-existent authority. In his brief, plaintiff cited several purported decisions of this Court, including “Slayton v. Willing, 2010 VT 56, ¶ 14, 188 Vt. 216, 4 A.3d 1155,” “Sorrell v. Wigginton, 154 Vt. 301, 303 (1990),” “Morrison v. City of Montpelier, 2011 VT 9, ¶ 10,” “Thrall v. Rowan, 161 Vt. 451, 456 (1994),” and “EcoScience Corp. v. United States, 156 Vt. 185, 193 (1991),” among others. The Vermont Reports citations provided by plaintiff correspond to entirely different opinions than those named. We were unable to identify any existing case that corresponds to the citations provided in plaintiff's brief. ... Plaintiff's misrepresentation of the record extends to asserting that documents and records contain quotations that simply are not there. ... Plaintiff's practice of citing to non-existent authority and misrepresenting the contents of court records is a waste of limited judicial resources, a waste of the resources of opposing parties and further evidence of his disrespect for the courts of this State. ... Defendant's Motion for Sanctions (# 7) is GRANTED. Plaintiff is hereby ENJOINED from filing any new actions in the Civil Division of the Vermont Superior Court without obtaining prior leave from the court.",
    cited_authorities=["Slayton v. Willing, 2010 VT 56", "Sorrell v. Wigginton, 154 Vt. 301 (1990)", "Morrison v. City of Montpelier, 2011 VT 9", "Thrall v. Rowan, 161 Vt. 451 (1994)", "EcoScience Corp. v. United States, 156 Vt. 185 (1991)", "V.R.C.P. 11", "V.R.A.P. 25"],
    summary="The Vermont Superior Court grants Brattleboro’s sanctions motion against Jeffrey Rivard and imposes a civil-division prefiling injunction. The order cites Rivard’s prior non-existent authorities, mismatched Vermont Reports citations, spurious record quotations, and repeated warnings that had not changed his filing conduct.",
    incident={
        "conduct": "Self-represented plaintiff repeatedly cited non-existent Vermont authority, mismatched reporter citations, and spurious quotations from court records.",
        "outcome": "sanctions",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="9c1fa2f02d03afad0b085d8317a8fa080a421ccefc35d5eafd9c60898df70b09",
    source_url=source + "/documents/2953/Rivard_v_Vermont_Dept_of_Corrections_USA_14_August_2026.pdf",
    notes=westlaw_note,
)


add(
    decision_id="azctapp-2026-boettcher-v-boettcher",
    case_name="Boettcher v. Boettcher",
    court="Arizona Court of Appeals, Division One",
    court_level="state-appellate",
    state="AZ",
    date_filed="2026-08-14",
    docket_number="1 CA-SA 26-0121",
    document_type="opinion",
    topics=["fabricated-citations"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court accepted special action jurisdiction, granted relief in part, and struck an apparently false quotation.",
    ai_passage="Father contends the superior court both lacked jurisdiction to hold him in contempt and abused its discretion by finding him in contempt. He also contends the court imposed improper sanctions. ... In making his jurisdictional argument, Father said, “Arizona appellate courts have consistently held that a trial court may not hold a party in contempt for violating a parenting plan that was never ordered. Without a valid court order, contempt is legally impossible.” He cited two cases for the quote, neither of which contains that language. And we could not find it in any Arizona case. We strike the apparently false quotation. Matter of Est. of Acciavatti, 1 CA-CV 25-0606 PB, 2026 WL 2041963, at *2, ¶ 9 (App. July 15, 2026). But because we identified no additional citation concerns, and opposing counsel raised none (including this one), we decline to impose sanctions. Id. at *4, ¶ 18 (“citing a hallucinated case in a legal filing is sanctionable conduct.”).",
    cited_authorities=["Matter of Estate of Acciavatti, 2026 WL 2041963 (Ariz. App. July 15, 2026)"],
    summary="The Arizona Court of Appeals grants partial special-action relief in a contempt dispute and addresses a quotation in Father’s filing. The court says neither cited case contains the quoted jurisdictional rule, it cannot find the language in Arizona law, strikes the false quotation, and declines sanctions.",
    incident={
        "conduct": "Petitioner’s filing attributed a jurisdictional quotation to two cases, but neither case contained it and the court could not find it in Arizona law.",
        "outcome": "other",
        "actor": "lawyer",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="64a76c382bf74eed8516a6e6f5068c52ced2516ed100f86a06e7385241f96ab9",
    source_url=source + "/documents/2899/BOETTCHER_v._BOETTCHER_USA_14_August_2026.pdf",
)


add(
    decision_id="fladistctapp-2026-jmor-properties-v-artist-alley",
    case_name="JMOR Properties, LLC v. Artist Alley Townhomes, LLC",
    court="District Court of Appeal of Florida, Fourth District",
    court_level="state-appellate",
    state="FL",
    date_filed="2026-08-12",
    docket_number="4D2026-1787",
    document_type="opinion",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court referred petitioner's counsel to the Florida Bar after a certiorari petition contained false AI-draft citations.",
    ai_passage="Counsel filed a certiorari petition in this case that is riddled with false citations and arguments, including an unsupported allegation that this Court has “repeatedly entertained, and granted, certiorari review of orders vacating clerk’s defaults.” The petition cited a non-existent case allegedly from this Court and cited other cases that do not support this proposition. ... Counsel’s response acknowledges the false citations identified in our order and identifies additional false citations. Counsel accepts responsibility for his deficient filing but alleges that he did not mean to mislead this Court and merely submitted the wrong draft. Counsel explains that his normal process is to have artificial intelligence (“AI”) software research and draft the initial document, and he then verifies every citation and revises the draft. Counsel allegedly did that in this case and removed all the fake and false citations, but while he was making final edits, he inadvertently worked from the wrong version and ended up filing the AI’s initial draft with this Court. ... Thus, counsel’s petition misrepresented the law and cited non-existent authority for the opposite proposition. ... Accordingly, we refer this matter to the Florida Bar for consideration of disciplinary proceedings.",
    cited_authorities=["Fla. R. Jud. Admin. 2.515(d)(2)", "Fla. R. App. P. 9.410(a)", "Leibman v. Sportatorium, Inc., 374 So. 2d 1124 (Fla. 4th DCA 1979)", "Eclectic Synergy, LLC v. Seredin, 51 Fla. L. Weekly D1061 (Fla. 4th DCA May 27, 2026)", "Hessert v. Hessert, 431 So. 3d 610 (Fla. 6th DCA 2026)", "Russell v. Mells, 426 So. 3d 913 (Fla. 2d DCA 2025)", "R. Regulating Fla. Bar 4-1.1", "R. Regulating Fla. Bar 3-7.18"],
    summary="The Florida Fourth District Court of Appeal refers Barry Leff to the Florida Bar after a certiorari petition cited false AI-draft authority. Counsel says he filed the wrong draft; the court finds the petition misrepresented jurisdictional law, lacked controlling adverse authority, and cited non-existent authority.",
    incident={
        "conduct": "Petitioner's counsel filed an AI initial draft containing a nonexistent Fourth DCA case and other false citations supporting certiorari jurisdiction.",
        "outcome": "referral",
        "actor": "lawyer",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": "artificial intelligence software",
    },
    tracker_slug="jmor-properties-v-artist-alley",
    text_sha256="8ae7ec98c7005eaeae7e4a16003f0b4125a0c85f9a0b3c71a4b8bfbd36a4b73f",
    source_url=source + "/documents/2839/JMOR_Properties_LLC_v._Artist_Alley_Townhomes_LLC_et_al._USA_12_August_2026.pdf",
)


add(
    decision_id="flmd-2026-rose-v-arts-bonita",
    case_name="Rose v. Arts Bonita, Inc.",
    court="United States District Court for the Middle District of Florida",
    court_code="flmd",
    court_level="federal-district",
    state="FL",
    date_filed="2026-08-12",
    citation="2026 WL 2329753",
    docket_number="2:26-cv-484-KCD-KRH",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court partly granted an AI-use motion by warning Rose; it declined to impose a broader AI-use order.",
    ai_passage="In her response to Arts Bonita's motion to dismiss, Rose cited Prousalis v. Bert's Bikes & Fitness, No. 8:18-cv-1234, 2019 WL 13202785 (M.D. Fla. 2019). That case does not exist. Once Arts Bonita caught the error, it asked Rose to join an agreed order on generative AI use. The City signed on, but Rose refused, telling counsel that as a pro se litigant she did not want to limit her own access to research and accessibility tools and promised to keep reviewing her filings for accuracy herself. ... Rose eventually filed a notice withdrawing the citation, admitting only that the citation was “incorrect or unverifiable.” ... Rose's conduct falls near the bottom of that range—i.e., a single hallucinated citation. Even so, a fabricated citation is never harmless since it forces the opposing party and the Court to “waste time and money in exposing the deception.” ... A sanction is not yet warranted, but the record supports an admonishment. This is the only warning Rose will receive for her infraction.",
    cited_authorities=["Prousalis v. Bert's Bikes & Fitness, 2019 WL 13202785 (M.D. Fla. 2019)", "Versant Funding LLC v. Teras Breakbulk Ocean Navigation Enterprises, LLC, 2025 WL 1440351 (S.D. Fla. May 20, 2025)", "Kendrick v. Secretary, Florida Department of Corrections, 2022 WL 2388425 (11th Cir. July 1, 2022)", "O'Brien v. Flick, 2025 WL 242924 (S.D. Fla. Jan. 10, 2025)", "Mata v. Avianca, Inc., 678 F. Supp. 3d 433 (S.D.N.Y. 2023)", "Fed. R. Civ. P. 11"],
    summary="The Middle District of Florida partly grants Arts Bonita’s motion about generative AI use. The court finds Julia Rose cited a nonexistent Prousalis case, later withdrew it as incorrect or unverifiable, declines sanctions for a single hallucinated citation, and warns future inaccurate authority may be sanctioned.",
    incident={
        "conduct": "Self-represented plaintiff cited nonexistent Prousalis v. Bert's Bikes & Fitness, then withdrew it as incorrect or unverifiable.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="2e0acf6c6f33a7325d92281c09c5d638f8132ce1366d969ea836aa9a03ed71bd",
    source_url=source + "/documents/2831/Rose_v_Arts_Bonita_Inc_USA_12_August_2026.pdf",
    notes=westlaw_note,
)


add(
    decision_id="alnd-2026-chapman-v-city-of-priceville",
    case_name="Chapman v. City of Priceville",
    court="United States District Court for the Northern District of Alabama",
    court_code="alnd",
    court_level="federal-district",
    state="AL",
    date_filed="2026-08-12",
    citation="2026 WL 2350902",
    docket_number="5:26-cv-84-HDM",
    document_type="order",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court publicly reprimanded attorney Scott Morro and ordered notice to opposing counsel and presiding judges in pending cases.",
    ai_passage="The court finds, based upon its own careful review and Morro's admission, (doc. 34 at 1–2), that the purported citations, quotations, and representations of law in the filings at issue were fabricated. Accordingly, by citing nonexistent cases and attributing nonexistent quotations and propositions of law to actual authorities, Morro made false statements of law. Morro admits that his nonlawyer client drafted the filings at issue and that Morro submitted the filings to the court without ensuring that the assertions within were legally correct. Transcript of 8/6/2026 Show Cause Hearing at 5–10. This is no different than submitting AI-generated work product to the court without thoroughly checking it. Morro signed the filings, and he is responsible for them. ... Morro presented to the court numerous citations, purported quotations, and representations that either do not exist or are unsupported by the cited law. ... Accordingly, the court will not, in this instance, refer this matter to the Alabama State Bar, order a monetary fine, disqualify Attorney Morro from this case, or suspend him from practice in the Northern District of Alabama, though he is WARNED that each of these options is on the table should he commit a similar infraction in the future. ... The court PUBLICLY REPRIMANDS Attorney Scott Thomas Morro.",
    cited_authorities=["Fed. R. Civ. P. 11", "Kaplan v. DaimlerChrysler, A.G., 331 F.3d 1251 (11th Cir. 2003)", "Miller v. Regions Bank, 2026 WL 1430381 (N.D. Ala. May 21, 2026)", "Johnson v. Dunn, 792 F. Supp. 3d 1241 (N.D. Ala. 2025)"],
    summary="The Northern District of Alabama sanctions Scott Morro for false citations, quotations, and legal representations in Chapman v. City of Priceville. The court treats client-drafted filings submitted without verification like unchecked AI work, publicly reprimands Morro, orders notice in pending cases, and directs publication.",
    incident={
        "conduct": "Plaintiff’s counsel filed nonexistent cases and false quotations/propositions drafted by his client without reading and verifying the cited authorities.",
        "outcome": "sanctions",
        "actor": "lawyer",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    tracker_slug="chapman-v-city-of-priceville",
    text_sha256="e55eeecb5e6d7ad41969d6e6cd8c14c184753b0f6594fdc5ba6ab65c35c3a7ec",
    source_url=source + "/documents/2836/Chapman_v._City_of_Priceville_USA_12_August_2026.pdf",
    notes=westlaw_note,
)


add(
    decision_id="pawd-2026-davenport-v-churilla",
    case_name="Davenport v. Churilla",
    court="United States District Court for the Western District of Pennsylvania",
    court_code="pawd",
    court_level="federal-district",
    state="PA",
    date_filed="2026-08-12",
    docket_number="3:25-cv-00330-RJC",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court dismissed several claims, allowed amendment on some, and warned Davenport about false authority and allegations.",
    ai_passage="Moreover, the Court acknowledges that Plaintiff’s briefs appear to include at least one AI hallucinated citation. Plaintiff has also made unsupported, and to the extent unsupportable, arguably outrageous allegations about Defendants and their counsel. ... Plaintiff has proffered and the Court has seen no evidence to suggest that either of these allegations is at all true. Plaintiff is sternly warned that he must confirm the accuracy of both asserted facts and law cited in his filings to this Court. The Court will not countenance inaccurate or inflammatory allegations. ... The Court notes that Plaintiff appears to have cited an AI-hallucinated case in support of his argument on this point. See Br. in Opp. at 2 (citing the nonexistent case “Loder v. City of Philadelphia, 838 F.3d 311 (3d Cir. 2016)”). Nonetheless, Plaintiff has also cited relevant caselaw, and indeed, the Court finds that Plaintiff’s interpretation is the better one.",
    cited_authorities=["Loder v. City of Philadelphia, 838 F.3d 311 (3d Cir. 2016)"],
    summary="The Western District of Pennsylvania resolves motions in Dyran Davenport’s civil-rights action and warns him about inaccurate filings. The court identifies nonexistent Loder v. City of Philadelphia as an AI-hallucinated citation in his opposition but still accepts his accrual argument based on other relevant authority.",
    incident={
        "conduct": "Self-represented plaintiff cited nonexistent Loder v. City of Philadelphia in support of his statute-of-limitations argument.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="5f23de9bfc074d8c8353f3a29240c9fef0c4bf63fa09f22d8719ae3d512847a5",
    source_url=source + "/documents/2898/DAVENPORT_v._CHURILLA_et_al_USA_12_August_2026.pdf",
)


add(
    decision_id="mdapp-2026-eyong-v-72-barrow-st-realty",
    case_name="Eyong v. 72 Barrow St. Realty Corp.",
    court="Appellate Court of Maryland",
    court_level="state-appellate",
    state="MD",
    date_filed="2026-08-11",
    citation="2026 WL 2321382",
    docket_number="1910, Sept. Term, 2025",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed judgment for the landlord, taxed costs to appellant, and noted a remand sanctions motion could be considered.",
    ai_passage="72 Barrow has moved for sanctions against Mr. Eyong under Rules 1-341 and 8-504, arguing that his citation to fictional legal authority in his opening brief and his reply brief; the lack of legal authority for his positions; and his failure to prepare a record extract justify an award of reasonable attorneys’ fees and costs. On remand, the circuit court may entertain a motion under Rule 1-341(a) concerning fees incurred by 72 Barrow in defending this appeal. ... JUDGMENT OF THE CIRCUIT COURT FOR MONTGOMERY COUNTY AFFIRMED. COSTS TO BE PAID BY APPELLANT. ... This Court previously entered an order striking large portions of Mr. Eyong's opening brief and his reply brief because it contained fictitious citations to legal authority and inaccurate summaries of the holdings of other cases. We limit our consideration of the issues to the portions of the briefs that have not been stricken.",
    cited_authorities=["Md. Rule 1-341", "Md. Rule 8-504", "Litty v. Becker, 104 Md. App. 370 (1995)"],
    summary="The Appellate Court of Maryland affirms judgment for 72 Barrow St. Realty and taxes costs to Simon Eyong. The per curiam opinion notes earlier orders striking large portions of his self-represented briefs for fictitious legal citations and inaccurate summaries, and leaves a sanctions motion for remand.",
    incident={
        "conduct": "Self-represented appellant’s opening and reply briefs contained fictitious legal citations and inaccurate summaries of case holdings.",
        "outcome": "costs-order",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="3b4f630cf1aaafc13ac36b0ff463b9a3abb1b0d651e4884e64ca68731b537192",
    source_url=source + "/documents/2896/Eyong_v_72_Barrow_St_Realty_Corp_USA_11_August_2026.pdf",
    notes=westlaw_note,
)


add(
    decision_id="arwd-2026-nesbitt-v-trans-union",
    case_name="Nesbitt v. Trans Union, LLC",
    court="United States District Court for the Western District of Arkansas",
    court_code="arwd",
    court_level="federal-district",
    state="AR",
    date_filed="2026-08-11",
    docket_number="5:26-CV-05085-DCF",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court imposed filing restrictions on Nesbitt and denied defendants' request for a Rule 16 conference.",
    ai_passage="Since then, Plaintiff has filed numerous replies without leave of Court, repetitive notices and motions, and at least two motions relying on fabricated cases. ... On July 17, 2026, the undersigned ordered Plaintiff to show cause why he should not be sanctioned under Federal Rule of Civil Procedure 11(b) for citing nonexistent case law in his motions. (Doc. 131). Plaintiff apologized to the Court for relying on artificial intelligence to assist him in conducting legal research and writing pleadings. (Doc. 132). Plaintiff assured the Court that he would never again submit a filing containing fabricated cases. ... Most concerning to the Court is Plaintiff’s reliance on artificial intelligence for legal research and writing, which facilitates rapid filing of numerous documents, many containing fabricated caselaw and misrepresentation of federal rules, within just a few hours. ... IT IS HEREBY ORDERED that the Clerk of Court is DIRECTED to accept no further pleadings or motions from Plaintiff without prior approval from the Court or pursuant to a Court Order.",
    cited_authorities=["Fed. R. Civ. P. 11", "Bass v. General Motors Corp., 150 F.3d 842 (8th Cir. 1998)", "Vallejo v. Amgen, Inc., 903 F.3d 733 (8th Cir. 2018)"],
    summary="The Western District of Arkansas sanctions Nicholas Nesbitt in a consumer-credit case by imposing filing restrictions. The court says he relied on AI for legal research and writing, filed at least two motions with fabricated cases, apologized after a Rule 11 show-cause order, and continued filing improper papers.",
    incident={
        "conduct": "Self-represented plaintiff relied on AI and filed at least two motions with fabricated cases plus many improper filings misrepresenting rules.",
        "outcome": "sanctions",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="cf25b688b7186f5ed8cb5e33fa3aa60601f80c75e29b83fd762d8defc3bf0161",
    source_url=source + "/documents/2840/Nesbitt_v._Transunion_USA_11_AUgust_2026.pdf",
)


add(
    decision_id="pamd-2026-voyton-v-voyton",
    case_name="Voyton v. Voyton",
    court="United States District Court for the Middle District of Pennsylvania",
    court_code="pamd",
    court_level="federal-district",
    state="PA",
    date_filed="2026-08-11",
    citation="2026 WL 2322660",
    docket_number="3:26-cv-27",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court adopted the report and recommendation, dismissed with leave to amend, and required future AI-use affidavits.",
    ai_passage="Prior to addressing the merits of the allegations against Skibitsky, plaintiff is admonished for misrepresenting the law. The statute cited by plaintiff in Paragraph 43 has nothing to do with the alleged conduct by Skibitsky. Rather, the statute referenced requires a person to file a formal written notice of their intent to sue a state governmental unit for personal injury or property damage within six months of the incident. 42 PA. CONS. STAT. § 5522(a). It is improper to misstate the law in this manner. See FED. R. CIV. P. 11 (b). Therefore, plaintiff's future filings in this court will require an affidavit regarding Al usage. ... Courtney's objections also argue about the non-applicability of Younger abstention, the Rooker-Feldman doctrine, and quasi-judicial immunity. However, the R&R issued by Chief Magistrate Judge Bloom in this case did not include a discussion about any of these areas of the law. The only conclusion that may be reached is that the generative Al service used by the plaintiff steered her in the wrong direction. The result is a misleading document and a waste of judicial resources filtering out “ghost arguments” to reach matters on their merits. ... Given the seriousness of the misrepresentations in her complaint and in her objections to the R&R, the plaintiff is forewarned that future unchecked Al usage will result in sanctions, up to and including striking pleadings and dismissing claims with prejudice.",
    cited_authorities=["42 Pa. Cons. Stat. § 5522(a)", "Fed. R. Civ. P. 11", "Younger abstention", "Rooker-Feldman doctrine", "Jones v. Kankakee County Sheriff's Department, 164 F.4th 967 (7th Cir. 2026)"],
    summary="The Middle District of Pennsylvania adopts a recommendation to dismiss Courtney Voyton’s complaint with leave to amend and admonishes her AI use. The memorandum says she misrepresented 42 Pa. Cons. Stat. § 5522 and advanced AI-steered ghost arguments unrelated to the report, requiring future AI-use affidavits.",
    incident={
        "conduct": "Self-represented plaintiff misrepresented a Pennsylvania notice statute and filed AI-steered ghost arguments about doctrines not discussed in the R&R.",
        "outcome": "warning",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="fb560027581915a5bd9774d3eefcc31903cc4df291206c6fbedd19d1f1b2ca53",
    source_url=source + "/documents/2844/Voyton_v._Voyton_USA_11_AUgust_2026.pdf",
    notes=westlaw_note,
)


add(
    decision_id="azctapp-2026-wri-summit-reit-v-kuerschner",
    case_name="WRI Summit REIT LP v. Kuerschner",
    court="Arizona Court of Appeals, Division One",
    court_level="state-appellate",
    state="AZ",
    date_filed="2026-08-10",
    docket_number="1 CA-CV 25-0854",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court dismissed the appeal under ARCAP 25 and awarded appellees reasonable appellate fees and taxable costs.",
    ai_passage="Stefanie’s opening brief does not include a single citation to the record. Her opening brief also consistently misquotes cases and cites cases for propositions either not mentioned or directly contradicted by the case. And one case she cites appears not to exist. ... On page 27, the brief quotes State ex rel. Dep’t of Econ. Sec. v. Burton, 205 Ariz. 27, 30, ¶ 14 (App. 2003) as saying that an appellate court will find an abuse of discretion if a ruling was “manifestly unreasonable, or exercised on untenable grounds, or for untenable reasons.” But Burton contains none of that language. ... On page 48, the brief cites Cruz v. Superior Court (Ramirez), 172 Ariz. 462, 464 (App. 1992). We cannot locate a case with this name in the Arizona appellate courts. ... These citation errors are consistent with the misuse of generative AI. ... Dismissal of Stefanie’s appeal is warranted under ARCAP 25 because she continued to violate ARCAP 13 despite receiving repeated warnings about its requirements and of the consequences for failing to comply.",
    cited_authorities=["State ex rel. Department of Economic Security v. Burton, 205 Ariz. 27 (App. 2003)", "Bennett v. Baxter Group, Inc., 223 Ariz. 414 (App. 2010)", "Brown v. U.S. Fidelity & Guaranty Co., 194 Ariz. 85 (App. 1998)", "Cruz v. Superior Court (Ramirez), 172 Ariz. 462 (App. 1992)", "Takieh v. O'Meara, 252 Ariz. 51 (App. 2021)", "ARCAP 13", "ARCAP 25", "Matter of Estate of Acciavatti, 2026 WL 2041963 (Ariz. App. July 15, 2026)"],
    summary="The Arizona Court of Appeals dismisses Stefanie Kuerschner’s appeal and awards appellate fees and costs. The court says her brief lacked record citations, repeatedly misquoted or misstated cases, included one unlocatable case, and repeated citation problems despite earlier warnings about AI-related errors.",
    incident={
        "conduct": "Self-represented appellant filed briefs with false quotations, unsupported propositions, and an unlocatable Arizona case despite prior warnings.",
        "outcome": "dismissal",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="e9948cde362c2a1864b319d1d8c7be32de3ae42586fe8f77b24b52c011df78f1",
    source_url=source + "/documents/2835/Summit_Reit_USA_10_August_2026.pdf",
)


add(
    decision_id="delch-2026-palumbo-v-palumbo",
    case_name="Palumbo v. Palumbo",
    court="Court of Chancery of the State of Delaware",
    court_level="state-trial",
    state="DE",
    date_filed="2026-08-10",
    docket_number="2024-0661-DH",
    document_type="report-and-recommendation",
    topics=["fabricated-citations", "pro-se-ai-use", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The master recommended trustee removal, denial of respondent's accounting petition, and fee shifting under the bad-faith exception.",
    ai_passage="Moreover, many of the cases cited by Respondent in support of his proposition neither expressly state nor even suggest the statements for which he invokes them. Respondent cites Kuroda v. SPJS Holdings, LLC for the proposition that (1) the proper procedural retort to a confusing claim is a Rule 12(e) motion for a more definite statement, (2) that Delaware courts routinely reject “objections as to style” in pleadings, (3) “[e]ven if the pleading is imperfect, dismissal is not warranted where the defendant is on notice of the claim,” and (4) that Delaware courts evaluate “based on their substance, not the heading under which they appear.” 2009 WL 4345724 (Del. Ch. Dec. 1, 2009). Unfortunately for Respondent, Kuroda never discusses Rule 12(e) nor stands for any of these principles. Respondent even purports to cite Kuroda on two occasions in his post-trial briefing, yet the cited words never appear in the Kuroda decision. Respondent’s invocation of Koninklijke v. Philips Electronics N.V. fares no better. ... Inclusion of fictitious quotations from cases constitutes one of the hallmarks of Artificial Intelligence usage. ... Abuse of AI in litigation filings comprises an “abuse of the adversary system” and is sanctionable conduct. ... Respondent misrepresented law to the court, knowing it was material to the present issues, and failed to correct his statement. ... This concert of action supports my finding that Respondent conducted this litigation with subjective bad faith. As a result, I shift fees and costs to the Petitioners.",
    cited_authorities=["Kuroda v. SPJS Holdings, LLC, 2009 WL 4345724 (Del. Ch. Dec. 1, 2009)", "Koninklijke v. Philips Electronics N.V., 2009 WL 4345724 (Del. Ch. Dec. 1, 2009)", "An v. Archblock, 2025 WL 1024661 (Del. Ch. Apr. 4, 2025)", "Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023)", "Shawe v. Elting, 157 A.3d 142 (Del. 2017)", "Johnston v. Arbitrium (Cayman Islands) Handels AG, 720 A.2d 542 (Del. 1998)"],
    summary="The Delaware Court of Chancery master recommends removing Gregory Palumbo as trustee, denying his accounting petition, and shifting fees. The report says the self-represented disbarred attorney cited Kuroda and Koninklijke for propositions they do not support, treated fictitious quotations as an AI hallmark, and found subjective bad faith.",
    incident={
        "conduct": "Self-represented respondent cited Kuroda and Koninklijke for unsupported propositions and fictitious quotations in post-trial briefing.",
        "outcome": "costs-order",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="930a755ec28bc4223cd88c843d5df429fc4703e8c21409f07baf3a90ffa921cc",
    source_url=source + "/documents/2832/Stephen_J._Palumbo_et_al._v._Gregory_M._Palumbo_USA_10_August_2026.pdf",
)


add(
    decision_id="ilnd-2026-united-states-v-smith",
    case_name="United States v. Smith",
    court="United States District Court for the Northern District of Illinois",
    court_code="ilnd",
    court_level="federal-district",
    state="IL",
    date_filed="2026-08-07",
    docket_number="1:25-cv-05215; 1:21-cr-00703-2",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court denied Smith's § 2255 motion and ordered him to show cause about monetary sanctions for fabricated citations.",
    ai_passage="Smith also cites United States v. Jones, 965 F.3d 149 (2d Cir. 2020) as a case that “reversed a sentence,” Smith’s Br. at 2, but Jones both did not involve challenges to the sentence and affirmed the defendant’s conviction, 965 F.3d at 153. In his reply brief, Jones cites “United States v. Johnson, 605 F.3d 728, 731 (7th Cir. 2010),” for the proposition that prosecutorial exaggeration is improper. Smith’s Reply Br. at 15. But Johnson does not appear to exist. Smith also references United States v. Abbas, 560 F.3d 660 (7th Cir. 2009), for the proposition that a miscalculated guidelines range “infects the entire sentencing process.” Smith’s Reply Br. at 15. Abbas is a real case and discusses sentencing, but it lacks the quote that Smith attributes to the decision. ... One concern remains: potential sanctions against Smith for submitting false citations and quotations. By the Court’s count, Smith falsified entire cases or quotations nearly a dozen times. Falsifying information “undermines the most basic foundations of our judicial system” and “imposes unjust burdens on the opposing party, the judiciary, and honest litigants.” ... So the Court issues a rule for Smith to show cause why he should not be subject to monetary sanctions for the fabricated legal citations. Smith’s response is due on or before September 4, 2026.",
    cited_authorities=["United States v. Aviles-Colon, 536 F.3d 1 (1st Cir. 2008)", "United States v. Jones, 965 F.3d 149 (2d Cir. 2020)", "United States v. Johnson, 605 F.3d 728 (7th Cir. 2010)", "United States v. Abbas, 560 F.3d 660 (7th Cir. 2009)", "Secrease v. Western & Southern Life Insurance Co., 800 F.3d 397 (7th Cir. 2015)", "Fed. R. Civ. P. 11", "Alexander v. United States, 121 F.3d 312 (7th Cir. 1997)", "Smith v. Gilmore, 111 F.3d 55 (7th Cir. 1997)"],
    summary="The Northern District of Illinois denies Darren Smith’s § 2255 motion and issues a sanctions show-cause order. The court identifies a nonexistent Johnson case, false quotations from real cases, and nearly a dozen falsified cases or quotations, then orders Smith to explain why monetary sanctions should not issue.",
    incident={
        "conduct": "Self-represented § 2255 movant submitted nearly a dozen false citations or quotations, including nonexistent United States v. Johnson.",
        "outcome": "pending",
        "actor": "litigant-in-person",
        "monetary_penalty": None,
        "currency": None,
        "ai_tool": None,
    },
    text_sha256="c955205039f0d95c4b69a606af16275229840e03974ccf267085266982dab5c3",
    source_url=source + "/documents/2833/United_States_of_America_v._Smith_USA_7_August_2026.pdf",
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
