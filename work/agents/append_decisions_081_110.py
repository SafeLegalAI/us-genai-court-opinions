import glob
import hashlib
import json
from pathlib import Path

fetched_at = "2026-09-07T15:05:00-07:00"
base_url = "https://www.damiencharlotin.com"
secondary_note = "Official source not obtained within allotted attempts; read the court-authored document from the Charlotin mirror and marked link-only."

leads = json.load(open("work/leads/t1-slice-1.json", encoding="utf-8"))
OFFICIAL_SOURCES = {
    101: "https://ilcourtsaudio.blob.core.windows.net/antilles-resources/resources/23d7df84-ed51-48df-8477-3a6872db40d5/Scott%20v.%20IL%20Human%20Rights%20Commn%202026%20IL%20App%20(1st)%20251462.pdf",
}


def source_url_for(index):
    if index in OFFICIAL_SOURCES:
        return OFFICIAL_SOURCES[index]
    src = leads[index - 1]["Source"]
    return src if src.startswith("http") else base_url + src


def pdf_sha(index):
    matches = glob.glob(f"work/agents/source_docs/{index:03d}-*")
    if len(matches) != 1:
        raise RuntimeError((index, matches))
    return hashlib.sha256(open(matches[0], "rb").read()).hexdigest()


rows = []


def add(index, **kw):
    row = dict(
        citation=None,
        docket_number=None,
        court_code=None,
        state=None,
        ai_tool_named=None,
        incident=None,
        tracker_slug=None,
        courtlistener_url=None,
        text_sha256=pdf_sha(index),
        archive_url=None,
        notes=secondary_note,
        lead_source=["charlotin-cc0"],
        fetched_at=fetched_at,
        verification="link-only",
        source_url=source_url_for(index),
    )
    row.update(kw)
    rows.append(row)


add(
    81,
    decision_id="pasuperct-2026-bisher-v-civic",
    case_name="Bisher v. Civic",
    court="Superior Court of Pennsylvania",
    court_level="state-appellate",
    state="PA",
    date_filed="2026-08-03",
    docket_number="2582 EDA 2025",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed summary judgment and admonished self-represented appellants over nonexistent and misleading appellate citations.",
    ai_passage="Appellants cite to two cases—one which is non-existent—for the rules that summary judgment may not be entered where discovery is incomplete or credibility issues remain. See id. at 40 (citing Gibson v. Bicknell, 668 A.2d 1370 (Pa. Super. 1995), and Washington v. Baxter, 719 A.2d 733 (Pa. 1998)). ... This cited case does not exist.Elsewhere in their brief, Appellants cite to Gonzalez v. Procaccio Bros. Trucking Co., 268 A.3d 528 (Pa. Super. 2021), and In re Estate of Pittman, 636 A.2d 1166 (Pa. Super. 1994), which also do not exist. We remind Appellants that litigants must cite to “pertinent” authority. See Pa.R.A.P. 2119(a). Such misstatements and/or misrepresentations, if further disseminated, undermine the accuracy and reliability of the law Appellants purport to reference. Moreover, we remind Appellants that we may dismiss an appeal if the brief defects are substantial. See Pa.R.A.P. 2101.",
    cited_authorities=["Gibson v. Bicknell, 668 A.2d 1370 (Pa. Super. 1995)", "Gonzalez v. Procaccio Bros. Trucking Co., 268 A.3d 528 (Pa. Super. 2021)", "In re Estate of Pittman, 636 A.2d 1166 (Pa. Super. 1994)", "Pa.R.A.P. 2119(a)", "Pa.R.A.P. 2101"],
    summary="The Superior Court of Pennsylvania affirms summary judgment in a medical-malpractice appeal. A footnote identifies three cited cases that do not exist, reminds the self-represented appellants that authority must be pertinent, and warns that substantial brief defects can justify dismissal.",
    incident={"conduct":"Self-represented appellants cited three nonexistent Pennsylvania cases and other misrepresented authority in an appellate brief.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    82,
    decision_id="txwd-2026-moore-v-aldridge-pite",
    case_name="Moore v. Aldridge Pite LLP",
    court="United States District Court for the Western District of Texas",
    court_code="txwd",
    court_level="federal-district",
    state="TX",
    date_filed="2026-08-03",
    docket_number="MO:25-CV-00326-DC",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court dismissed the final remaining claims without prejudice and expressly warned plaintiffs about future Rule 11 compliance.",
    ai_passage="They are the latest installment in a sustained series of filings marked by misstatements of law, mischaracterizations of the record, fabricated quotations, and demands untethered to any rule of procedure. ... Although Plaintiffs certified that they verified each citation contained in those objections (Doc. 76 at 26), the Court identified multiple instances in which Plaintiff attributed propositions to cases that did not support them. ... That motion attributed purported quotations to multiple judicial decisions in which the quoted language does not appear. It also included several misstatements of law and case holdings. ... This conduct is unacceptable. When a litigant places quotation marks around words and attributes those words to a judicial decision, they represent to the Court that the decision contains those words. When the decision does not, the filing misleads the Court. Repeatedly presenting invented quotations and inaccurate descriptions of authority consumes scarce judicial resources, burdens opposing parties, and undermines the adjudicative process. ... Whether those defects in Plaintiffs’ submissions were generated by artificial intelligence, copied from an unreliable source, or created by Plaintiffs themselves is immaterial. A litigant may use whatever tools it chooses, but it may not file misleading legal arguments. ... The Court declines at this time to initiate sanctions proceedings or impose filing restrictions. However, Plaintiffs are expressly WARNED that every future submission to this Court must comply fully with Federal Rule of Civil Procedure 11. Before filing any paper, Plaintiffs must personally verify that every cited authority exists, that every quotation appears in the cited source, that every description of the record is accurate, and that every legal contention is warranted by existing law or a nonfrivolous argument for changing it.",
    cited_authorities=["Fed. R. Civ. P. 11"],
    summary="The Western District of Texas adopts an R&R and dismisses the remaining defendant without prejudice. The order catalogs repeated invented quotations, unsupported case descriptions, and possible AI use, then warns the self-represented plaintiffs to verify all authorities and quotations in future filings.",
    incident={"conduct":"Self-represented plaintiffs repeatedly filed invented quotations, unsupported case descriptions, and legal misstatements after prior warnings.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    83,
    decision_id="cacd-2026-jabbari-v-omidvar",
    case_name="Jabbari v. Omidvar",
    court="United States District Court for the Central District of California",
    court_code="cacd",
    court_level="federal-district",
    state="CA",
    date_filed="2026-08-03",
    citation="2026 WL 2227350",
    docket_number="2:26-cv-03553-FLA (DTBx)",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court struck improper filings, restricted further filings, and ordered Jabbari to show cause why sanctions should not issue.",
    ai_passage="The court also ORDERS Plaintiff to Show Cause (“OSC”) in writing, on or before August 17, 2026, why sanctions should not be imposed under Federal Rule of Civil Procedure Rule 11 and the court's inherent authority, for Plaintiff's submission of frivolous and vexatious filings and/or false and fabricated legal citations. ... Plaintiff's filings bear hallmarks often associated with the use of generative AI programs, including the prompts Plaintiff used to generate results from these programs, tonal and textual inconsistencies, and the inclusion of fabricated and unsubstantiated (commonly referred to as “hallucinated”) legal authorities. ... Plaintiff is reminded that generative AI tools are known to “hallucinate” and fabricate legal citations and case law that do not exist or are incorrectly applied. Plaintiff bears the duty to verify the accuracy, existence, and validity of every legal citation and reference submitted to the court, and is warned that the submission of false, fabricated, and AI “hallucinated” legal authorities will result in the imposition of sanctions, which could include: (a) monetary sanctions to compensate Defendants for any and all attorney's fees and costs reasonably incurred in responding to documents that contain such statements; (b) monetary sanctions exceeding $1,000 payable to the court; and sanctions under Rule 11(b).",
    cited_authorities=["Fed. R. Civ. P. 11"],
    summary="The Central District of California manages a transferred pro se case by striking improper filings and imposing filing limits. The court says Jabbari’s papers contain AI hallmarks and fabricated legal authorities, then orders him to show cause why Rule 11 or inherent-authority sanctions should not issue.",
    incident={"conduct":"Self-represented plaintiff filed vexatious papers with fabricated and unsubstantiated legal authorities showing hallmarks of generative-AI use.", "outcome":"pending", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    84,
    decision_id="ord-2026-united-states-v-karnezis",
    case_name="United States v. Karnezis",
    court="United States District Court for the District of Oregon",
    court_code="ord",
    court_level="federal-district",
    state="OR",
    date_filed="2026-07-31",
    citation="2026 WL 2212298",
    docket_number="3:23-cr-00067-IM",
    document_type="order",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court granted in part a suppression motion and admonished Williams's counsel for a non-existent quotation in briefing.",
    ai_passage="Perhaps recognizing that Smith does not support his argument, Williams resorts to providing a non-existent quotation from the case: “The Ninth Circuit held that officers cannot ‘prevent a suspect from making an unambiguous request for counsel by cutting him off.’ ” Reply, ECF 172 at 9. This Court admonishes Williams's counsel for misquoting Smith, but at the same time, this Court does not endorse Agent Pasquale's interruption of Williams. ... At the hearing, Williams's counsel stated that this error was not a result of using generative AI but rather an inadvertent mistake. This Court reminds Williams's counsel that he is responsible for not only his own contributions but also his client's contributions to any of his submissions.",
    cited_authorities=["United States v. Smith, 860 F.2d 1533 (9th Cir. 1988)", "McNeil v. Wisconsin, 501 U.S. 171 (1991)", "United States v. Rodriguez, 518 F.3d 1072 (9th Cir. 2008)", "Miranda v. Arizona, 384 U.S. 436 (1966)"],
    summary="The District of Oregon partially suppresses statements in a criminal case. In resolving the Miranda arguments, the court notes that defense briefing supplied a quotation that does not appear in Smith and admonishes counsel, while recording counsel’s statement that the mistake was not caused by generative AI.",
    notes=secondary_note + " The court records counsel's statement that the non-existent quotation was an inadvertent mistake rather than generative AI.",
    incident={"conduct":"Defense counsel submitted a non-existent quotation from a Ninth Circuit Miranda case in suppression briefing.", "outcome":"warning", "actor":"lawyer", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    85,
    decision_id="nysd-2026-santana-v-shook-hardy-bacon",
    case_name="Santana v. Shook Hardy & Bacon",
    court="United States District Court for the Southern District of New York",
    court_code="nysd",
    court_level="federal-district",
    state="NY",
    date_filed="2026-07-31",
    citation="2026 WL 2212887",
    docket_number="25-CV-5088 (RA)",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court compelled arbitration, stayed the case, and cautioned Santana that future inaccurate citations may bring sanctions.",
    ai_passage="As a final matter, the Court addresses Defendants’ concern that Plaintiff's opposition brief contained citations and quotations to non-existent case authority, which they attribute to his use of artificial intelligence (“AI”). Dkt. No. 55 (“Forrest Defs. Repl.”) at 1–2; Dkt. No. 58 (“Shook Defs. Repl.”) at 1. The Shook Defendants urge the Court to sanction Plaintiff, including by striking his opposition and treating the motions as unopposed. ... Forrest Defendants do not seek sanctions pursuant to Rule 11 given that Plaintiff is pro se, but express frustration at the unnecessary resources they spent verifying his inaccurate citations. ... Whether this Court has adopted an individual rule regarding the use of AI or not, Rule 11 requires parties to certify that their legal contentions “are warranted by existing law.” Fed. R. Civ. P. 11. Even though he is proceeding pro se, Plaintiff “is required to comply with the Local Rules and Federal Rules of Civil Procedure.” McClellon v. Rickard, 2026 WL 686499, at *9 (S.D.N.Y. Mar. 11, 2026). Accordingly, whether the deficiencies in Plaintiff's filings stem from his use of AI or some other source, the Court cautions him that future submissions to any court must contain only accurate citations and representations. If they do not—because of AI hallucinating case citations or otherwise—he may be sanctioned, id., although the Court declines to do so now.",
    cited_authorities=["Fed. R. Civ. P. 11", "McClellon v. Rickard, 2026 WL 686499 (S.D.N.Y. Mar. 11, 2026)"],
    summary="The Southern District of New York compels arbitration and stays a pro se employment case. The opinion separately addresses defendants’ concern that Santana’s opposition used nonexistent case authority attributed to AI, declines sanctions for now, and warns that future inaccurate citations may be sanctioned.",
    incident={"conduct":"Self-represented plaintiff filed an opposition brief allegedly containing citations and quotations to nonexistent case authority.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    86,
    decision_id="mied-2026-al-ali-v-cvs-pharmacy",
    case_name="Al-Ali v. CVS Pharmacy, Inc.",
    court="United States District Court for the Eastern District of Michigan",
    court_code="mied",
    court_level="federal-district",
    state="MI",
    date_filed="2026-07-31",
    citation="2026 WL 2211604",
    docket_number="24-13046",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court overruled objections and warned Al-Ali that future factitious citations may lead to struck filings or monetary sanctions.",
    ai_passage="First, Plaintiff's objections contain numerous factitious citations. For example, Plaintiff quotes 9 U.S.C. § 5, but the quote is inaccurate. Additionally, Plaintiff purportedly cites cases such as “Cottman Transmission Sys., Inc. v. Metro. Pontiac GMC, Inc., 351 F. Supp. 2d 343, 347 (E.D. Pa. 2004)” and “McMahon v. RMS Electronics, Inc., 951 F. Supp. 923, 925 (S.D.N.Y. 1997),” but these cases do not exist. ... As set forth previously in this opinion, Plaintiff's objections contained factitious citations. These factitious citations appear to be created by generative artificial intelligence (“AI”) tools. ... Nevertheless, “a pro se litigant must not provide the Court with erroneous and factitious citations and has an obligation to review documents filed with the Court to make certain they are scrupulously accurate.” ... The Court warns Plaintiff that, in the future, even one factitious citation will not be tolerated and that she may be sanctioned if future filings contain factitious citations, including but not limited to striking of filings or monetary penalties. The Court warns Plaintiff that factitious citations include case citations to nonexistent cases, but also case citations that, while real, do not stand for their asserted proposition. Plaintiff has an obligation to ensure that she does not submit any factitious citations in the future.",
    cited_authorities=["9 U.S.C. § 5", "Cottman Transmission Sys., Inc. v. Metro. Pontiac GMC, Inc., 351 F. Supp. 2d 343 (E.D. Pa. 2004)", "McMahon v. RMS Electronics, Inc., 951 F. Supp. 923 (S.D.N.Y. 1997)", "United States v. Hayes, 763 F. Supp. 3d 1054 (E.D. Cal. 2025)", "Everett J. Prescott, Inc. v. Beall, 2025 WL 2084353 (D. Me. July 24, 2025)", "Whiting v. City of Athens, 170 F.4th 455 (6th Cir. 2026)", "Ali v. IT People Corp., Inc., 2025 WL 2682622 (E.D. Mich. Sept. 19, 2025)"],
    summary="The Eastern District of Michigan overrules arbitration-related objections and warns Natashah Al-Ali. The order identifies nonexistent cases and an inaccurate statutory quotation, says the factitious citations appear AI-created, and states that even one future factitious citation may trigger sanctions.",
    incident={"conduct":"Self-represented plaintiff filed objections with inaccurate statutory text, nonexistent cases, and real cases that did not support asserted propositions.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    87,
    decision_id="txapp-2026-higgins-v-state",
    case_name="Higgins v. State",
    court="Texas Court of Appeals, Twelfth District",
    court_level="state-appellate",
    state="TX",
    date_filed="2026-07-31",
    docket_number="12-25-00090-CR",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "competence-fees", "criminal-justice-algorithms"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="artificial intelligence",
    disposition="The court affirmed Higgins's conviction and rejected ineffective-assistance arguments, including complaints about an inaccurate AI-prepared memorandum.",
    ai_passage="Outside the jury’s presence, the trial judge referred to a written memorandum defense counsel filed regarding the admissibility of said items. During the ensuing colloquy between the trial judge and defense counsel, the trial judge stated that defense counsel’s memorandum misstated the holdings of several cases, whereupon defense counsel admitted that the memorandum was produced by artificial intelligence and he did not read the cases cited therein. The trial judge overruled defense counsel’s objection and admitted the items into evidence. ... Counsel described the amount of discovery in Appellant’s case as “insurmountable” and stated that he used artificial intelligence (AI) to transcribe long videos into written form to make it easier to review them with Appellant. ... Counsel also testified that he used AI to generate memoranda regarding legal issues. ... Appellant argues that trial counsel provided ineffective assistance by ... presenting an inaccurate AI-prepared memorandum to the trial court ... Assuming without deciding that counsel’s performance was deficient, we conclude that Appellant fails to establish that, but for counsel’s alleged errors and omissions, the outcome of his trial would have been different.",
    cited_authorities=["Strickland v. Washington, 466 U.S. 668 (1984)", "Texas Rule of Evidence 403"],
    summary="The Texas Twelfth Court of Appeals affirms Kevin Higgins’s conviction. The opinion recounts defense counsel’s admission that an AI-produced evidentiary memorandum misstated case holdings because counsel did not read the cited cases, but holds Higgins did not establish Strickland prejudice.",
    incident={"conduct":"Defense counsel filed an AI-produced memorandum misstating several case holdings and admitted he had not read the cited cases.", "outcome":"other", "actor":"lawyer", "monetary_penalty":None, "currency":None, "ai_tool":"artificial intelligence"},
)

add(
    88,
    decision_id="gao-2026-jaaw-group",
    case_name="Matter of The JAAW Group, LLC",
    court="Government Accountability Office",
    court_level="federal-specialty",
    state=None,
    date_filed="2026-07-31",
    docket_number="B-424433.22",
    document_type="opinion",
    topics=["fabricated-citations", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="GAO dismissed the protest on factual insufficiency and warned that future nonexistent or irrelevant citations may lead to sanctions.",
    ai_passage="In addition to the factual inaccuracies discussed above, JAAW offered, in support of its protest arguments, citations to five bid protest decisions--two decisions of our Office and three decisions of the U.S. Court of Appeals for the Federal Circuit. ... Based on these inaccurate legal citations, the Army posited that JAAW’s protest “bears indicia consistent with the use of a large-language model or other artificial intelligence (AI)” tool. ... The Army correctly notes that two citations in JAAW’s July 2, 2026 GAO protest require correction. JAAW acknowledges these errors and takes full responsibility: 1. Tyco Electronics Corp., B-411937: The Army was unable to locate this decision. JAAW has independently verified that this citation as presented does not correspond to a published GAO decision. JAAW withdraws this citation. ... 2. Impresa Construzioni Geom. Domenico Garufi v. United States, 238 F.3d 1324 (Fed. Cir. 2001): The Army correctly notes that this case addresses a contractor responsibility determination, not solicitation ambiguity. JAAW withdraws the citation as applied to the ambiguity argument. ... while there is nothing inherently wrong with the proper and competent use of AI tools in the legal arena, this evolving technology has many glitches--including hallucinations--and must only be used with close, careful supervision, fact-checking, and citation-checking. ... Here, because we dismiss the protest for failing to set forth a factually sufficient basis of protest, we do not exercise our right to impose sanctions for JAAW’s submission of one non-existent citation and one wholly irrelevant citation. The protester, however, is advised that any future submissions of filings to our Office with citations to non-existent or wholly irrelevant authority may, after a review of the totality of the circumstances, result in the imposition of sanctions.",
    cited_authorities=["Tyco Electronics Corp., B-411937", "Impresa Construzioni Geom. Domenico Garufi v. United States, 238 F.3d 1324 (Fed. Cir. 2001)", "KE System Servs., Inc., B-423881", "Raven Investigations & Sec. Consulting, LLC, B-423447", "4 C.F.R. § 21.1(c)(4)"],
    summary="GAO dismisses JAAW’s bid protest as factually insufficient and separately addresses AI-associated citation problems. The decision notes one nonexistent GAO citation and one irrelevant Federal Circuit citation, declines sanctions because dismissal rests on other grounds, and warns future filings may be sanctioned.",
    incident={"conduct":"Protester submitted one nonexistent GAO decision citation and one Federal Circuit citation unrelated to the solicitation-ambiguity proposition asserted.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    89,
    decision_id="vaeb-2026-in-re-mahar",
    case_name="In re Mahar",
    court="United States Bankruptcy Court for the Eastern District of Virginia",
    court_code="vaeb",
    court_level="federal-bankruptcy",
    state="VA",
    date_filed="2026-07-31",
    citation="2026 WL 2220314",
    docket_number="25-72454-SCS; Adv. No. 25-07027-SCS",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The bankruptcy court dismissed the adversary complaint without prejudice for lack of subject-matter jurisdiction.",
    ai_passage="At the March 26, 2026 hearing, the Court advised Ms. Mahar's counsel that one of the cases he cited in support of this proposition does not exist. ECF No. 61, Transcript of Mar. 26, 2026 hearing, at 9-10. Despite extensive efforts, the Court was unable to locate any case by the alleged name, and its case citation within the response returned a completely unrelated case that is criminal in nature. See ECF No. 34, at 4 (citing the non-existent case titled In re Coastal Carolina Fruit Company). ... In support of this argument, Ms. Mahar's counsel cites three cases for which the United States District Court and Westlaw case numbers, as well as the decision dates, are incorrect. See ECF No. 34, at 2 (cases of Jennings v. RoundPoint Mortgage Servicing Corporation; Mastin v. Ditech Financial, LLC; and Heflin v. PHH Mortgage Corporation). The Court advised Ms. Mahar's counsel of the discovery of the incorrect case information at the March 26, 2026 hearings. ECF No. 61, at 9-10. The Court further advised counsel of a fourth case name contained in the pleading that was nonexistent (the citation for which related to a criminal case). Id. at 10; see n.12, supra.",
    cited_authorities=["In re Coastal Carolina Fruit Company", "Jennings v. RoundPoint Mortgage Servicing Corporation", "Mastin v. Ditech Financial, LLC", "Heflin v. PHH Mortgage Corporation", "28 U.S.C. § 1334"],
    summary="The Eastern District of Virginia bankruptcy court dismisses Alicia Mahar’s adversary complaint for lack of jurisdiction. Footnotes note that counsel cited a nonexistent In re Coastal Carolina Fruit Company decision and supplied incorrect court, Westlaw, or date information for three other mortgage cases.",
    incident={"conduct":"Plaintiff’s counsel cited a nonexistent bankruptcy case and three existing-case names with incorrect court, Westlaw, or date information.", "outcome":"other", "actor":"lawyer", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    90,
    decision_id="txapp-2026-in-re-smt-sjt",
    case_name="In the Interest of S.M.T. and S.J.T.",
    court="Texas Court of Appeals, Fourteenth District",
    court_level="state-appellate",
    state="TX",
    date_filed="2026-07-30",
    docket_number="14-25-00151-CV",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "competence-fees", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="artificial intelligence",
    disposition="The court affirmed and ordered attorney Jerry Lytel Lavespere III to complete three additional hours of AI-focused CLE.",
    ai_passage="Finally, some discussion of appellant’s brief is warranted. As previously mentioned, appellant’s brief is disjointed and difficult to follow. However, that is not the only shortcoming of appellant’s briefing. It is obvious that appellant’s brief was either (1) the result of using artificial intelligence yielding hallucination citations or (2) a deliberate attempt to mislead this court. I prefer to assume the use of AI rather than intentional deception. ... Unfortunately, the brief is far from accurate. On page 8 of Mr. Lavespere’s brief, he states: “As held in In re Marriage of Harrison, 557 S.W.3d 99, 111 (Tex. App.—Houston [14th Dist.] 2018, pet. denied), a trial court’s failure to consider valid objections to a proposed order can constitute reversible error. The court stated that ‘fundamental notions of due process require that parties be afforded a reasonable opportunity to be heard on issues affecting their rights.’” Although the Marriage of Harrison case exists, the passage that Mr. Lavespere quoted is entirely fabricated. Unfortunately, that is not the only instance of fabricated or hallucinated quotations. ... The problem with fake citations and quotations has become rampant. While courts might ignore hallucination cases and quotations from pro se litigants, we cannot turn a blind eye when lawyers commit the same transgressions. ... Although appellee did not request sanctions, on our own motion we order attorney Lavespere to attend three hours of Continuing Legal Education on the dangers of the use of artificial intelligence in court filings and to certify to this court such attendance and compliance within sixty days of this opinion.",
    cited_authorities=["In re Marriage of Harrison, 557 S.W.3d 99 (Tex. App.—Houston [14th Dist.] 2018)", "In re Marriage of Swim, 291 S.W.3d 500 (Tex. App.—Amarillo 2009)", "Lenz v. Lenz, 79 S.W.3d 10 (Tex. 2002)", "In re A.S., 298 S.W.3d 834 (Tex. App.—Amarillo 2009)", "In re Terminix Intern. Co., L.P., 131 S.W.3d 651 (Tex. App.—Corpus Christi–Edinburg 2004)", "In re Bennett, 960 S.W.2d 35 (Tex. 1997)"],
    summary="The Fourteenth Court of Appeals affirms a child-custody modification judgment and sanctions Father’s lawyer. The court finds fabricated quotations from Harrison and Swim, unsupported assertions from Lenz and A.S., assumes AI hallucination rather than deliberate deception, and orders three additional hours of AI-focused CLE.",
    incident={"conduct":"Appellant’s lawyer signed a brief with fabricated quotations from real cases and asserted propositions not found in cited authorities.", "outcome":"sanctions", "actor":"lawyer", "monetary_penalty":None, "currency":None, "ai_tool":"artificial intelligence"},
)

add(
    91,
    decision_id="utd-2026-carey-v-breakell",
    case_name="Carey v. Breakell",
    court="United States District Court for the District of Utah",
    court_code="utd",
    court_level="federal-district",
    state="UT",
    date_filed="2026-07-30",
    docket_number="4:25-cv-00108-AMA-PK",
    document_type="order",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court transferred the action to Arizona and left possible AI-related citation issues for the receiving judge.",
    ai_passage="Before addressing the substance of Defendants’ Motion, the Court calls attention to certain concerns it has regarding the Opposition Plaintiff’s counsel filed on March 10, 2026. In reviewing the Opposition, the Court located a number of case citations suggesting that the improper use of artificial intelligence may have occurred here. For example, the Opposition cites to “Larsen v. Davis Cnty. Sch. Dist., 2017 UT App 27, ¶¶ 14–16, 392 P.3d 1008 (Utah Ct. App. 2017)” and “Dale v. Bennett, 921 P.2d 466, 469 (Utah 1996)[,]” but the Court has been unable to locate these cases as cited on Westlaw. Citations to non-existent cases “undermine the integrity of court filings and evince a lack of diligence under Federal Rule of Civil Procedure 11(b).” “A fake opinion is not ‘existing law’ and citation to a fake opinion does not provide a non-frivolous ground for extending, modifying, or reversing existing law, or for establishing new law. An attempt to persuade a court or oppose an adversary by relying on fake opinions is an abuse of the adversary system.” The Court does not take suggestions of the improper use of artificial intelligence lightly. However, because, as the Court will discuss in full below, transfer of this action to the District of Arizona is appropriate, the Court will leave this issue to be handled according to the discretion of the receiving judge. As such, this issue does not impact the Court’s decision in this Order, which the Court makes according to the applicable law.",
    cited_authorities=["Larsen v. Davis Cnty. Sch. Dist., 2017 UT App 27", "Dale v. Bennett, 921 P.2d 466 (Utah 1996)", "Fed. R. Civ. P. 11(b)", "28 U.S.C. §§ 1404, 1406"],
    summary="The District of Utah grants transfer to Arizona and flags possible improper AI use in plaintiff’s opposition. The order says counsel cited two cases the court could not locate on Westlaw, quotes authority condemning fake opinions, and leaves the matter to the receiving judge.",
    incident={"conduct":"Plaintiff’s counsel filed an opposition citing two Utah cases the court could not locate and treated as possible AI-related fake opinions.", "outcome":"pending", "actor":"lawyer", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    92,
    decision_id="nysd-2026-in-re-firestar-diamond",
    case_name="In re Firestar Diamond, Inc.",
    court="United States District Court for the Southern District of New York",
    court_code="nysd",
    court_level="federal-district",
    state="NY",
    date_filed="2026-07-30",
    docket_number="25 Civ. 9434 (AT)",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="artificial intelligence (‘AI’) tool",
    disposition="The court denied Modi leave to pursue an interlocutory bankruptcy appeal and dismissed the action.",
    ai_passage="[H]e claims that because he has no access to a computer or typing facilities in prison, he first wrote “the entire document by hand” and then had “a person outside the prison type[] [his] handwritten notes and input[] them into an [artificial intelligence (‘AI’)] tool to help format the document properly.” Id. at 2. The Trustee contends that the legal citations in the motion “appear[] to be AI-generated” and that although “most of the cited cases exist, they generally do not support the propositions stated” and that at least one case citation “includes a non-existent quotation.” Opp. at 12. ... Rule VI reminds “all parties” of “their obligation to provide the Court with accurate and complete representations in any pleading, written motion, or other paper submitted to the Court” pursuant to Federal Rule of Civil Procedure 11. Rule VI further requires a party using “generative artificial intelligence” for any submission to confirm for themselves “that the submission and all source material within, is accurate and in compliance with the obligations of Rule 11.” ... For example, on page 21, Modi argues that the Order violates “fundamental notions of fair play” and cites Cohen v. Beneficial Indus. Loan Corp., 337 U.S. 541, 546 (1949) for the quotation. Mot. at 21. That quotation does not, however, appear in Cohen. The Court is also concerned by what appear to be AI-generated legal citations that do not support the propositions in the motion. Compare, e.g., Mot. at 18 (citing Traguth v. Zuck, 710 F.2d 90 (2d Cir. 1983) for the proposition that “the Second Circuit held that courts must give special solicitude to pro se prisoners to prevent unfair technical dismissals”), with Traguth, 710 F.2d at 95 (setting aside default judgment in case involving a pro se defendant, who was not incarcerated, where default was not willful).",
    cited_authorities=["Fed. R. Civ. P. 11", "Fed. R. Bankr. P. 8011", "Cohen v. Beneficial Industrial Loan Corp., 337 U.S. 541 (1949)", "Traguth v. Zuck, 710 F.2d 90 (2d Cir. 1983)"],
    summary="The Southern District of New York denies Nirav Modi’s motion for leave to appeal a bankruptcy order. The court notes Modi used an outside person and AI tool to format the motion, identifies a false Cohen quotation and unsupported AI-generated citations, and dismisses the action.",
    incident={"conduct":"Self-represented appellant submitted an AI-assisted bankruptcy appeal motion with a non-existent quotation and citations that did not support asserted propositions.", "outcome":"dismissal", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":"artificial intelligence (‘AI’) tool"},
)

add(
    93,
    decision_id="wiscapp-2026-first-community-credit-union-v-smith",
    case_name="First Community Credit Union v. Smith",
    court="Wisconsin Court of Appeals, District IV",
    court_level="state-appellate",
    state="WI",
    date_filed="2026-07-30",
    docket_number="2025AP1045",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed and denied the respondent's frivolous-appeal fee motion, while cautioning Smith about false citations.",
    ai_passage="Smith’s briefs include false legal citations, of which her citation to Gielow is one example. Specifically, and as noted throughout this opinion, some citations misrepresent the content of the cited cases and statutes, and some citations are to legal authorities that exist but are wholly unrelated to the proposition for which they are cited. The inclusion of false legal citations in Smith’s briefing violates WIS. STAT. RULE 809.19(1)(e) and (4)(b). This court cautions Smith not to repeat this violation in any future filings in this or any court. I offer an additional note of caution—if the root of the problem is that Smith used generative AI for legal research and trusted it to provide accurate results, she should be aware that there are many reported instances in which generative AI has hallucinated nonexistent cases and misreported the holdings of existing cases. ... While many if not most of Smith’s arguments are not supported by the record or by citations to relevant authority, I cannot conclude that the entire appeal is frivolous. Accordingly, I deny First Community’s motion.",
    cited_authorities=["Gielow v. Napiorkowski, 2003 WI App 249", "WIS. STAT. RULE 809.19(1)(e)", "WIS. STAT. RULE 809.19(4)(b)", "WIS. STAT. RULE 809.25", "Thompson v. Ouellette, 2023 WI App 7"],
    summary="The Wisconsin Court of Appeals affirms in a credit-union dispute and denies a frivolous-appeal fee request. A footnote says Ashley Smith’s briefs contain false legal citations, warns against repetition, and cautions that generative AI can hallucinate nonexistent cases or misreport holdings.",
    incident={"conduct":"Self-represented appellant filed briefs with false legal citations, including misrepresented case and statutory authorities and irrelevant authorities.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    94,
    decision_id="msnd-2026-harris-v-bank-of-america",
    case_name="Harris v. Bank of America",
    court="United States District Court for the Northern District of Mississippi",
    court_code="msnd",
    court_level="federal-district",
    state="MS",
    date_filed="2026-07-30",
    docket_number="3:25-cv-00328-MPM-JMV",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court dismissed Harris's FCRA claims without prejudice for lack of standing and warned him about hallucinated case law.",
    ai_passage="While not touched on by the current opinion due to lack of standing, the Court will note that Mr. Harris cited “Allen v. Equifax Info. Services, LLC, 2020 WL 2155673, at 3 (N.D. Miss. Apr. 1, 2020) and LeBlanc v. TransUnion, LLC, 2021 WL 1243659, at 5 (N.D. Miss. Mar. 19, 2021)” to support his claims against BANA. These two cited Northern District of Mississippi Opinions were unable to be found by this Court, and are likely fictitious citations generated by artificial intelligence. Neither a search of the Westlaw citations or the party names brings up any corresponding case in the Northern District. Citations to and reliance on fraudulent authorities severely undermines the credibility of any of Mr. Harris’ allegations. Due to his pro se nature, the Court will not sanction Mr. Harris, but he is put on notice and will not be given the same grace if he refiles his lawsuit and cites to hallucinated case law again.",
    cited_authorities=["Allen v. Equifax Info. Services, LLC, 2020 WL 2155673 (N.D. Miss. Apr. 1, 2020)", "LeBlanc v. TransUnion, LLC, 2021 WL 1243659 (N.D. Miss. Mar. 19, 2021)"],
    summary="The Northern District of Mississippi dismisses a pro se FCRA suit without prejudice for lack of standing. A footnote identifies two Northern District opinions that the court could not locate, calls them likely AI-generated fictitious citations, declines immediate sanctions, and warns Harris.",
    incident={"conduct":"Self-represented plaintiff cited two likely fictitious Northern District of Mississippi opinions in opposition briefing.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    95,
    decision_id="illappct-2026-cole-v-lee",
    case_name="Cole v. Lee",
    court="Appellate Court of Illinois, First District",
    court_level="state-appellate",
    state="IL",
    date_filed="2026-07-30",
    citation="2026 IL App (1st) 252223-U",
    docket_number="1-25-2223",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The appellate court struck Cole's brief and dismissed the appeal because repeated inaccurate citations prevented meaningful review.",
    ai_passage="Before we can consider the merits of Cole’s contentions, we observe that several of his citations to authorities are incorrect, including attributing propositions to authorities that those authorities simply do not support. For example, citing to Avery v. State Farm Mutual Automobile Insurance Co., 216 Ill. 2d 100 (2005), Cole asserts that claims under the Consumer Fraud Act that seek damages are legal claims triable to a jury. However, Avery contains no support for that proposition. Additionally, citing to People ex rel. Daley v. Datacom Systems Corp., 146 Ill. 2d 1 (1991), Cole asserts that where legal and equitable issues are joined, the legal issues must be tried to a jury. Datacom likewise contains no support for that proposition. In addition to attributing propositions to authorities that those authorities do not support, Cole also cites to multiple cases with incorrect citations. ... Under Illinois Supreme Court Rule 341(h)(7) (eff. Oct. 1, 2020), an appellant’s brief must contain argument “with citation of the authorities.” Implicit in this requirement is that citations to authority be accurate. ... Cole’s repeated inaccuracies in this case have prevented meaningful review of his contentions of error and improperly shifted the burden of legal research onto this court. ... Accordingly, we strike Cole’s brief and dismiss his appeal.",
    cited_authorities=["Avery v. State Farm Mutual Automobile Insurance Co., 216 Ill. 2d 100 (2005)", "People ex rel. Daley v. Datacom Systems Corp., 146 Ill. 2d 1 (1991)", "Stephens v. Kasten, 383 Ill. 127 (1943)", "In re Estate of Mulvaney, 128 Ill. App. 3d 133 (1984)", "Ill. S. Ct. R. 341(h)(7)", "Strong v. Zubha Pop Foods LLC, 2026 IL App (1st) 242451-U"],
    summary="The Illinois First District strikes Tony Cole’s pro se brief and dismisses his appeal. The order identifies authorities that do not support cited propositions and incorrect case citations, says the inaccuracies improperly shifted research burdens to the court, and relies on repeated Rule 341 violations.",
    incident={"conduct":"Self-represented appellant filed a brief with case citations that did not support asserted propositions and several incorrect reporter citations.", "outcome":"dismissal", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    96,
    decision_id="txapp-2026-in-re-qc-pc",
    case_name="In the Interest of Q.C. and P.C.",
    court="Texas Court of Appeals, Second District",
    court_level="state-appellate",
    state="TX",
    date_filed="2026-07-30",
    docket_number="02-24-00278-CV",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court denied Mother's pending motions and affirmed the trial court's modification judgment.",
    ai_passage="Despite the lengthy preparation time, her opening brief’s purported legal analysis—which advanced six appellate issues—spanned just five pages with zero record references and a citation to a nonexistent case. Cf. Tex. R. App. P. 38.1(i). ... Three months later, on the day Father’s brief was due, Mother moved for leave to file an overhauled amended brief. Mother conceded that her original opening brief had not complied with the Rules of Appellate Procedure and she stated that her amended opening brief “correct[ed the] technical deficiencies, incorporate[d] accurate citations to the record and legal authority, and present[ed] the substantive arguments in a clear, organized manner.” ... But as it turned out, Mother’s amended brief was nearly three times the length of her original brief and it raised new and different appellate issues. ... Furthermore, Mother’s amended opening brief cited to portions of case law that did not exist and quoted statements nowhere to be found in the cited case law. ... Mother cannot raise new appellate issues beyond those in her original opening brief, and even if she had obtained leave to do so, the eight issues raised in her amended opening brief lack merit. Mother’s pending motions are denied, and the trial court’s judgment is affirmed.",
    cited_authorities=["Tex. R. App. P. 38.1(i)", "ERC Midstream LLC v. American Midstream Partners, LP, 497 S.W.3d 99 (Tex. App.—Houston [14th Dist.] 2016)"],
    summary="The Texas Second Court of Appeals affirms a child-custody modification judgment on rehearing. The opinion notes Mother’s original brief cited a nonexistent case and that her counsel-filed amended brief cited nonexistent case portions and false quotations, but the court resolves the appeal on briefing and merits grounds.",
    incident={"conduct":"Appellant’s original and amended briefs cited a nonexistent case, nonexistent portions of case law, and quotations not found in cited cases.", "outcome":"other", "actor":"lawyer", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    97,
    decision_id="cod-2026-maloit-v-maloit",
    case_name="Maloit v. Maloit",
    court="United States District Court for the District of Colorado",
    court_code="cod",
    court_level="federal-district",
    state="CO",
    date_filed="2026-07-29",
    docket_number="24-cv-02383-PAB-KAS",
    document_type="report-and-recommendation",
    topics=["fabricated-citations", "pro-se-ai-use", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The magistrate judge recommended summary judgment, granted discovery-fee sanctions in part, and ordered Maloit to show cause over defective citations.",
    ai_passage="Finally, it has come to the Court’s attention that Plaintiff’s Response briefs in opposition to the instant Motion for Summary Judgment [#91] and Motion for Sanctions [#87] contain defective citations to case law. These defects include (1) misattributed or inaccurately quoted language from cases, (2) misrepresentations of legal concepts associated with the cited cases, and, most concerningly, (3) citations to cases that do not exist. Plaintiff appears to have used generative artificial intelligence to prepare her briefs. At this juncture, many generative AI tools are incapable of distinguishing between legitimate precedent and fabricated legal fiction. ... Defendant pointed out some of these deficiencies in his Reply in Support of Motion for Sanctions [#118], stating that the hallucinated citations to legal authority “forced [him] to incur yet further attorney fees to verify the falsity of [Plaintiff’s] citations.” ... The submission of legal argument premised on nonexistent law generated by artificial intelligence is a flagrant Rule 11 violation. ... In conducting a thorough inquiry, the Court believes that the following legal authorities that Plaintiff cited in her briefs do not exist: Mastro v. Rigby, 767 F.3d 934 (10th Cir. 2014) ... United States v. Kitchen, 57 F.3d 916 (10th Cir. 1995) ... Somlo v. S.C. Johnson & Son, Inc., 7 F.3d 1334, 1338 (10th Cir. 1993) ... Mikulski v. Center for Psychiatric Rehabilitation, 789 F.3d 1205, 1213 (10th Cir. 2015) ... Chavez v. Young, 880 F.2d 299, 302-03 (10th Cir. 1989) ... Mobley v. McCormick, 40 F.4th 1199, 1205 (10th Cir. 2022) ... Shen v. Express Scripts, Inc., 2019 WL 4741257, at *3. ... Accordingly, the Court orders that, no later than August 26, 2026, Plaintiff shall SHOW CAUSE in writing why the Court should not further sanction her for her submission of defective legal citations.",
    cited_authorities=["Fed. R. Civ. P. 11", "Wadsworth v. Walmart Inc., 348 F.R.D. 489 (D. Wyo. 2025)", "Coomer v. Lindell, 2025 WL 1865282 (D. Colo. July 7, 2025)", "Ferris v. Amazon.com Servs., LLC, 778 F. Supp. 3d 879 (N.D. Miss. 2025)", "Mastro v. Rigby, 767 F.3d 934 (10th Cir. 2014)", "United States v. Kitchen, 57 F.3d 916 (10th Cir. 1995)", "Somlo v. S.C. Johnson & Son, Inc., 7 F.3d 1334 (10th Cir. 1993)", "Mikulski v. Center for Psychiatric Rehabilitation, 789 F.3d 1205 (10th Cir. 2015)", "Chavez v. Young, 880 F.2d 299 (10th Cir. 1989)", "Mobley v. McCormick, 40 F.4th 1199 (10th Cir. 2022)", "Shen v. Express Scripts, Inc., 2019 WL 4741257"],
    summary="The District of Colorado magistrate judge recommends summary judgment and grants discovery-fee sanctions in part. The order separately finds Maloit’s briefs contain misquotations, misstatements, and seven nonexistent cases likely from generative AI, then orders her to show cause about additional sanctions.",
    incident={"conduct":"Self-represented plaintiff filed response briefs with misquoted language, misstated legal concepts, and at least seven nonexistent case citations.", "outcome":"pending", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    98,
    decision_id="ca10-2026-robinson-v-oglala-sioux-tribe",
    case_name="Robinson v. Oglala Sioux Tribe",
    court="United States Court of Appeals for the Tenth Circuit",
    court_code="ca10",
    court_level="federal-appellate",
    state=None,
    date_filed="2026-07-29",
    docket_number="25-6143",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use", "evidence-authentication"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The Tenth Circuit affirmed dismissal with prejudice as a Rule 11 sanction for Robinson's litigation misconduct.",
    ai_passage="The district court’s order detailed the clear and convincing evidence it relied on to determine that Ms. Robinson’s conduct was sanctionable. The court noted that despite her claims that her emergency motion was “grounded in fact,” Ms. Robinson submitted “no evidence to support the veracity of the purported intercepted statements” about Mr. Raines following her, and admitted she submitted a photo that was “not authentic” as an exhibit to one of her filings. ... The court further noted that at least four of Ms. Robinson’s filings contained non-existent and misrepresented legal authority, and cited caselaw establishing that failure “to confirm the validity of any cited legal authority” may violate Rule 11. ... Ms. Robinson also claims on appeal that “[a]ll case citations are verifiable,” and that she never submitted any fake or AI-hallucinated cases. Aplt. Opening Br. at 2. But this is not true. In fact, Ms. Robinson relied on a hallucinated case in her opening brief on appeal. See id. at 2 (citing a non-existent case called “Reynolds v. Smith, 62 F.3d 1421 (10th Cir. 1995)”). ... For example, in Ms. Robinson’s opposition to WLCC’s and Mr. Raines’s motion to dismiss, she cited “Navajo Nation Oil & Gas Co. v. Window Rock Unified Sch. Dist., 638 F. App’x 698 (10th Cir. 2016).” Aplee. Supp. App. vol. III at 256. But the case found at 638 F. App’x 698 is Sayed v. Broman. On the same page, Ms. Robinson quotes Lewis v. Clarke, 581 U.S. 155 (2017), as stating, “tribal immunity does not extend to individuals acting outside their official capacity,” but that quote does not exist in the case. Id. ... The district court did not abuse its discretion by dismissing Ms. Robinson’s claims with prejudice as a sanction for her litigation misconduct.",
    cited_authorities=["Fed. R. Civ. P. 11", "Ehrenhaus v. Reynolds, 965 F.2d 916 (10th Cir. 1992)", "Sanders v. United States, 176 Fed. Cl. 163 (2025)", "Reynolds v. Smith, 62 F.3d 1421 (10th Cir. 1995)", "Navajo Nation Oil & Gas Co. v. Window Rock Unified Sch. Dist., 638 F. App'x 698 (10th Cir. 2016)", "Lewis v. Clarke, 581 U.S. 155 (2017)"],
    summary="The Tenth Circuit affirms dismissal of Shantell Robinson’s claims with prejudice as a Rule 11 sanction. The order describes nonauthentic evidence, at least four filings with nonexistent or misrepresented authority, and a new appellate brief citation to the nonexistent Reynolds v. Smith case.",
    incident={"conduct":"Self-represented plaintiff filed nonauthentic evidence and multiple filings with nonexistent, misrepresented, or falsely quoted legal authorities.", "outcome":"dismissal", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    99,
    decision_id="tnctapp-2026-harding-place-v-robinson",
    case_name="Harding Place Multifamily Partners v. Robinson",
    court="Court of Appeals of Tennessee",
    court_level="state-appellate",
    state="TN",
    date_filed="2026-07-29",
    docket_number="M2025-01361-COA-R3-CV",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court disregarded inaccurate or fabricated portions of Robinson's brief and affirmed the trial court's judgment.",
    ai_passage="Unfortunately, Mr. Robinson’s brief fails to comply with this rule as it contains numerous false quotations from case law and statutes and, in some instances, outright fake citations. In this way, Mr. Robinson’s brief bears all the hallmarks of an artificial intelligence-generated brief, filled with what has been referred to as “hallucinations.” ... Mr. Robinson’s brief contains all of these forms of hallucinations. For instance, Mr. Robinson cites to “First Tenn. Bank Nat’l Ass’n v. McClure, 199 S.W.3d 429, 432 (Tenn. Ct. App. 2005).” While there is a real case under that name, it is not reported in the South Western Reporter. The citation given actually leads to the dissent of a case from the Court of Appeals of Texas, City of Seabrook v. Port of Houston Auth., 199 S.W.3d 403 (Tex. App. 2006). Further, the real McClure case is not from 2005 but from 1990. ... This issue of AI hallucinations is prevalent in Mr. Robinson’s statutory citations as well. His brief quotes Tenn. Code Ann. § 66-28-304(a) as “A landlord shall: . . . (4) Maintain in good and safe working order and condition all electrical, plumbing, sanitary, heating, ventilating air-conditioning and other facilities and appliances supplied or required to be supplied by the landlord.” ... However, that section of the code, Tenn. Code Ann. § 66-28-304(a)(4), actually states: “In multi-unit complexes of four (4) or more units, provide and maintain appropriate receptacles and conveniences for the removal of ashes, garbage, rubbish and other waste from common points of collection subject to § 66-28-401(3),” language which is certainly less helpful to Mr. Robinson’s position. Further still, some cases appear to be fabricated entirely as Mr. Robinson cites to “Puckett v. Estate of Puckett, 174 S.W.3d 252, 257 (Tenn. 2005).” The given location in the reporter is actually for the Court of Appeals case Emmit v. Emmit, 174 S.W.3d 248 (Tenn. Ct. App. 2005), and we are unable to find any Tennessee Supreme Court case under the cited case name. ... Because of the inaccurate citations to law, Mr. Robinson’s arguments are not “warranted by existing law,” as required by Tenn. Ct. App. R. 17.01. ... Therefore, we believe the best course is to disregard the citations in Mr. Robinson’s brief that do not accurately reflect what the authority states and address the arguments without consideration of fictitious or meritless arguments.",
    cited_authorities=["Tenn. Ct. App. R. 17.01", "Simmons v. Islam, 2026 WL 1431143 (Tenn. Ct. App. May 21, 2026)", "Andre v. Warden, FCI Danbury, 827 F. Supp. 3d 294 (D. Conn. 2025)", "First Tenn. Bank Nat'l Ass'n v. McClure, 199 S.W.3d 429 (Tenn. Ct. App. 2005)", "Tenn. Code Ann. § 66-28-304(a)", "Puckett v. Estate of Puckett, 174 S.W.3d 252 (Tenn. 2005)", "Akerlund v. Atlas Air, Inc., 2026 WL 1993146 (11th Cir. July 10, 2026)"],
    summary="The Tennessee Court of Appeals affirms a landlord-tenant judgment and disregards fabricated or inaccurate parts of Samuel Robinson’s pro se brief. The opinion says the brief bears AI hallmarks, identifies false case and statutory quotations, a fabricated Tennessee Supreme Court case, and unsupported legal assertions.",
    incident={"conduct":"Self-represented appellant filed a brief with false case and statutory quotations, a fabricated Tennessee Supreme Court citation, and misleading reporter citations.", "outcome":"other", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    100,
    decision_id="ohsd-2026-gragston-v-amazon",
    case_name="Gragston v. Amazon LLC",
    court="United States District Court for the Southern District of Ohio",
    court_code="ohsd",
    court_level="federal-district",
    state="OH",
    date_filed="2026-07-29",
    citation="2026 WL 2184981",
    docket_number="1:25-cv-206",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court granted Amazon's dismissal motion, allowed Gragston to seek leave to amend, and formally warned him about AI-hallucinated cases.",
    ai_passage="As Amazon suggests (but does not expressly state), Gragston seems to rely on AI-hallucinated caselaw in support of this point. (See Doc. 28, #141 n.2). The Court's independent review suggests the same. Gragston cites a case that he refers to as “Latham v. Off. of Att'y Gen. of Ohio, No. 20-4089, 2021 WL 1324065 (6th Cir. Apr. 9, 2021).” (Doc. 27, #133). True, there is a Sixth Circuit case that bears that name, but it is a published decision from 2005 that is not about hostile work environment claims or the use of racial epithets in the workplace. See 395 F.3d 261 (6th Cir. 2005). And, as best the Court can tell, the only Sixth Circuit case with the docket number “20-4089” is United States v. Culver, 20-4089, 2021 WL 4258764 (6th Cir. Sep. 20, 2021), which is a criminal case about sentencing. Finally, there is no case with the Westlaw citation “2021 WL 1324065.” Accordingly, to avoid any such concerns going forward, the Court FORMALLY WARNS Gragston that any future reliance on AI-hallucinated caselaw in this litigation will result in sanctions, including monetary penalties and dismissal of this case with prejudice. ... But, in offering Gragston this opportunity, the Court reiterates its warning that any further reliance on AI-hallucinated authorities in connection with briefing in this matter will result in sanctions, including monetary penalties and potential dismissal of this case with prejudice.",
    cited_authorities=["Latham v. Office of the Attorney General of Ohio, 395 F.3d 261 (6th Cir. 2005)", "United States v. Culver, 20-4089, 2021 WL 4258764 (6th Cir. Sept. 20, 2021)"],
    summary="The Southern District of Ohio dismisses Gragston’s amended employment complaint but permits a motion for leave to amend. A footnote identifies a purported Sixth Circuit hostile-work-environment citation as AI-hallucinated and formally warns that future reliance may bring monetary sanctions or dismissal with prejudice.",
    incident={"conduct":"Self-represented plaintiff cited a purported Sixth Circuit case with mismatched name, docket number, subject matter, and nonexistent Westlaw citation.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    101,
    decision_id="illappct-2026-scott-v-illinois-human-rights-commission",
    case_name="Scott v. Illinois Human Rights Commission",
    court="Appellate Court of Illinois, First District",
    court_level="state-appellate",
    state="IL",
    date_filed="2026-07-28",
    citation="2026 IL App (1st) 251462",
    docket_number="1-25-1462",
    document_type="opinion",
    topics=["fabricated-citations", "competence-fees", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="ChatGPT",
    disposition="The court affirmed the Commission's dismissal, fined attorney Mason Cole $15,000, and referred the opinion to the ARDC.",
    ai_passage="We also sanction petitioner’s attorney Mason Cole for submitting briefs containing false citations and quotations that are the product of artificial intelligence (AI) hallucinations. ... Petitioner’s briefs also contain false case citations. One such case, “Harris v. Illinois Human Rights Comm’n, 2022 IL App (1st) 210454,” does not exist at all. The citation 2022 IL App (1st) 210454-U leads to a criminal case named People v. Riley-Palmer. ... Citations of fictitious legal authority do not automatically justify striking a brief and dismissing an appeal. ... However, we must address petitioner’s attorney’s pattern of presenting multiple fabricated quotes of statutory language and case citations. ... On June 30, 2026, we ordered petitioner’s attorney Mason Cole to file a response explaining the false quotations and citations in his briefs by July 14, 2026. Attorney Cole filed his response on July 2, 2026, 12 days early. His response concedes that all the quotations and citations set out above are false for the reasons we have explained. Attorney Cole states that he “frequently use[s] a premier corporate subscription of ChatGPT” to “synthesize complex matters,” including this case. ... We order attorney Cole to pay a $15,000 fine to the clerk of the Appellate Court, First District, within 30 days of this opinion. ... Attorney Cole’s briefs contain a total of 10 false citations: 4 false statutory quotations, 1 nonexistent case, and 5 cases that exist but do not contain the cited principle or quoted language. This sanction reflects a $1,500 fine for each false citation and quotation. ... The fact that AI hallucinated these citations does not mitigate their falsehood. AI-hallucinated citations are no different than false citations an attorney could create from his own imagination. ... In addition, the clerk of the Appellate Court, First District, shall send a copy of this opinion to the ARDC.",
    cited_authorities=["Ill. S. Ct. R. 375", "Ill. S. Ct. R. 341", "Harris v. Illinois Human Rights Comm'n, 2022 IL App (1st) 210454", "People v. Riley-Palmer, 2022 IL App (1st) 210454-U", "In re Baby Boy, 2025 IL App (4th) 241427", "Couvrette, 2025 WL 4109655", "Noland v. Land of the Free, L.P., 336 Cal. Rptr. 5th 426 (Ct. App. 2025)", "Illinois Supreme Court Policy on Artificial Intelligence"],
    summary="The Illinois First District affirms dismissal of Kimberly Scott’s discrimination charge and sanctions attorney Mason Cole. The opinion says ChatGPT produced 10 false citations or quotations, fines Cole $15,000 at $1,500 per misstatement, and directs the clerk to send the opinion to the ARDC.",
    verification="fetched-and-read",
    notes="Official Illinois Courts PDF located through the lead's Reason/Volokh source and fetched/read directly.",
    lead_source=["charlotin-cc0", "reason-volokh"],
    incident={"conduct":"Attorney used ChatGPT in appellate briefing that contained four false statutory quotations, one nonexistent case, and five unsupported case quotations or principles.", "outcome":"sanctions", "actor":"lawyer", "monetary_penalty":15000, "currency":"USD", "ai_tool":"ChatGPT"},
)

add(
    102,
    decision_id="med-2026-mcneil-v-bisignano",
    case_name="McNeil v. Bisignano",
    court="United States District Court for the District of Maine",
    court_code="med",
    court_level="federal-district",
    state="ME",
    date_filed="2026-07-28",
    docket_number="2:25-cv-00292-SDN",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court granted summary judgment for the Commissioner and cautioned McNeil to personally check future citations.",
    ai_passage="The Court notes the presence of several citations to nonexistent or fabricated legal authority in Plaintiff's pleadings. “Although courts are solicitous toward pro se litigants, there are reasonable limits”—“a pro se litigant must not provide the Court with erroneous and factitious citations and has an obligation to review documents filed with the Court to make certain they are scrupulously accurate.” Everett J. Prescott, Inc. v. Beall, No. 1:25-cv-00071, 2025 WL 2084353, at *2 (D. Me. July 24, 2025) (quotation modified). Should Plaintiff continue to litigate matters before this Court, he is cautioned that he bears an obligation to personally check each citation to ensure it is “accurate and stands for its asserted proposition.” Id. ... For these reasons, the Commissioner’s motion for summary judgment, ECF No. 22, is GRANTED. Plaintiff’s amended complaint, ECF No. 20, is DISMISSED.",
    cited_authorities=["Everett J. Prescott, Inc. v. Beall, No. 1:25-cv-00071, 2025 WL 2084353 (D. Me. July 24, 2025)", "42 U.S.C. § 405(g)"],
    summary="The District of Maine grants summary judgment to the Social Security Commissioner and dismisses Alexander McNeil’s amended complaint. A footnote flags several nonexistent or fabricated legal authorities in the pro se pleadings and cautions McNeil to personally verify each future citation.",
    incident={"conduct":"Self-represented plaintiff filed pleadings with several citations to nonexistent or fabricated legal authority.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    103,
    decision_id="azd-2026-ruiz-v-magellan-financial-claude-osc",
    case_name="Ruiz v. Magellan Financial & Insurance Services",
    court="United States District Court for the District of Arizona",
    court_code="azd",
    court_level="federal-district",
    state="AZ",
    date_filed="2026-07-28",
    citation="2026 WL 2167989",
    docket_number="CV-23-02090-PHX-DWL",
    document_type="order",
    topics=["fabricated-citations", "competence-fees", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="Claude AI",
    tracker_slug="ruiz-v-magellan-financial",
    disposition="The court required plaintiff's counsel Elizabeth Tate to file a supplemental memorandum addressing additional possible AI-related quotation errors.",
    ai_passage="On July 8, 2026, the Court issued an order to show cause (“OSC”) requiring Plaintiff's counsel, Elizabeth Tate, to show cause why she should not be sanctioned or disciplined for including, in Plaintiff's response to Defendant's motion for attorneys’ fees, two false quotations from Ninth Circuit cases. ... Ms. Tate utilized Claude AI to help her research and prepare the Response ....After Claude prepared a draft brief incorporating the arguments Ms. Tate asked it to make, Ms. Tate entered the following query: ‘Now please make a list of the cited cases for me to review on lexis to make sure I agree with the way you've cited them.’ Claude generated a list of fourteen cases. ... But it appears that instead of reviewing the Claude-generated brief in a thorough line-by-line manner, confirming the accuracy of each citation as it arises during her review of the brief as a whole, Ms. Tate simply asks Claude to list the cases that Claude used when drafting the brief and then uses that list (rather than the brief) for purposes of her verification efforts. ... it does not strike the Court as responsible to allow an AI program to draft an entire brief and then submit that brief, without significant attorney reworking, as the attorney's own work product. Needless to say, Claude is not a licensed attorney permitted to practice law in the District of Arizona. ... Separately, during trial, Ms. Tate filed “Plaintiff's Brief on Impeachment.” (Doc. 124.) That brief contained the following purported quotation from United States v. Antonakeas, 255 F.3d 714 (9th Cir. 2001): “Rule 607 permits impeachment by contradiction, or the admission of extrinsic evidence to impeach specific errors or falsehoods in a witness's testimony.” (Id. at 2.) The quoted language, however, does not appear in Antonakeas. ... It appears to the Court that the additional examples identified above may also be attributable to the misuse of generative AI. ... IT IS ORDERED that within 14 days from the date of this order, Ms. Tate shall file a supplemental memorandum, not to exceed 10 pages, addressing the issues raised in this order.",
    cited_authorities=["United States v. Antonakeas, 255 F.3d 714 (9th Cir. 2001)", "United States v. Osazuwa, 564 F.3d 1169 (9th Cir. 2009)", "Malkeet Lnu v. Blanche, 177 F.4th 1014 (9th Cir. 2026)", "28 U.S.C. § 1924", "State Bar of Arizona, Guidance For The Use of Generative Artificial Intelligence In The Practice Of Law In Arizona (Apr. 22, 2025)"],
    summary="The District of Arizona expands an AI show-cause inquiry against Elizabeth Tate. The order recounts Tate’s Claude AI workflow, finds that list-based cite checking missed false quotations in several filings, criticizes delegating whole-brief drafting to Claude, and requires a supplemental memorandum.",
    incident={"conduct":"Plaintiff’s lawyer used Claude AI to draft filings containing false quotations from Ninth Circuit cases and a fabricated statutory quotation.", "outcome":"pending", "actor":"lawyer", "monetary_penalty":None, "currency":None, "ai_tool":"Claude AI"},
)

add(
    104,
    decision_id="ord-2026-owen-v-askew",
    case_name="Owen v. Askew",
    court="United States District Court for the District of Oregon",
    court_code="ord",
    court_level="federal-district",
    state="OR",
    date_filed="2026-07-28",
    docket_number="6:25-cv-01272-AA",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court denied defendants' dismissal, transfer, and anti-SLAPP motions and warned all parties against false or hallucinated citations.",
    ai_passage="In the course of briefing her motion to dismiss and in response to Plaintiff’s filings, Ms. Askew acknowledged that she relied on a false citation, “Young v. Maciorca, 69 F.4th 1099, 1106 (9th Cir. 2023).” ECF No. 92. Ms. Askew subsequently withdrew her references to “Young v. Maciorca,” which is not a Ninth Circuit decision. The Court notes, however, that “Young v. Maciorca” is not the only false citation in Ms. Askew’s briefing. Ms. Askew also cited to “IGI Cybersecurity Services v. [Defendant], Case No. 3:23-cv-01277 (D. Or. July 11, 2024),” in which Ms. Askew claims that “the court found no personal jurisdiction even though the defendant engaged in videoconferences and communications with Oregon parties. The court explained that such incidental or attenuated contacts, absent purposeful targeting, do not satisfy due process.” Askew Mot. at 6. As might be guessed from its incomplete caption, this is not the case cited. The docket number, 3:23-cv-1277, is for Cohen v. Infinite Group, Inc. et al. and, while that case did discuss personal jurisdiction and final judgment was entered on July 11, 2024, the case was subsequently reversed by the Ninth Circuit, which found errors in the district court’s analysis of personal jurisdiction. The Court understands that the parties in this case are self-represented and that there is a significant temptation to rely on artificial intelligence in the drafting of legal papers. The Court therefore advises the parties that it will not accept false or “hallucinated” citations and will view their inclusion in legal filings as an attempt to deceive or mislead the Court. All parties are warned that the inclusion of false or hallucinated citations in future briefs may result in the imposition of sanctions on the filing party.",
    cited_authorities=["Young v. Maciorca, 69 F.4th 1099 (9th Cir. 2023)", "IGI Cybersecurity Services v. [Defendant], Case No. 3:23-cv-01277 (D. Or. July 11, 2024)", "Cohen v. Infinite Group, Inc., No. 3:23-cv-1277", "LR 7-1(a)(3)"],
    summary="The District of Oregon denies self-represented defendants’ dismissal, transfer, and anti-SLAPP motions. Before reaching the merits, the order records withdrawn and additional false citations in Askew’s briefing and warns all parties that future false or hallucinated citations may be sanctioned.",
    incident={"conduct":"Self-represented defendant relied on a nonexistent Ninth Circuit citation and an incomplete, misleading District of Oregon citation.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    105,
    decision_id="mdd-2026-campbell-v-tidalhealth",
    case_name="Campbell v. TidalHealth, Inc.",
    court="United States District Court for the District of Maryland",
    court_code="mdd",
    court_level="federal-district",
    state="MD",
    date_filed="2026-07-28",
    docket_number="1:25-cv-04293-BAH",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "pro-se-ai-use", "discovery-ediscovery"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court denied both sides' sanctions requests, partly granted sealing, and cautioned Campbell about future AI-related authority errors.",
    ai_passage="One other consideration worth discussing is the potential misuse of generative artificial intelligence. The parties dedicate a substantial portion of their respective filings to whether Campbell’s motions involve improper use of or reliance on generative artificial intelligence, including whether she misstates legal authority or she uploaded confidential documents into a generative artificial intelligence program. ... Campbell denies submitting documents into any generative artificial intelligence tools but admits to using unspecified “available tools solely to express [her] arguments in proper legal format, the same way any litigant uses available legal resources.” ... Campbell’s filings bear common hallmarks of generative artificial intelligence, including their verbosity (more than 60 pages of briefing) about a relatively narrow issue, repeated statements that sound legally sophisticated while some of the legal citations are imprecise or inconsistent, and difficult to follow titles of her briefs. More concerning than those are any misrepresentations about the law. While the filings do not outright “hallucinate” any case, the citations do not support Campbell’s asserted propositions in the manner she attempts. For example, while Aguilar is a real case from the Southern District of New York (cited above and in the May 14 Order), the discussion at Campbell’s pincites does not say exactly what she represents. Also, her filings miss the mark in describing the import of this Court’s decision in Mancia. These could be viewed as a matter of (im)precision by a self-represented party lacking formal legal training rather than willful misleading or fabrication. In combination with other aspects of Campbell’s filings, they corroborate her admitted use of generative artificial intelligence. ... However, going forward, Campbell must exercise care in any use of generative artificial intelligence tools, to ensure that they do not generate any fictitious cases or, as best as she can determine, incorrect explanations of real cases. She is responsible for ensuring that the legal arguments presented in her filings are accurate and may not misrepresent the law to the Court. Further, the Court cautions that a failure to exercise such care could result in future sanctions, including an award of attorneys’ fees if future filings reflect bad faith or objectively improper arguments or authority.",
    cited_authorities=["Aguilar v. Immigration & Customs Enforcement Division, 255 F.R.D. 350 (S.D.N.Y. 2008)", "Mancia v. Mayflower Textile Services Co., 253 F.R.D. 354 (D. Md. 2008)", "Kruglyak v. Home Depot U.S.A., Inc., 774 F. Supp. 3d 755 (W.D. Va. 2025)", "United States v. Malik, 2025 WL 2687413 (D. Md. Sept. 19, 2025)", "Fed. R. Civ. P. 11"],
    summary="The District of Maryland denies discovery sanctions in a pro se employment case and addresses possible generative-AI misuse. The court says Campbell’s filings do not outright hallucinate cases but misdescribe Aguilar and Mancia, corroborating admitted tool use, and cautions that future errors may draw fees or sanctions.",
    incident={"conduct":"Self-represented plaintiff used generative-AI-adjacent tools and filed briefs with imprecise or incorrect descriptions of real cases.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    106,
    decision_id="txnd-2026-transcontinental-realty-v-moos",
    case_name="Transcontinental Realty Investors, Inc. v. Moos",
    court="United States District Court for the Northern District of Texas",
    court_code="txnd",
    court_level="federal-district",
    state="TX",
    date_filed="2026-07-28",
    docket_number="3:26-CV-694-O-BW",
    document_type="memorandum-opinion",
    topics=["fabricated-citations", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court denied the motions to disqualify Johansen and Blank Rome and admonished pro hac vice counsel about AI-related citation duties.",
    ai_passage="The filings in this case are riddled with inaccurate citations, seemingly deliberate misrepresentations of guiding caselaw and the factual record, failures to comply with Court rules, and, in at least one instance, advocacy using caselaw that does not exist, likely the result of imprudent reliance on a generative artificial intelligence tool. ... (See Int. Resp. at 14 (citing Aetna Health Inc. v. Health Goals Chiropractic Ctr., Inc., No. 3:12-CV-2587-O, 2012 WL 12873819, at *1 (N.D. Tex. Oct. 25, 2012) (O’Connor, J.))). The Court notes the existence of a case by the same name, Aetna Health Inc. v. Health Goals Chiropractic Center, Inc., No. 10-5216-NLH-JS, 2011 WL 1343047 (D.N.J. Apr. 7, 2011), but that case provides no support for the assertion made in the brief. The Court notes that the attorney who signed the brief, and thus made certain representations under Fed. R. Civ. P. 11(b), is appearing pro hac vice, and it admonishes counsel about the responsible use of generative artificial intelligence in court filings. See Shelton v. Parkland Health, No. 3:24-CV-2190-L-BW, 2025 WL 3141108, at *3 (N.D. Tex. Nov. 10, 2025). ... For the foregoing reasons, Plaintiffs Pillar and TCI’s Motion to Disqualify Johansen and Blank Rome (Dkt. No. 51) and the Liberty Parties’ Motion to Disqualify Johansen and Blank Rome (Dkt. No. 54) are DENIED.",
    cited_authorities=["Aetna Health Inc. v. Health Goals Chiropractic Ctr., Inc., No. 3:12-CV-2587-O, 2012 WL 12873819 (N.D. Tex. Oct. 25, 2012)", "Aetna Health Inc. v. Health Goals Chiropractic Center, Inc., No. 10-5216-NLH-JS, 2011 WL 1343047 (D.N.J. Apr. 7, 2011)", "Fed. R. Civ. P. 11(b)", "Shelton v. Parkland Health, 2025 WL 3141108 (N.D. Tex. Nov. 10, 2025)"],
    summary="The Northern District of Texas denies disqualification motions in a commercial dispute. The opinion notes briefing problems, including one nonexistent Northern District citation likely caused by imprudent generative-AI reliance, and admonishes pro hac vice counsel about responsible AI use and Rule 11 obligations.",
    incident={"conduct":"Pro hac vice counsel signed briefing citing a nonexistent N.D. Texas Aetna decision; only an unrelated D.N.J. case by that name existed.", "outcome":"warning", "actor":"lawyer", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    107,
    decision_id="mied-2026-ponder-v-bcg-equities",
    case_name="Ponder v. BCG Equities, LLC",
    court="United States District Court for the Eastern District of Michigan",
    court_code="mied",
    court_level="federal-district",
    state="MI",
    date_filed="2026-07-27",
    docket_number="2:25-13474",
    document_type="order",
    topics=["fabricated-citations", "pro-se-ai-use", "rules-by-opinion"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court struck pending motions, set aside default, set a responsive-pleading deadline, and warned both parties about generative AI.",
    ai_passage="Finally, the Court issues a caution about the use of generative artificial intelligence (“AI”). It appears from the briefing that one or both parties may be utilizing AI to draft their briefs. (See, e.g., ECF No. 20, PageID.71 (citing Antoine v. Atlas Turner, Inc., 66 F.3d 105, 110 (6th Cir. 1995) for a quotation and proposition that does not appear at the citation).) The parties should take note: AI cannot give legal advice, and, in many cases, its use in legal research has led to glaring misstatements of law and related sanctions awarded against both attorneys and pro se litigants. “At this point, it ‘is no secret that generative AI programs are known to ‘hallucinate’ nonexistent cases, and with the advent of AI, courts have seen a rash of cases in which both counsel and pro se litigants have cited such fake, hallucinated cases in their briefs.’” Seither & Cherry Quad Cities, Inc. v. Oakland Automation, LLC, No. 23-11310, 2025 WL 2105286, at *1 (E.D. Mich. July 28, 2025) (Behm, J.) (quoting Sanders v. United States, 176 Fed. Cl. 163, 169 (2025)). AI chatbots “are designed to mimic patterns of words, probabilistically. When they are ‘right,’ it is because correct things are often written down in the dataset they were trained on, not because they can independently fact-check themselves in the same way a human would.” Id. Indeed, French data scientist Damien Charlotin catalogued “at least 490 court filings” between May and October 2025 that contained hallucinations. ... Thus, the use of generative AI when drafting legal filings is a very risky practice, as pro se litigants and attorneys are still subject to the requirements of Fed. R. Civ. P. 11(b)(2) with respect to pleadings, motions and other documents they sign and submit to the Court; even in the absence of bad faith, Rule 11 sanctions for use of AI generated phantom cases may be warranted. ... The parties are HEREBY SO WARNED.",
    cited_authorities=["Antoine v. Atlas Turner, Inc., 66 F.3d 105 (6th Cir. 1995)", "Seither & Cherry Quad Cities, Inc. v. Oakland Automation, LLC, 2025 WL 2105286 (E.D. Mich. July 28, 2025)", "Sanders v. United States, 176 Fed. Cl. 163 (2025)", "Ali v. IT People Corp., Inc., 2025 WL 2682622 (E.D. Mich. Sept. 19, 2025)", "Fed. R. Civ. P. 11(b)(2)"],
    summary="The Eastern District of Michigan resets a pro se FCRA case by striking pending motions and setting aside default. The order cautions both sides after a brief cites Antoine for a quotation and proposition not found there, warning that generative-AI phantom cases can trigger Rule 11 sanctions.",
    incident={"conduct":"A party cited Antoine for a quotation and proposition that the court says do not appear at the cited source, suggesting possible generative-AI use.", "outcome":"warning", "actor":"other", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    108,
    decision_id="mnctapp-2026-ally-bank-v-ngouambe",
    case_name="Ally Bank v. Ngouambe",
    court="Minnesota Court of Appeals",
    court_level="state-appellate",
    state="MN",
    date_filed="2026-07-27",
    docket_number="A25-1873",
    document_type="opinion",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The court affirmed summary judgment and disregarded fabricated authority in Ngouambe's informal brief.",
    ai_passage="We conclude by addressing fabricated authority in Ngouambe’s brief to this court. Fabricated authority includes citations to authority that do not exist, quotations that do not appear in the cited authority, and asserted propositions of law not reasonably attributable to the cited authority. Ngouambe’s informal brief contains fabricated authority in the form of three citations to authority that do not exist and numerous asserted propositions of law not reasonably attributable to the cited authority. The submission of incorrect, misleading, or nonexistent content to this, or any other, court is improper, unacceptable, and an abuse of the judicial process. And we do not consider fabricated authority in our evaluation of the merits. Affirmed.",
    cited_authorities=["Minn. R. Civ. App. P. 136.01", "State v. Bartylla, 755 N.W.2d 8 (Minn. 2008)", "Schoepke v. Alexander Smith & Sons Carpet Co., 187 N.W.2d 133 (Minn. 1971)"],
    summary="The Minnesota Court of Appeals affirms summary judgment for Ally Bank. At the end of the opinion, the court defines fabricated authority, identifies three nonexistent citations and many unsupported legal propositions in Ngouambe’s pro se informal brief, and disregards them when evaluating the merits.",
    incident={"conduct":"Self-represented appellant filed an informal brief with three nonexistent authority citations and many propositions not reasonably attributable to cited sources.", "outcome":"other", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

add(
    109,
    decision_id="wawd-2026-ledoux-v-outliers-sanctions",
    case_name="LeDoux v. Outliers, Inc.",
    court="United States District Court for the Western District of Washington",
    court_code="wawd",
    court_level="federal-district",
    state="WA",
    date_filed="2026-07-24",
    docket_number="3:24-cv-05808-TMC",
    document_type="order",
    topics=["fabricated-citations", "evidence-authentication", "competence-fees"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    ai_tool_named="ChatGPT and Claude",
    tracker_slug="ledoux-v-outliers",
    disposition="The court sanctioned attorney Jocelyn Stewart $3,000 and required citation certifications after unverified ChatGPT and Claude outputs.",
    ai_passage="In November and December 2025, Plaintiff Joann LeDoux submitted multiple filings containing dozens of inaccurate factual and legal citations which appeared “hallucinated” by a generative artificial intelligence tool. On February 4, 2026, the Court ordered Plaintiff’s counsel, Ms. Jocelyn Stewart, to show cause and explain why she should not be sanctioned for these errors. ... Ms. Stewart filed a sworn declaration on March 4, explaining that she had used two artificial intelligence programs—ChatGPT and Claude—to generate the false citations, that she was unaware of any falsities when she submitted the documents, and that she “accept[s] full responsibility for the errors” and has “changed [her] practices to ensure this does not happen again.” ... On February 4, 2026, the Court found that Ms. Stewart “submitted dozens of inaccurate factual and legal citations across at least five different filings.” These errors included citations to nonexistent sources, as well as fictitious quotations from real sources. Concerningly, two of Plaintiff’s expert reports contained citations to the same nonexistent or misattributed academic articles. ... She avers that she used Claude and ChatGPT to draft her submissions in this case, that these programs generated the false citations identified in the Court’s order, and that she “did not verify the output against the source before filing.” ... Here, Ms. Stewart’s actions warrant significant sanctions. Ms. Stewart submitted dozens of false citations throughout four briefs and two expert reports. ... The Court thus finds that the below sanctions are necessary to address Ms. Stewart’s conduct. The Court ORDERS the following sanctions for violation of Federal Rule of Civil Procedure 11(b): 1. Attorney Jocelyn Stewart is personally sanctioned in the amount of $3,000. ... 2. Ms. Stewart shall include a certification with all subsequent briefing in this case stating that all citations have been verified and accurately reflect the propositions put forth. 3. Ms. Stewart shall provide a copy of this order to Plaintiff Joann LeDoux and file a certification with the Court that she has done so no later than July 28, 2026.",
    cited_authorities=["Fed. R. Civ. P. 11(b)", "Washington State Bar Association Advisory Opinion 202505", "Chaney v. Transdev Services Inc., 2026 WL 1146736 (C.D. Cal. Apr. 28, 2026)", "Gerke v. Travelers Casualty Insurance Co. of America, 289 F.R.D. 316 (D. Or. 2013)", "Parker, 2025 WL 4228413"],
    summary="The Western District of Washington sanctions Jocelyn Stewart in the LeDoux litigation. The order finds Stewart used ChatGPT and Claude without verifying outputs, causing dozens of false citations across briefs and expert reports, and imposes a $3,000 personal sanction plus future citation certifications.",
    incident={"conduct":"Plaintiff’s counsel used ChatGPT and Claude to generate dozens of false citations and citation tables in briefs and expert reports without verification.", "outcome":"sanctions", "actor":"lawyer", "monetary_penalty":3000, "currency":"USD", "ai_tool":"ChatGPT and Claude"},
)

add(
    110,
    decision_id="caed-2026-graves-v-pacific-gas-electric",
    case_name="Graves v. Pacific Gas & Electric Co.",
    court="United States District Court for the Eastern District of California",
    court_code="caed",
    court_level="federal-district",
    state="CA",
    date_filed="2026-07-24",
    citation="2026 WL 2138081",
    docket_number="2:25-cv-02558-DC-SCR",
    document_type="report-and-recommendation",
    topics=["fabricated-citations", "pro-se-ai-use"],
    primary_topic="fabricated-citations",
    court_used_ai=False,
    disposition="The magistrate judge recommended dismissal with leave to amend, granted leave to amend, denied e-filing, and warned Graves about nonexistent cases.",
    ai_passage="Plaintiff cites to Boling v. Pub. Utils. Comm'n, 105 Cal.App.3d 805 (1980) and Loving v. Cnty. of Stanislaus, 33 Cal.App.5th 444 (2019), which are not real cases. Plaintiff also cites to Pierce v. Cnty. of Orange, 526 F.3d 1190 (9th Cir. 2008), which does not discuss statute of limitations or continuing violation issues. At the hearing on these motions, the undersigned admonished Plaintiff about the danger of using Artificial Intelligence tools for legal research and writing and Plaintiff's obligation to ensure that all legal citations are legitimate. Future citations to non-existent cases may subject Plaintiff to an order to show cause as to why she should not be sanctioned under Rule 11 of the Federal Rules of Civil Procedure. ... IT IS HEREBY ORDERED that: 1. Plaintiff's motions to e-file (ECF Nos. 4 & 21) are DENIED. ... IT IS HEREBY RECOMMENDED that: 1. Defendants’ motion to dismiss (ECF No. 5) be GRANTED; 2. Plaintiff's motion for leave to amend (ECF No. 14) be GRANTED and Plaintiff allowed 21 days to file a First Amended Complaint.",
    cited_authorities=["Boling v. Public Utilities Commission, 105 Cal.App.3d 805 (1980)", "Loving v. County of Stanislaus, 33 Cal.App.5th 444 (2019)", "Pierce v. County of Orange, 526 F.3d 1190 (9th Cir. 2008)", "Fed. R. Civ. P. 11"],
    summary="The Eastern District of California recommends dismissing Graves’s utility-pole claims with leave to amend and denies e-filing. A footnote identifies two nonexistent California cases, notes that Pierce does not support the cited limitations point, and warns about AI research and Rule 11 sanctions.",
    incident={"conduct":"Self-represented plaintiff cited two nonexistent California cases and mischaracterized Pierce on limitations and continuing-violation issues.", "outcome":"warning", "actor":"litigant-in-person", "monetary_penalty":None, "currency":None, "ai_tool":None},
)

out_path = Path("work/agents/decisions-t1-s1.jsonl")
existing_ids = set()
if out_path.exists():
    with out_path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                existing_ids.add(json.loads(line)["decision_id"])

new_rows = [r for r in rows if r["decision_id"] not in existing_ids]
with out_path.open("a", encoding="utf-8") as f:
    for row in new_rows:
        f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

print(f"prepared={len(rows)} appended={len(new_rows)} skipped_existing={len(rows)-len(new_rows)}")
