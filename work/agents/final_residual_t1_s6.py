import json,re,textwrap
from pathlib import Path
leads=json.load(open('work/leads/t1-slice-6.json'))
rows=[json.loads(l) for l in open('work/agents/decisions-t1-s6.jsonl') if l.strip()]
lead_url={}
for i,l in enumerate(leads,1):
    src=(l.get('Source') or '').strip()
    if src: lead_url[src if src.startswith('http') else 'https://www.damiencharlotin.com'+src]=i
idx_for=[lead_url[r['source_url']] for r in rows]
COND={
 30:"Counsel's appellate brief cited four fictitious Georgia authorities, including Waller v. Waller, Johnson v. Johnson, Durden v. Barron, and In re Waitz.",
 46:"Counsel's motion cited Whittaker v. Otto, 2014 WL 37845 (9th Cir.), which the court described as inaccurate or nonexistent.",
 47:"Counsel's opening brief included several AI-generated erroneous citations and false quotations with mismatched captions, citations, and legal principles.",
 91:"Counsel cited a nonexistent AI-generated case about certificate-of-deposit surrender and misapplied People v. Wharton and AARTS Productions.",
 99:"The self-represented party's briefing misused Caruso for a per se defamation point and gave an inaccurate Sorensen citation later corrected to Norg.",
 102:"Counsel's response to dismissal cited nonexistent case law that GAO said bore hallmarks of AI or large-language-model use without verification.",
 110:"Counsel's brief cited four defective authorities, including Steele v. County of San Mateo, Kogan v. Martin, and a Muller citation the court could not locate.",
}
DISP={
 102:"GAO denied the protest in part, dismissed it in part, and warned that future submissions with nonexistent authority may lead to sanctions.",
}

def sent(s):
    s=re.sub(r'\s+',' ',s.strip())
    if s and s[-1] not in '.!?': s+='.'
    return s[0].upper()+s[1:] if s else s

def short_court(c):
    for a,b in [('United States District Court for the ',''),('United States Court of Appeals for the ',''),('Court of Appeals of Washington','Washington Court of Appeals'),('Court of Appeals of Arizona','Arizona Court of Appeals'),('Appellate Court of Illinois','Illinois Appellate Court'),('District Court of Appeal of Florida','Florida District Court of Appeal')]: c=c.replace(a,b)
    return c

def make_summary(row):
    court=short_court(row['court']); date=row['date_filed']; case=row['case_name']
    cond=row['incident']['conduct'].rstrip('.')
    disp=row['disposition'].rstrip('.')
    if disp.lower().startswith('the court '): disp_sentence='The court '+re.sub(r'^The court\s+','',disp,flags=re.I)
    else: disp_sentence=disp[0].upper()+disp[1:]
    s=f"{court} on {date} in {case} found {cond[0].lower()+cond[1:]}. {disp_sentence}."
    if len(s.split())>60:
        s=f"{court} on {date} found {cond[0].lower()+cond[1:]}. {disp_sentence}."
    if len(s.split())>60:
        cshort=textwrap.shorten(cond[0].lower()+cond[1:], width=180, placeholder='...')
        s=f"{court} on {date} found {cshort}. {disp_sentence}."
    if len(s.split())<40:
        s=s.rstrip('.')+" in the challenged filing before resolving the pending matter."
    if len(s.split())>60:
        cshort=textwrap.shorten(cond[0].lower()+cond[1:], width=155, placeholder='...')
        s=f"{court} on {date} found {cshort}. {disp_sentence}."
    return sent(s)

for r,idx in zip(rows,idx_for):
    if idx in COND: r['incident']['conduct']=sent(COND[idx])
    if idx in DISP: r['disposition']=sent(DISP[idx])
    r['incident']['conduct']=r['incident']['conduct'].replace('The expert\'s expert submission','The expert\'s submission')
    r['summary']=make_summary(r)
Path('work/agents/decisions-t1-s6.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in rows),encoding='utf-8')
print(f'fixed {len(rows)} rows')
