import glob
import hashlib
import json

fetched_at = "2026-09-07T13:15:21.976-07:00"
base_url = "https://www.damiencharlotin.com"
secondary_note = "Official source not obtained after CourtListener throttling; read the court-authored document from the Charlotin mirror and marked link-only."

leads = json.load(open("work/leads/t1-slice-1.json", encoding="utf-8"))


def source_url_for(index):
    return base_url + leads[index - 1]["Source"]


def pdf_sha(index):
    matches = glob.glob(f"work/agents/source_docs/{index:03d}-*")
    if len(matches) != 1:
        raise RuntimeError((index, matches))
    return hashlib.sha256(open(matches[0], "rb").read()).hexdigest()


rows = []


def add(**kw):
    row = dict(
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
    row.update(kw)
    rows.append(row)


add(
    decision_id="utd-2026-hack-v-preston",
    case_name="Hack v. Preston",
    court="United States District Court for the District of Utah",
    court_code="utd",
    court_level="federal-district",
    state="UT",
    date_filed="2026-08-07",
    docket_number="4:25-cv-00096-DN",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="ChatGPT",
    disposition="The court required future assistance declarations and cautioned the self-represented defendant about Rule 11 sanctions.",
    ai_passage="Ms. Stephens filed the Declaration on August 3, 2026, and declared, under penalty of perjury, that she had used a generative artificial intelligence (“GenAI”) tool known as ChatGPT. She confirms that she utilized ChatGPT “for assistance with research, organization, drafting, editing, and formatting.” Her candor is appreciated, but necessitates a caution. ... Ms. Stephens has acknowledged using ChatGPT, a GenAI tool that is widely known for its potential to produce inaccurate or fabricated information, commonly referred to as “AI hallucinations.” Although the use of GenAI is not inherently improper, it presents a risk that filings may contain unsupported or inaccurate legal authority if not carefully verified. In her reply memorandum, supporting her motion to dismiss for insufficient service, Ms. Stephens includes a mischaracterized legal assertion relying on a case that was improperly cited. Briefing has not yet crossed the threshold to warrant sanctions, but the risks of AI hallucinations in future filings concern the court. Accordingly, this order serves as a caution that sanctions under Rule 11 of the Federal Rules of Civil Procedure may be imposed if the use of GenAI results in violations of the Federal Rules of Civil Procedure.",
    cited_authorities=["Picon-Diaz v. Bondi, No. 25-9530, 2026 WL 412348 (10th Cir. Feb. 13, 2026)", "Moore v. City of Del City, No. 25-6002, 2025 WL 3471341 (10th Cir. Dec. 3, 2025)", "Hukill v. Oklahoma Native Am. Domestic Violence Coal.", "Fed. R. Civ. P. 11"],
    summary="The District of Utah addresses Jayne Stephens’s declaration that ChatGPT assisted her filings. The order notes a mischaracterized assertion based on an improperly cited Tenth Circuit case, requires future assistance disclosures, and cautions that GenAI-related Rule 11 violations may be sanctioned.",
    incident={"conduct":"Self-represented defendant used ChatGPT and filed a reply with an improperly cited and mischaracterized Tenth Circuit case.","outcome":"warning","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":"ChatGPT"},
    text_sha256=pdf_sha(61),
    source_url=source_url_for(61),
)

add(
    decision_id="nysupct-2026-brown-v-real-estate-capital-of-america",
    case_name="Brown v. Real Estate Capital of America, LLC",
    court="Supreme Court of New York, New York County",
    court_level="state-trial",
    state="NY",
    date_filed="2026-08-07",
    citation="2026 N.Y. Slip Op. 51211(U); 2026 WL 2291696",
    docket_number="Index No. 165361/2025",
    document_type="opinion",
    topics=["fabricated-citations"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court dismissed one claim against two defendants and denied a reply-requested sanctions award over an alleged AI-fabricated quotation.",
    ai_passage="Movants alternatively seek dismissal of plaintiffs' claims and an award of attorney fees, on the additional ground that plaintiffs' opposition assertedly includes a quotation fabricated by artificial intelligence. (NYSCEF No. 30 at 5-6, 9.) Movants do not identify the basis for this court's authority to impose the requested sanction. Movant's request for sanctions is denied. ... Movants have identified a quotation in plaintiffs' opposition papers that does not appear in the case to which the opposition attributes it. But even if this court were to conclude that the challenged quotation is an AI fabrication, rather than the product of ordinary human error, movants' sanctions request is based on a single quotation erroneously attributed to a single case; and the passage of the opposition in which the quotation appears merely provides additional, supplemental support for an argument that rests on properly cited authority. The court is unpersuaded, in these circumstances, that a § 130-1.1 monetary sanction would be warranted.",
    cited_authorities=["22 NYCRR 130-1.1", "Matter of Julien v. Arthur, 2026 NY Slip Op 03308", "Tewari v. Tsoutsouras, 75 NY2d 1 (1989)", "Napoli v. Bern, 171 AD3d 489 (1st Dept 2019)"],
    summary="The New York Supreme Court decides a broker-dispute dismissal motion and denies sanctions requested on reply. The court says plaintiffs attributed a quotation to a case where it did not appear, but even treating it as an AI fabrication did not warrant a monetary sanction.",
    incident={"conduct":"Plaintiffs’ opposition attributed a quotation to a cited case that the court says did not contain it.","outcome":"other","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(62),
    source_url=source_url_for(62),
)

add(
    decision_id="masslandct-2026-in-re-machinsky",
    case_name="In the matter of Machinsky",
    court="Massachusetts Land Court, Plymouth District",
    court_level="state-trial",
    state="MA",
    date_filed="2026-08-07",
    citation="2026 WL 2295072",
    docket_number="26 SBQ 09293 04 - 001 (LER)",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court denied the self-represented defendant's motion to dismiss and warned about fabricated quotations and inaccurate citations.",
    ai_passage="In addition to this false quotation, a review of other legal citations in defendant's filings uncovered several additional inaccuracies and questionable string citations that may be attributable to use of generative artificial intelligence (“AI”) tools or large language models (“LLMs”). On page 3 of defendant's Motion to Recuse, he writes: “The appearance of bias or improper ex parte communications is sufficient to require recusal, even absent a showing of actual bias. Commonwealth v. Eddington, 71 Mass. App. Ct. 138, 144-145 (2008); Commonwealth v. Gogan, 389 Mass. 255, 259 (1983); Commonwealth v. LeBlanc, 475 Mass. 820, 822-823 (2016).” While Eddington and Gogan address the issue of recusal, both affirm that recusal was not required under the applicable standard and circumstances. However, LeBlanc is entirely irrelevant. LeBlanc concerns whether leaving the scene of property damage requires proof that the accident occurred on a public way. It does not mention recusal at all. ... The presence of fabricated quotations and inaccurate citations strongly suggests that defendant used unverified or unreliable sources, such as AI tools or LLMs (like ChatGPT, Claude, Gemini, or Copilot) when drafting his filings. While this does not bear directly on the outcome of this S-case, the court documents this issue on the record to serve as a warning to defendant and other litigants (and an alert to judicial officers in related proceedings) about the serious risks of AI-generated “hallucinations” and false citations when AI tools or LLMs are used without adequate oversight.",
    cited_authorities=["Commonwealth v. Eddington, 71 Mass. App. Ct. 138 (2008)", "Commonwealth v. Gogan, 389 Mass. 255 (1983)", "Commonwealth v. LeBlanc, 475 Mass. 820 (2016)", "Mass. R. Civ. P. 70", "Peterson v. Hopson, 306 Mass. 597 (1940)", "King v. Driscoll, 424 Mass. 1 (1996)"],
    summary="The Massachusetts Land Court denies Robert Machinsky’s self-represented motion to dismiss in a registered-land proceeding. A footnote documents false statutory quotation, irrelevant recusal authority, Rule 70 cases that do not address Rule 70, and warns about AI-generated hallucinations and false citations.",
    incident={"conduct":"Self-represented defendant filed a false statutory quotation and inaccurate or irrelevant case citations in motion papers.","outcome":"warning","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(63),
    source_url=source_url_for(63),
)

add(
    decision_id="ncwd-2026-smith-v-polk-county",
    case_name="Wayne K. Smith, Sr. v. Polk County",
    court="United States District Court for the Western District of North Carolina",
    court_code="ncwd",
    court_level="federal-district",
    state="NC",
    date_filed="2026-08-07",
    docket_number="1:24-cv-00037-MR-WCM",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court discharged an AI-use show-cause order without sanctions but cautioned plaintiff's counsel about future filings.",
    ai_passage="On June 3, 2026, the Court directed counsel for the Plaintiff to show cause in writing as to why she should not be sanctioned for failure to comply with the Court’s Standing Order Regarding the Use of Artificial Intelligence. [Doc. 98 at 15]. The Court specifically directed counsel for the Plaintiff to explain both the origin of the fabricated quotations in briefing she filed with the Court and her repeated failure to provide timely certifications that complied with the Court’s Standing Order. ... Counsel represented that she “does not use AI to conduct legal research,” and that “[t]o ensure the accuracy of citations . . . [she] runs briefs through LexisNexis brief analysis” and fixes any error that appears “alarming.” ... Moreover, counsel has not explained the origin of the fabricated quotations other than to accept responsibility for them and assert that they were not produced by an artificial intelligence program. How such fabricated quotations could have appeared in the Plaintiff’s filings at all therefore remains a mystery. Finally, while counsel asserts that the artificial intelligence program embedded in her practice cannot hallucinate, she has provided no corroboration for that assertion, nor has she even provided the name of the artificial intelligence program that she uses. As a result, the Court finds that counsel’s response has fallen well short of the Court’s expectations. Nevertheless, because counsel has accepted responsibility for the errors in the Plaintiff’s filings, the Court will discharge the Show Cause Order. Counsel for the Plaintiff is cautioned, however, that any similar shortcomings in future filings will result in sanctions.",
    cited_authorities=["Fed. R. Civ. P. 11", "Standing Order Regarding the Use of Artificial Intelligence"],
    summary="The Western District of North Carolina resolves summary-judgment and spoliation motions and discharges an AI show-cause order. The court says plaintiff’s counsel accepted responsibility for fabricated quotations but did not explain their origin or substantiate claims about an unnamed AI program.",
    incident={"conduct":"Plaintiff’s counsel filed briefing with fabricated quotations and did not submit timely AI-use certifications required by the court’s standing order.","outcome":"warning","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(64),
    source_url=source_url_for(64),
)

add(
    decision_id="tnmd-2026-in-re-bfi-waste-systems",
    case_name="In re BFI Waste Systems of Tennessee",
    court="United States District Court for the Middle District of Tennessee",
    court_code="tnmd",
    court_level="federal-district",
    state="TN",
    date_filed="2026-08-06",
    citation="2026 U.S. Dist. LEXIS 175482; 2026 LX 497566",
    docket_number="3:22-cv-00605",
    document_type="order",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court publicly reprimanded attorney Louis W. Ringger III and imposed a $1,500 Rule 11 monetary sanction.",
    ai_passage="On July 30, 2026, the Court ordered several of plaintiff's attorneys to show cause why they should not be sanctioned-under either or both of Rule 11 of the Federal Rules of Civil Procedure and the Court's inherent authority-for filing a document at Doc. No. 293 that contained hallucinated quotations and misleading citations. ... Ringger has confirmed the Court's suspicion that a major factor in the deficiencies at Doc. No. 293-plus others that he identified (Doc. No. 328 at 6)-was the failure to check content generated through tools using artificial intelligence. ... The novel danger with artificial intelligence is how much easier a Rule 11 violation becomes when using it. Submitting false legal authority by conventional means requires either willfulness or a failure by multiple professionals involved in the preparation of a document. ... This is where Ringger fell short, with quotations that did not exist and with legal citations that gave the impression that an argument in his favor had support when it did not. This conduct must be swiftly addressed and deterred. For those reasons, Ringger must be sanctioned. ... Attorney Ringger has violated Rule 11 and is hereby publicly reprimanded through this order. Ringger also is assessed a monetary sanction of $1,500.00, payable to the Clerk of the Court within 30 days after entry of this order.",
    cited_authorities=["Fed. R. Civ. P. 11", "Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023)", "Safe Choice, LLC v. City of Cleveland, 2025 WL 2958211 (N.D. Ohio Oct. 17, 2025)", "Rivera v. Triad Props. Corp., 829 F. Supp. 3d 983 (N.D. Ala. 2026)", "Benjamin v. Costco Wholesale Corp., 779 F. Supp. 3d 341 (E.D.N.Y. 2025)"],
    summary="The Middle District of Tennessee sanctions attorney Louis W. Ringger III after a filing contained hallucinated quotations and misleading citations. The order says unchecked AI-generated content contributed to the deficiencies, publicly reprimands Ringger, and orders him to pay $1,500 to the clerk.",
    incident={"conduct":"Attorney filed a document containing hallucinated quotations and misleading citations after failing to check AI-generated content.","outcome":"sanctions","actor":"lawyer","monetary_penalty":1500,"currency":"USD","ai_tool":None},
    tracker_slug="in-re-bfi-waste-systems",
    text_sha256=pdf_sha(66),
    source_url=source_url_for(66),
)

add(
    decision_id="nd-2026-ali-v-osman",
    case_name="Mohamed Ali v. Saeed Osman",
    court="Supreme Court of North Dakota",
    court_code="nd",
    court_level="state-supreme",
    state="ND",
    date_filed="2026-08-06",
    citation="2026 ND 156",
    docket_number="20260029",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed and remanded, awarding Ali $1,000 in sanctions for citation errors in Osman's opening brief.",
    ai_passage="We conclude Osman’s appeal is not completely frivolous; therefore, we do not sanction under N.D.R.App.P 38 as requested. Nevertheless, while Osman corrected two nonexistent citations, he failed to acknowledge numerous other citations wholly unrelated to the propositions for which they were cited. Under N.D.R.App.P. 28(b)(2) and (7), a party’s brief must provide citations to authorities, and under Rule 28(l), the brief must be accurate and free from irrelevant matters. Under N.D.R.App.P. 13, this court “may take appropriate action against any person failing to perform an act required by rule or court order.” We conclude a sanction is appropriate based on the multiple fictitious or nonexistent citation errors in his opening brief. See City of Dickinson v. Helgeson, 2026 ND 34, ¶¶ 16, 19, 31 N.W.3d 672 (awarding $500 as a sanction for misconduct based on fake or nonexistent legal citations); Stokka v. Stokka, 2026 ND 94, ¶¶ 4-5, 35 N.W.3d 207 (citing Helgeson and imposing costs and attorney’s fees of $1,000, noting the “few legal authorities cited” were “either irrelevant, fictitious, or nonexistent”). We therefore award Ali sanctions in the amount of $1,000.",
    cited_authorities=["N.D.R.App.P. 13", "N.D.R.App.P. 28", "N.D.R.App.P. 38", "City of Dickinson v. Helgeson, 2026 ND 34", "Stokka v. Stokka, 2026 ND 94"],
    summary="The North Dakota Supreme Court affirms and remands in a divorce dispute and separately sanctions self-represented appellant Mojahid Osman. The court says Osman corrected two nonexistent citations but ignored many unrelated authorities, and awards Sara Ali $1,000 for multiple fictitious or nonexistent citation errors.",
    incident={"conduct":"Self-represented appellant filed an opening brief with multiple fictitious or nonexistent citations and citations unrelated to the stated propositions.","outcome":"sanctions","actor":"litigant-in-person","monetary_penalty":1000,"currency":"USD","ai_tool":None},
    text_sha256=pdf_sha(67),
    source_url=source_url_for(67),
)

add(
    decision_id="ohnd-2026-burgess-v-greater-cleveland-rta",
    case_name="Burgess v. Greater Cleveland Regional Transit Authority",
    court="United States District Court for the Northern District of Ohio",
    court_code="ohnd",
    court_level="federal-district",
    state="OH",
    date_filed="2026-08-06",
    docket_number="1:24-cv-01217-PAB",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court warned GCRTA that future frivolous arguments and hallucinated citations could draw sanctions.",
    ai_passage="The Court first addresses GCTRA’s reliance on Shimola. First, “State ex rel. Shimola v. City of Cleveland” is not found at “70 Ohio St.3d 40” as cited by GCRTA. That citation is to State ex rel. Hopkins v. Indus. Comm’n of Ohio, 70 Ohio St.3d 36, 635 N.E.2d 1257 (Ohio 1994). And that case was a workers’ compensation case that has nothing to do with parties pursing inconsistent remedies. Second, “State ex rel. Shimola v. City of Cleveland” is a real case, which can be found at 70 Ohio St.3d 100, 637 N.E.2d 325 (Ohio 1994). But Shimola involved the entry of default judgment and there was no discussion of whether the plaintiff was pursuing inconsistent remedies. ... This citation bears the hallmarks of a hallucinated case citation. Given GCRTA’s other frivolous arguments in their Opposition, the Court strongly suspects that AI was used to draft the Opposition. This undersigned has issued sanctions in the past for Rule 11 violations related to improper AI use. Safe Choice, LLC v. City of Cleveland, No. 1:24-cv-02033-PAB, 2025 U.S. Dist. LEXIS 214410, at *11–12 (N.D. Ohio Oct. 30, 2025). GCRTA is expressly warned that the undersigned will not hesitate to do so again in this case if further briefing contains frivolous arguments and hallucinated case citations. This remains true even if these were merely human errors made without the use of AI.",
    cited_authorities=["State ex rel. Shimola v. City of Cleveland, 70 Ohio St.3d 100 (Ohio 1994)", "State ex rel. Hopkins v. Indus. Comm’n of Ohio, 70 Ohio St.3d 36 (Ohio 1994)", "Safe Choice, LLC v. City of Cleveland, No. 1:24-cv-02033-PAB"],
    summary="The Northern District of Ohio rules on Greater Cleveland Regional Transit Authority’s motion to dismiss and flags a Shimola citation. The court says the cited reporter page points to another case, Shimola does not support the proposition, and future hallucinated citations may be sanctioned.",
    incident={"conduct":"Defendant cited Shimola at a reporter page for a different case and represented Shimola as supporting a proposition it did not discuss.","outcome":"warning","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(68),
    source_url=source_url_for(68),
)

add(
    decision_id="ned-2026-kadlaskar-v-uscis",
    case_name="Kadlaskar v. United States Citizenship and Immigration Services",
    court="United States District Court for the District of Nebraska",
    court_code="ned",
    court_level="federal-district",
    state="NE",
    date_filed="2026-08-06",
    citation="2026 WL 2267773",
    docket_number="4:25CV3025",
    document_type="order",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court awarded EAJA fees and cautioned plaintiff's counsel about a hallucinated Eighth Circuit citation.",
    ai_passage="Plaintiff cites one case in her initial brief in support of the Motion for Attorney Fees. Filing No. 27-1 at 2. Plaintiff quotes Peterson v. U.S. Retirement Board, 785 F.2d 245 (8th Cir. 1986) as follows: Agency action found to be arbitrary and capricious or unsupported by substantial evidence is virtually certain not to have been substantially justified under the Act. Only the most extraordinary special circumstances could permit such an action to be found to be substantially justified under the Act. ... However, that case does not exist. The Court found a portion of this particular quotation in a footnote in Jackson v. Bowen, 807 F.2d 127, n. 5 (8th Cir. 1986) that Plaintiff incorrectly cites in her reply brief. ... While this apparent “hallucinated” case does not necessarily misstate the law, Plaintiff's counsel's reliance on it certainly undermines his credibility with this Court. ... A case of a similar name with a different citation, Peterson v. U.S. Railroad Retirement Board, 780 F.2d 1361 (8th Cir. 1985), does not contain the quoted language. 785 F.2d 245 does not exist. Counsel is cautioned that under the ABA Canons of Professional Ethics he has a duty of candor to the Court to not knowingly make false statements of fact or law to the Court and to correct any such false statement. In addition, counsel has an obligation under Fed. R. Civ. P. 11(b)(2) that the legal authority cited in his filings are based on “an inquiry reasonable the circumstances.” Finally, NECivR 7.1(d)(2) specifically admonishes that “parties are required, if using generative artificial intelligence programs, to verify the contents of their filings. Any filing not properly verified may be stricken and/or sanctions may be imposed on the filing party.”",
    cited_authorities=["Peterson v. U.S. Retirement Board, 785 F.2d 245 (8th Cir. 1986)", "Jackson v. Bowen, 807 F.2d 127 (8th Cir. 1986)", "Peterson v. U.S. Railroad Retirement Board, 780 F.2d 1361 (8th Cir. 1985)", "Fed. R. Civ. P. 11", "NECivR 7.1(d)(2)"],
    summary="The District of Nebraska grants an EAJA fee request and cautions plaintiff’s counsel over a cited Peterson decision. The order says the Eighth Circuit citation does not exist, a similarly named case lacks the quoted language, and Nebraska’s AI rule requires verification.",
    incident={"conduct":"Plaintiff’s counsel cited a nonexistent Eighth Circuit Peterson decision and quoted language that appeared elsewhere in a legislative-history footnote.","outcome":"warning","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(69),
    source_url=source_url_for(69),
)

add(
    decision_id="ctd-2026-booker-v-us-bank",
    case_name="Ulish Kerry Terrace Booker, III v. U.S. Bank National Association",
    court="United States District Court for the District of Connecticut",
    court_code="ctd",
    court_level="federal-district",
    state="CT",
    date_filed="2026-08-05",
    docket_number="25-CV-1205 (VDO)",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="Gemini Pro, Perplexity, Cetient Legal AI, and ChatGPT",
    disposition="The court admonished Booker for violating Rule 11, warned him, and affirmed the bankruptcy court orders on appeal.",
    ai_passage="On June 25, 2026, this Court issued an Order to Show Cause after discovering that Booker III’s briefs were riddled with cases that do not exist, incorrect quotes, and erroneous citations. Specifically, in its Show-Cause Order, the Court identified the following hallucinations: ... BCB Contracting Services, LLC v. United States, 104 B.R. 771, 775 (S.D. Ariz. 2021) [was a] Nonexistent case. Page 771 of Volume 104 of the Bankruptcy Reporter lands in the middle of In re Crouch, a bankruptcy case from West Virginia (104 B.R. 770). ... Mathews v. Dillon, 489 U.S. 567 (1989) [was a] Nonexistent case. Page 567 lands in the middle of a case called Coit Independence Joint Venture v. Federal Sav. and Loan Ins. Corp. (489 U.S. 561). That case explicitly does not discuss due process. The Court could not find any case called “Mathews v. Dillon.” ... In sum, the Court was able to identify at least two inaccurate quotes, four erroneous citations, and six fabricated cases. These hallucinations clearly indicated to the Court the use of generative artificial intelligence (“AI”) in the preparation of these briefs. ... At the hearing, Booker III again apologized to the Court and admitted that he had used several generative AI programs—including Gemini Pro, Perplexity, Cetient Legal AI, and ChatGPT—to prepare his filings. ... For the foregoing reasons, Booker III is ADMONISHED for violating Rule 11 and is WARNED that any future filing containing fabricated authorities, inaccurate quotations, erroneous citations, or other AI-generated hallucinations—or any future failure to conduct a reasonable, human-based verification of authorities before filing—may result in substantially more severe sanctions, including monetary sanctions, the striking of filings, dismissal of claims or appeals, or any other sanction authorized by Rule 11 or the Court’s inherent authority.",
    cited_authorities=["Fed. R. Civ. P. 11", "Fed. R. Bankr. P. 9011", "BCB Contracting Services, LLC v. United States, 104 B.R. 771", "Mathews v. Dillon, 489 U.S. 567", "Coit Independence Joint Venture v. Federal Sav. and Loan Ins. Corp., 489 U.S. 561", "Mata v. Avianca, Inc.", "Mattox"],
    summary="The District of Connecticut admonishes self-represented debtor Ulish Booker in a bankruptcy appeal. After a show-cause hearing, the court finds his briefs contained fabricated cases, erroneous citations, and incorrect quotations produced with Gemini Pro, Perplexity, Cetient Legal AI, and ChatGPT.",
    incident={"conduct":"Self-represented appellant filed briefs with at least two inaccurate quotations, four erroneous citations, and six fabricated cases generated through AI tools.","outcome":"warning","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":"Gemini Pro; Perplexity; Cetient Legal AI; ChatGPT"},
    tracker_slug="in-re-booker-d-conn",
    text_sha256=pdf_sha(70),
    source_url=source_url_for(70),
)

add(
    decision_id="txapp-2026-san-antonio-isd-v-becerra",
    case_name="San Antonio Independent School District v. Becerra",
    court="Texas Court of Appeals, Fourth District",
    court_level="state-appellate",
    state="TX",
    date_filed="2026-08-05",
    docket_number="04-25-00724-CV",
    document_type="opinion",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court reversed and rendered dismissal while admonishing Becerra's counsel about hallucinated authorities.",
    ai_passage="We begin by noting that Becerra’s appellee’s brief cites eight judicial opinions, four of which appear to be hallucinations created by generative artificial intelligence: “Alief Independent School District v. Lozano, 543 S.W.3d 118 (Tex. App.—Houston [14th Dist.] 2018, pet. denied),” cited on page 23 of Becerra’s brief, does not exist. The citation 543 S.W.3d 118 leads to a 2018 opinion from a Missouri court of appeals. ... “Hoffman v. ESD 48, No. 01-14-00676-CV (Tex. App.—Houston [1st Dist.] 2015, pet. denied),” cited on page 22 of Becerra’s brief, does not exist. ... “Neely v. West Orange-Cove Consol. ISD, No. 09-17-00196-CV (Tex. App.—Beaumont 2018, no pet.),” cited on page 21 of Becerra’s brief, does not exist. ... “Cutrer v. Tarrant County College District, 943 F.3d 265 (5th Cir. 2019),” cited on page 21 of Becerra’s brief, appears to be an attempt to cite a Fifth Circuit opinion styled Cutrer v. Tarrant County Local Workforce Development Board, 943 F.3d 265 (5th Cir. 2019). Becerra’s brief states that Cutrer “involved a college student’s expressive conduct and campus restrictions[.]” This is not correct. ... Reliance on fictitious citations and inaccurate representations about the contents of an opposing party’s brief are inconsistent with both of these duties. In light of these hallucinations, we have considered whether to strike Becerra’s brief “and proceed as if [she] had failed to file a brief.” ... However, we will proceed to the merits of this appeal without taking further action on this issue. We nevertheless caution Becerra’s counsel that we will not tolerate similar issues in any future appearances before this court.",
    cited_authorities=["Alief Independent School District v. Lozano, 543 S.W.3d 118", "Hoffman v. ESD 48, No. 01-14-00676-CV", "Neely v. West Orange-Cove Consol. ISD, No. 09-17-00196-CV", "Cutrer v. Tarrant County Local Workforce Development Board, 943 F.3d 265 (5th Cir. 2019)", "Suday v. Suday, 2026 WL 100418", "AGiza v. Franklin, 2025 WL 2058089", "Tex. R. App. P. 38.9"],
    summary="The Texas Fourth Court of Appeals reverses denial of SAISD’s jurisdiction plea and renders dismissal. Before reaching the merits, the court identifies four hallucinated opinions in Becerra’s brief and cautions counsel that similar future issues will not be tolerated.",
    incident={"conduct":"Appellee’s counsel cited three nonexistent Texas appellate opinions and misdescribed a real Fifth Circuit Cutrer employment case as school-law authority.","outcome":"warning","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(71),
    source_url=source_url_for(71),
)

add(
    decision_id="nynd-2026-calenzo-v-waste-management",
    case_name="Calenzo v. Waste Management, Inc.",
    court="United States District Court for the Northern District of New York",
    court_code="nynd",
    court_level="federal-district",
    state="NY",
    date_filed="2026-08-05",
    citation="2026 WL 2253803",
    docket_number="1:24-cv-01499 (AMN/PJE)",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court dismissed one defendant, allowed amendment in part, and warned Calenzo about nonexistent case citations.",
    ai_passage="As a final matter, the undersigned has been unable to locate or verify several of the cases cited by Plaintiff in support of her opposition to Defendant's motion to dismiss. Specifically, Plaintiff's opposition includes citations to at least four nonexistent judicial opinions: LPD New York, LLC v. Adidas Am., Inc., 2020 WL 1501881 (S.D.N.Y. Mar. 30, 2020); Powell v. Monarch Recovery Mgmt., Inc., 2017 WL 102666 (E.D.N.Y. Mar. 23, 2017); Robertson v, Waste Management, Inc., 2019 WL 1238839 (D. Colo. Mar. 18, 2019); and Snyder v. Ply Gem Indus., Inc., 827 F. Supp. 2d 472 (E.D.N.Y. 2011). ... “Although in ‘some circumstances courts will make some allowances for a pro se [p]laintiff's failure to cite to proper legal authority,’ it is ‘no more acceptable for a pro se litigant to submit briefs with fake case citations than it is for a lawyer to do so.’ ” ... Accordingly, the Court directs Plaintiff to refrain from any further use of hallucinated or fabricated case law in submissions before this Court. Plaintiff is further advised that any future filings containing citations to nonexistent cases may result in sanctions, including the striking of such filings from the record, the imposition of filing restrictions, the issuance of monetary sanctions, or the dismissal of this action.",
    cited_authorities=["LPD New York, LLC v. Adidas Am., Inc., 2020 WL 1501881", "Powell v. Monarch Recovery Mgmt., Inc., 2017 WL 102666", "Robertson v. Waste Management, Inc., 2019 WL 1238839", "Snyder v. Ply Gem Indus., Inc., 827 F. Supp. 2d 472", "Hodges v. McGough Enters. LLC, 2026 WL 1470246", "Park v. Kim, 91 F.4th 610 (2d Cir. 2024)"],
    summary="The Northern District of New York grants Waste Management’s dismissal motion, allows limited amendment, and warns self-represented plaintiff Mary-Rose Calenzo. The court identifies at least four nonexistent opinions in her opposition and directs her to stop using hallucinated or fabricated case law.",
    incident={"conduct":"Self-represented plaintiff cited at least four nonexistent judicial opinions in opposition to a motion to dismiss.","outcome":"warning","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(72),
    source_url=source_url_for(72),
)

add(
    decision_id="txwd-2026-cain-v-hyatt",
    case_name="Cain v. Hyatt Corporation",
    court="United States District Court for the Western District of Texas",
    court_code="txwd",
    court_level="federal-district",
    state="TX",
    date_filed="2026-08-05",
    docket_number="1:25-cv-02053-ADA-SH",
    document_type="order",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court ordered plaintiffs' counsel Daniel Miguel Hernandez to appear and show cause under Rule 11.",
    ai_passage="Plaintiffs cited nonexistent case Henry v. Kroger Co., No. 4:19-cv-00630, 2019 WL 6311295 (E.D. Tex. Nov. 25, 2019), in their Response to Defendant’s Motion for Partial Dismissal. Dkt. 9 at 7. Under Rule 11(b), an attorney certifies that legal citations in papers presented to the Court are correct “to the best of the person’s knowledge, information, and belief, formed after an inquiry reasonable under the circumstances.” Plaintiffs’ counsel are “duty-bound to check and certify that all factual contentions and statements of law are warranted and nonfrivolous.” Duncan v. Gridhawk, LLC, No. MO:25-CV-00394-DC, 2025 WL 3515411, at *2 (W.D. Tex. Dec. 6, 2025). The Court held a hearing on July 29, 2026, during which Plaintiffs’ counsel Lino Ochoa represented that he did not prepare or review the response before it was filed. The Court ORDERS Plaintiffs’ other attorney of record, Daniel Miguel Hernandez, to appear and show cause under Rule 11(c)(3) why the conduct described in this Order has not violated Rule 11(b) at 2 p.m. Wednesday, August 19, 2026 in Courtroom 6 on the Sixth Floor of the United States Courthouse, 501 W. 5th Street, Austin, Texas 78701.",
    cited_authorities=["Henry v. Kroger Co., No. 4:19-cv-00630, 2019 WL 6311295", "Fed. R. Civ. P. 11", "Duncan v. Gridhawk, LLC, No. MO:25-CV-00394-DC, 2025 WL 3515411 (W.D. Tex. Dec. 6, 2025)"],
    summary="The Western District of Texas issues a show-cause order in Cain v. Hyatt. The order says plaintiffs cited nonexistent Henry v. Kroger authority in a dismissal response and requires attorney Daniel Miguel Hernandez to appear under Rule 11(c)(3).",
    incident={"conduct":"Plaintiffs’ response cited nonexistent Henry v. Kroger Co. authority in opposing partial dismissal.","outcome":"pending","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(73),
    source_url=source_url_for(73),
)

add(
    decision_id="ctd-2026-barteca-v-tacobarn",
    case_name="Barteca Holdings LLC v. Tacobarn Newtown LLC",
    court="United States District Court for the District of Connecticut",
    court_code="ctd",
    court_level="federal-district",
    state="CT",
    date_filed="2026-08-04",
    docket_number="26-CV-250 (VDO)",
    document_type="order",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="Open Law; Claude; Chat GPT",
    disposition="The court imposed a $3,500 Rule 11 sanction, referred counsel to the Grievance Committee, and required corrected briefing.",
    ai_passage="This Order addresses the Court’s previously issued Order to Show Cause concerning defense counsel Hilary Miller’s use of unverified generative artificial intelligence (“AI”) in this matter. Having considered counsel’s written response to the Order to Show Cause and his representations made at the show-cause hearing, the Court concludes that sanctions are warranted and imposes the sanctions set forth below. ... Upon review of the Motions, the Court discovered numerous case quotes that do not exist, erroneous citations, and misrepresentations of the law. ... On June 25, 2026, the Court held a show-cause hearing, at which Attorney Miller reiterated those representations and further explained the circumstances under which the AI-generated material was incorporated into his briefing. Attorney Miller clarified that this matter is the first and only matter in which he utilized artificial intelligence. As for his writing process, Attorney Miller explained that he first wrote the brief himself conventionally. Then, in an attempt to improve it, he used a tool called Open Law, which he paid for, for suggestions on arguments and additional cases. He also used Claude and Chat GPT for additional suggestions. Concerned about the risk of AI hallucinations, Attorney Miller then cross-checked the citations in the brief to determine whether they existed and were cited correctly ... Balancing these considerations, the Court concludes that a monetary sanction of $3,500, together with a referral of this matter to the Grievance Committee pursuant to Local Rule 83(c)(2), is appropriate. ... For the foregoing reasons, the Court concludes that Attorney Miller’s submission of unverified AI-generated legal authorities warrants sanctions under Rule 11 and, accordingly, imposes a $3,500 monetary sanction and refers this matter to the Grievance Committee pursuant to Local Rule 83(c)(2).",
    cited_authorities=["Ashcroft v. Iqbal, 556 U.S. 662 (2009)", "Streetwise Maps, Inc. v. VanDam, Inc., 159 F.3d 739 (2d Cir. 1998)", "Landscape Forms, Inc. v. Columbia Cascade Co., 113 F.3d 373 (2d Cir. 1997)", "Yurman Design, Inc. v. PAJ, Inc., 262 F.3d 101 (2d Cir. 2001)", "Chambers v. Time Warner, Inc., 282 F.3d 147 (2d Cir. 2002)", "Friedl v. City of New York, 210 F.3d 79 (2d Cir. 2000)", "Fonte v. Board of Managers of Continental Towers Condominium, 848 F.2d 24 (2d Cir. 1988)", "Cortec Industries, Inc. v. Sum Holding L.P., 949 F.2d 42 (2d Cir. 1991)", "Fed. R. Civ. P. 11", "D. Conn. L. Civ. R. 83(c)(2)"],
    summary="The District of Connecticut sanctions defense counsel Hilary Miller in a trademark dispute. The order says Miller used Open Law, Claude, and ChatGPT, submitted unverified AI-generated legal authorities with nonexistent quotations and erroneous citations, and must pay $3,500 with a grievance referral.",
    incident={"conduct":"Defense counsel used Open Law, Claude, and ChatGPT and filed motions with nonexistent case quotes, erroneous citations, and misstatements of law.","outcome":"sanctions","actor":"lawyer","monetary_penalty":3500,"currency":"USD","ai_tool":"Open Law; Claude; Chat GPT"},
    tracker_slug="barteca-v-tacobarn",
    text_sha256=pdf_sha(74),
    source_url=source_url_for(74),
)

add(
    decision_id="txsd-2026-cristancho-v-swbc-mortgage",
    case_name="Cristancho v. SWBC Mortgage Corporation",
    court="United States District Court for the Southern District of Texas",
    court_code="txsd",
    court_level="federal-district",
    state="TX",
    date_filed="2026-08-04",
    docket_number="3:24-cv-00110",
    document_type="report-and-recommendation",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The magistrate judge recommended granting defendants' summary-judgment motion and admonished plaintiffs' counsel over fabricated authorities.",
    ai_passage="Plaintiffs cite Pointe West Center, LLC v. It’s Alive, Inc., 796 S.W.2d 830, 838–39 (Tex. App.—Houston [1st Dist.] 1990, writ denied), and Motten v. Chase Home Financial, 821 F. Supp. 2d 988, 1008 (S.D. Tex. 2011), for the proposition that a cause of action for wrongful initiation of foreclosure proceedings exists. Pointe West is a fabricated cite, and Motten states that “courts in Texas do not recognize an action for attempted wrongful foreclosure.” 831 F. Supp. 2d at 1007 (quotation omitted). Plaintiffs’ counsel is reminded that every submission to the court represents that “the claims, defenses, and other legal contentions” within “are warranted by existing law or by a nonfrivolous argument for extending, modifying, or reversing existing law or for establishing new law.” Fed. R. Civ. P. 11(b)(2). “[S]ubmitting a brief riddled with fabricated quotations and assertions is . . . an abuse [of the judicial process].” Fletcher v. Experian Info. Sols., Inc., 168 F.4th 231, 234 (5th Cir. 2026). ... Plaintiffs argue that “the prior material breach doctrine does not bar a plaintiff’s contract claim where the defendant’s own breach caused or contributed to the plaintiff’s non-performance.” Dkt. 34 at 13. In support, Plaintiffs cite Restatement (Second) of Contracts § 237 cmt. d (1981), and Tractebel Energy Marketing, Inc. v. E.I. Du Pont De Nemours & Co., 118 F. Supp. 2d 737, 744 (S.D. Tex. 2000). The use of these citations is either the product of incredibly shoddy legal work or an outright misrepresentation to the court. The Tractebel case is fabricated, and the referenced Restatement provision says nothing of the sort.",
    cited_authorities=["Pointe West Center, LLC v. It’s Alive, Inc., 796 S.W.2d 830", "Motten v. Chase Home Financial, 821 F. Supp. 2d 988", "Fed. R. Civ. P. 11", "Fletcher v. Experian Info. Sols., Inc., 168 F.4th 231 (5th Cir. 2026)", "Restatement (Second) of Contracts § 237", "Tractebel Energy Marketing, Inc. v. E.I. Du Pont De Nemours & Co., 118 F. Supp. 2d 737"],
    summary="The Southern District of Texas magistrate judge recommends summary judgment for SWBC Mortgage and Cenlar. The recommendation says plaintiffs’ counsel cited fabricated Pointe West and Tractebel cases, misused other authorities, and is reminded of Rule 11 duties.",
    incident={"conduct":"Plaintiffs’ counsel cited fabricated Pointe West and Tractebel cases and invoked a Restatement provision for a proposition it did not contain.","outcome":"warning","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(75),
    source_url=source_url_for(75),
)

add(
    decision_id="moctapp-2026-whitehead-v-moore",
    case_name="Whitehead v. Moore",
    court="Missouri Court of Appeals, Western District",
    court_level="state-appellate",
    state="MO",
    date_filed="2026-08-04",
    docket_number="WD88216",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court dismissed the self-represented father's appeal for failure to provide a required record.",
    ai_passage="Therefore, we dismiss Father’s appeal for failure to provide this Court with the required record on appeal necessary to resolve the questions raised in his appeal. ... There are numerous other briefing deficiencies with Father’s appellate brief that would also independently support dismissal of Father’s appeal. ... Father’s brief includes two citations to cases that do not exist in the reporter he cites, and he additionally cites one case for a legal proposition that cannot be reasonably inferred from that case. Citing non-existent case law or misrepresenting the holdings of an existing case is “a flagrant violation of the duties of candor Appellant owes to this Court,” which warrants dismissal of an appeal. See Kruse v. Karlen, 692 S.W.3d 43, 52 (Mo. App. E.D. 2024).",
    cited_authorities=["Kruse v. Karlen, 692 S.W.3d 43 (Mo. App. E.D. 2024)", "Missouri Rule 84.04"],
    summary="The Missouri Court of Appeals dismisses self-represented father Zackery Moore’s family-access appeal because he did not supply the record needed for review. A footnote says his brief also contained two nonexistent reporter citations and one misrepresented holding, independently supporting dismissal.",
    incident={"conduct":"Self-represented appellant’s brief cited two cases that did not exist in the cited reporters and misrepresented another case’s holding.","outcome":"dismissal","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(76),
    source_url=source_url_for(76),
)

add(
    decision_id="nced-2026-forney-v-township-of-cary",
    case_name="Forney v. Township of Cary, North Carolina",
    court="United States District Court for the Eastern District of North Carolina",
    court_code="nced",
    court_level="federal-district",
    state="NC",
    date_filed="2026-08-03",
    citation="2026 WL 2439988",
    docket_number="5:25-CV-00738-M",
    document_type="report-and-recommendation",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court recommended dismissal, ordered counsel to pay Cary's response fees, and referred the matter to the North Carolina State Bar.",
    ai_passage="The record provides clear and convincing evidence that Colantonio engaged in conduct that justifies imposing sanctions under the court's inherent authority. First, Colantonio provided erroneous case citations repeatedly even after being warned. Colantonio has admitted that the citation was erroneous. ... Thus the record establishes by clear and convincing evidence that Colantonio knowingly submitted a pleading containing fabricated authority and citations on multiple occasions and even after being warned. This conduct constitutes an abuse of the judicial process that is utterly inconsistent with the orderly administration of justice and undermines the integrity of the judicial process. Colantonio's repeated conduct also establishes that he acted in bad faith when he submitted his response. Thus the court may sanction Colantonio under its inherent authority. ... The record in this case shows that a significant sanction is warranted. The submission of fabricated authority imposes substantial costs on the opposing party, the court, and the judicial process. ... After considering Colantonio's conduct and the need to deter similar conduct from him and other litigants, the court orders that he pay the attorney's fees incurred by the Town of Cary as a result of his brief. These fees include, but are not limited to, drafting its reply brief and attending the show cause hearing. ... Further, the Clerk of Court is directed to send a copy of this order and a transcript of the April 16, 2026 hearing (D.E. 18) to the North Carolina State Bar for whatever action it deems appropriate, including consideration of whether disciplinary or disability-related measures are warranted.",
    cited_authorities=["United States v. Shaffer Equipment Co., 11 F.3d 450 (4th Cir. 1993)", "Six v. Generations Federal Credit Union, 891 F.3d 508 (4th Cir. 2018)", "Jimenez v. DaimlerChrysler Corp., 269 F.3d 439 (4th Cir. 2001)", "Roadway Express, Inc. v. Piper, 447 U.S. 752 (1980)", "Chambers v. NASCO, Inc., 501 U.S. 32 (1991)", "In re McDonald, 489 U.S. 180 (1989)"],
    summary="The Eastern District of North Carolina recommends dismissal of Damon Forney’s employment case as untimely and sanctions attorney Lucas Colantonio. The order says Colantonio repeatedly submitted fabricated authority after a warning, must pay Cary’s response fees, and is referred to the North Carolina State Bar.",
    incident={"conduct":"Counsel repeatedly submitted fabricated authority and erroneous citations after a prior warning in related litigation.","outcome":"costs-order","actor":"lawyer","monetary_penalty":None,"currency":None,"ai_tool":None},
    tracker_slug="forney-v-township-of-cary",
    text_sha256=pdf_sha(78),
    source_url=source_url_for(78),
)

add(
    decision_id="alnd-2026-perry-v-social-security-administration",
    case_name="Perry v. Social Security Administration, Commissioner",
    court="United States District Court for the Northern District of Alabama",
    court_code="alnd",
    court_level="federal-district",
    state="AL",
    date_filed="2026-08-03",
    docket_number="2:26-cv-00048-AMM",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court dismissed Perry's claim without prejudice, denied her TRO-related motions, and warned against fabricated citations.",
    ai_passage="The SSA raised an issue of “fabricated citations” and misrepresentations in Ms. Perry’s motion for a temporary restraining order. See Doc. 30; Doc. 33 at 23–24. The court is aware that Ms. Perry has been warned by another court against such practices. The court warns Ms. Perry that fabricated citations and misrepresentations will not be tolerated. This is the only warning Ms. Perry will receive. Ms. Perry should expect that any future instances of fabricated citations and misrepresentations, in this case or any case in this court, will be sanctioned.",
    cited_authorities=["Doc. 30", "Doc. 33"],
    summary="The Northern District of Alabama dismisses Domeneque Perry’s Social Security claim without prejudice and denies TRO and amendment motions. The court notes the Commissioner raised fabricated citations and misrepresentations in Perry’s TRO motion and warns this is Perry’s only warning before sanctions.",
    incident={"conduct":"Self-represented plaintiff’s temporary-restraining-order motion drew an SSA objection for fabricated citations and misrepresentations.","outcome":"warning","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(79),
    source_url=source_url_for(79),
)

add(
    decision_id="ohioctapp-2026-state-v-davis",
    case_name="State v. Davis",
    court="Ohio Court of Appeals, Seventh Appellate District",
    court_level="state-appellate",
    state="OH",
    date_filed="2026-08-03",
    citation="2026-Ohio-2993",
    docket_number="25 CO 0050",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed Davis's speeding conviction and taxed costs against him.",
    ai_passage="A further problem on appeal is that Appellant has filed a non-conforming brief, well outside of the limits set by the Rules of Appellate Procedure. The brief is set in a small font, single spaced, and if converted to 12-point font and double-spaced would well exceed 35 pages and 9,000 words (the word count is over 12,000). Appellant has also notified this Court that he used generative Artificial Intelligence (AI) to create his brief. Since Appellant is not an attorney, he cannot determine whether AI has produced viable legal arguments. Since he has not tested most of his arguments at the trial court level, he seeks for this Court to determine the legitimacy of his AI documents and arguments. ... It is not clear what argument Appellant is trying to make regarding the Sanchez case, cited above. The issue in Sanchez was whether the defendant was being held solely on the pending charge. More specifically, the question in that case was whether a detainer filed by the Bureau of Immigration and Customs Enforcement nullified the triple count provision of R.C. 2945.71(E). This is not an issue in the instant matter. Sanchez does not discuss the topic Appellant raises and does not mention indefinite tolling. His citation to this immaterial case may have been as a result of a “hallucination” by Appellant’s AI queries.",
    cited_authorities=["State v. Sanchez, 2006-Ohio-4478", "R.C. 2945.71(E)", "State ex rel. Neil v. French, 2018-Ohio-2692"],
    summary="The Ohio Seventh District affirms Jacob Davis’s speeding conviction. The opinion says Davis disclosed using generative AI for his nonconforming brief, and a cited Sanchez case does not discuss the indefinite-tolling proposition he raised, possibly reflecting an AI hallucination.",
    incident={"conduct":"Self-represented appellant used AI and cited Sanchez for an indefinite-tolling proposition the opinion did not discuss.","outcome":"other","actor":"litigant-in-person","monetary_penalty":None,"currency":None,"ai_tool":None},
    text_sha256=pdf_sha(80),
    source_url=source_url_for(80),
)

existing = set()
out_path = "work/agents/decisions-t1-s1.jsonl"
try:
    with open(out_path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                existing.add(json.loads(line)["decision_id"])
except FileNotFoundError:
    pass

with open(out_path, "a", encoding="utf-8") as f:
    added = 0
    for row in rows:
        if row["decision_id"] in existing:
            continue
        f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
        added += 1
print(added)
