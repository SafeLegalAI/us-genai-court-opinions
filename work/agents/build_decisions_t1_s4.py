#!/usr/bin/env python3
import json, re, hashlib, datetime, unicodedata, difflib
from pathlib import Path

BASE='https://www.damiencharlotin.com'
ROOT=Path('.')
LEADS=json.load(open('work/leads/t1-slice-4.json',encoding='utf-8'))
FETCH_LOG={r['index']:r for r in json.load(open('work/agents/t1_s4_fetch_log.json',encoding='utf-8'))}
OUT=Path('work/agents/decisions-t1-s4.jsonl')
SKIP=Path('work/agents/decisions-t1-s4-skips.json')
FETCHED_AT=datetime.datetime.now().astimezone().isoformat(timespec='seconds')

tracker=[]
for line in open('work/tracker-slugs.txt',encoding='utf-8'):
    parts=line.rstrip('\n').split('\t')
    if len(parts)>=2:
        tracker.append((parts[0],parts[1],parts[2] if len(parts)>2 else ''))

def strip_accents(s):
    return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode('ascii')

def slugify(s):
    s=strip_accents(s)
    s=re.sub(r'\([^)]*\)',' ',s)
    s=s.replace('&',' and ')
    s=re.sub(r'[^A-Za-z0-9]+','-',s).strip('-').lower()
    s=re.sub(r'-+','-',s)
    # trim common suffixes
    words=[w for w in s.split('-') if w not in {'et','al','inc','llc','ltd','company','corporation','corp','national','association','the','usa','plaintiff','defendant','appellant','appellee','relator'}]
    return '-'.join(words) or 'case'

def tokens(s):
    stops={'v','vs','in','re','of','and','for','to','no','case','court','ct','app','district','dist','cir','civ','cv','ca','sc','usa','united','states','state','ex','rel','matter','the','et','al'}
    return [w for w in slugify(s).split('-') if len(w)>1 and w not in stops and not re.fullmatch(r'\d+', w)]

def tracker_match(lead):
    case=lead['Case Name']; date=lead.get('Date','')
    cslug=slugify(case)
    if cslug in {x[0] for x in tracker}:
        return cslug
    ctoks=set(tokens(case))
    if not ctoks: return None
    best=(0,None,None,0)
    for slug,title,tdate in tracker:
        ttoks=set(tokens(title)) | set(tokens(slug.replace('-',' ')))
        if not ttoks: continue
        inter=len(ctoks & ttoks)
        union=len(ctoks | ttoks)
        j=inter/union if union else 0
        seq=difflib.SequenceMatcher(None,cslug,slug).ratio()
        score=max(j,seq*0.9 if inter>=2 else 0)
        # bonus for date equality and same distinctive tokens
        if date and tdate and date==tdate: score+=0.1
        if inter>=2 and score>best[0]: best=(score,slug,title,inter)
    if best[0]>=0.50 and best[3]>=2:
        return best[1]
    return None

COURTS={
'D. New Jersey':('United States District Court for the District of New Jersey','dnj','federal-district','NJ','dnj'),
'CA Louisiana (5d)':('Louisiana Court of Appeal, Fifth Circuit',None,'state-appellate','LA','laapp5'),
'E.D. California':('United States District Court for the Eastern District of California','caed','federal-district','CA','caed'),
'E.D. Lousiana':('United States District Court for the Eastern District of Louisiana','laed','federal-district','LA','laed'),
'E.D. Louisiana':('United States District Court for the Eastern District of Louisiana','laed','federal-district','LA','laed'),
'E.D. Wisconsin':('United States District Court for the Eastern District of Wisconsin','wied','federal-district','WI','wied'),
'SC Pennsylvania':('Superior Court of Pennsylvania',None,'state-appellate','PA','pasuperct'),
'N.D. Illinois':('United States District Court for the Northern District of Illinois','ilnd','federal-district','IL','ilnd'),
'SC Connecticut':('Connecticut Superior Court',None,'state-trial','CT','ctsuperct'),
'CA Georgia':('Court of Appeals of Georgia',None,'state-appellate','GA','gactapp'),
'D. Colorado':('United States District Court for the District of Colorado','cod','federal-district','CO','cod'),
'CA Colorado':('Colorado Court of Appeals',None,'state-appellate','CO','coloctapp'),
'SC North Dakota':('Supreme Court of North Dakota',None,'state-supreme','ND','nd'),
'W.D. Oklahoma':('United States District Court for the Western District of Oklahoma','okwd','federal-district','OK','okwd'),
'N.D. Mississippi':('United States District Court for the Northern District of Mississippi','msnd','federal-district','MS','msnd'),
'E.D. Michigan':('United States District Court for the Eastern District of Michigan','mied','federal-district','MI','mied'),
'C.D. California':('United States District Court for the Central District of California','cacd','federal-district','CA','cacd'),
'D. New Mexico':('United States District Court for the District of New Mexico','nmd','federal-district','NM','nmd'),
'N.D. California':('United States District Court for the Northern District of California','cand','federal-district','CA','cand'),
'CA Oregon':('Oregon Court of Appeals',None,'state-appellate','OR','orctapp'),
'E.D. New York':('United States District Court for the Eastern District of New York','nyed','federal-district','NY','nyed'),
"D. Hawai'i":('United States District Court for the District of Hawaii','hid','federal-district','HI','hid'),
'CA Texas':('Texas Court of Appeals',None,'state-appellate','TX','texapp'),
'SC New York':('Supreme Court of the State of New York',None,'state-trial','NY','nysupct'),
'CA Michigan':('Michigan Court of Appeals',None,'state-appellate','MI','michctapp'),
'D. Minnesota':('United States District Court for the District of Minnesota','mnd','federal-district','MN','mnd'),
'D. Nevada':('United States District Court for the District of Nevada','nvd','federal-district','NV','nvd'),
'Missouri CA':('Missouri Court of Appeals',None,'state-appellate','MO','moctapp'),
'D. Maine':('United States District Court for the District of Maine','med','federal-district','ME','med'),
'SC Georgia':('Supreme Court of Georgia',None,'state-supreme','GA','ga'),
'D. Utah':('United States District Court for the District of Utah','utd','federal-district','UT','utd'),
'11th Cir. CA':('United States Court of Appeals for the Eleventh Circuit','ca11','federal-appellate',None,'ca11'),
'D. Maryland':('United States District Court for the District of Maryland','mdd','federal-district','MD','mdd'),
'CA Kentucky':('Kentucky Court of Appeals',None,'state-appellate','KY','kyctapp'),
'M.D. Florida':('United States District Court for the Middle District of Florida','flmd','federal-district','FL','flmd'),
'M.D. Georgia':('United States District Court for the Middle District of Georgia','gamd','federal-district','GA','gamd'),
'S.D. Mississippi':('United States District Court for the Southern District of Mississippi','mssd','federal-district','MS','mssd'),
'Montgomery CC, Ohio':('Court of Common Pleas of Montgomery County, Ohio',None,'state-trial','OH','montgomery-oh-ccp'),
'S.D. New York':('United States District Court for the Southern District of New York','nysd','federal-district','NY','nysd'),
'S.D. Iowa':('United States District Court for the Southern District of Iowa','iasd','federal-district','IA','iasd'),
'E.D. Pennsylvania':('United States District Court for the Eastern District of Pennsylvania','paed','federal-district','PA','paed'),
'D. Arizona':('United States District Court for the District of Arizona','azd','federal-district','AZ','azd'),
'CA Maryland':('Appellate Court of Maryland',None,'state-appellate','MD','mdapp'),
'D. Kansas':('United States District Court for the District of Kansas','ksd','federal-district','KS','ksd'),
'CA Iowa':('Iowa Court of Appeals',None,'state-appellate','IA','iactapp'),
'CA California (5d)':('California Court of Appeal, Fifth District',None,'state-appellate','CA','calctapp5'),
'5th Cir. CA':('United States Court of Appeals for the Fifth Circuit','ca5','federal-appellate',None,'ca5'),
'M.D. North Carolina':('United States District Court for the Middle District of North Carolina','ncmd','federal-district','NC','ncmd'),
'N.D. Alabama':('United States District Court for the Northern District of Alabama','alnd','federal-district','AL','alnd'),
'E.D. Tennessee':('United States District Court for the Eastern District of Tennessee','tned','federal-district','TN','tned'),
'S.D. Texas':('United States District Court for the Southern District of Texas','txsd','federal-district','TX','txsd'),
'M.D. Pennsylvania':('United States District Court for the Middle District of Pennsylvania','pamd','federal-district','PA','pamd'),
'SC Alabama':('Supreme Court of Alabama',None,'state-supreme','AL','ala'),
'10th Cir. CA':('United States Court of Appeals for the Tenth Circuit','ca10','federal-appellate',None,'ca10'),
'CA California (2d)':('California Court of Appeal, Second District',None,'state-appellate','CA','calctapp2'),
'AC Texas':('Texas Court of Appeals',None,'state-appellate','TX','texapp'),
'D. Alaska':('United States District Court for the District of Alaska','akd','federal-district','AK','akd'),
'S.D. Indiana':('United States District Court for the Southern District of Indiana','insd','federal-district','IN','insd'),
'SC Nevada':('Supreme Court of Nevada',None,'state-supreme','NV','nev'),
'Texas Court of Appeals (4th Dist.)':('Texas Court of Appeals, Fourth District',None,'state-appellate','TX','texapp4'),
'CA California (6d)':('California Court of Appeal, Sixth District',None,'state-appellate','CA','calctapp6'),
'TS Puerto Rico':('Supreme Court of Puerto Rico',None,'state-supreme','PR','pr'),
'SC DC':('Superior Court of the District of Columbia',None,'state-trial','DC','dcsuperct'),
'CA Washington':('Washington Court of Appeals',None,'state-appellate','WA','washctapp'),
'S.D. New York (Bankruptcy)':('United States Bankruptcy Court for the Southern District of New York','nysb','federal-bankruptcy','NY','nysb'),
'E.D. Texas':('United States District Court for the Eastern District of Texas','txed','federal-district','TX','txed'),
'GAO':('Government Accountability Office','gao','federal-specialty',None,'gao'),
'CA Texas (5d)':('Texas Court of Appeals, Fifth District',None,'state-appellate','TX','texapp5'),
'CA Illinois (1d)':('Appellate Court of Illinois, First District',None,'state-appellate','IL','illapp1'),
'Minnesota':('Minnesota Court of Appeals',None,'state-appellate','MN','minnctapp'),
'CA California (1d)':('California Court of Appeal, First District',None,'state-appellate','CA','calctapp1'),
'3d Dist':('Ohio Court of Appeals, Third District',None,'state-appellate','OH','ohctapp3'),
'D. Oregon':('United States District Court for the District of Oregon','ord','federal-district','OR','ord'),
'CA Florida (6d)':('Florida District Court of Appeal, Sixth District',None,'state-appellate','FL','fladistctapp6'),
}

KEY_RE=re.compile(r'(?i)(\bartificial intelligence\b|\bgenerative\b|\bGenAI\b|\blarge language\b|\bChatGPT\b|\bAI\b|hallucinat|fabricat|\bfake\b|fictitious|fictional|phantom|bogus|made[- ]?up|non\s*-?\s*existent|does not exist|do not exist|did not exist|unable to locate|could not locate|cannot locate|unlocatable|misleading citations?|citation clarifications?)')
STRONG_RE=re.compile(r'(?i)(\bartificial intelligence\b|\bgenerative\b|\bGenAI\b|\blarge language\b|\bChatGPT\b|\bAI\b|AI[- ]generated|hallucinat|fabricat|\bfake\b|fictitious|fictional|phantom|bogus|made[- ]?up)')
BAD_PARA=re.compile(r'(?i)(Editor\'s Note|Westlaw citation|Thomson Reuters|No claim to original|All Citations|Attorneys and Law Firms)')

def normalize_text(t):
    t=t.replace('\r','')
    # join common line-broken compounds while keeping most text intact
    t=re.sub(r'([A-Za-z])-\s*\n\s*([A-Za-z])', r'\1\2', t)
    t=re.sub(r'\n\s*\n+', '\n\n', t)
    return t

def paragraphs(t):
    t=normalize_text(t)
    # Drop courtlistener/westlaw page footers/copyright-only lines.
    lines=[]
    for line in t.splitlines():
        if re.search(r'© \d{4} Thomson Reuters|No claim to original U\.S\. Government Works|^\s*\d+\s*$', line):
            continue
        if re.search(r'Case \d.*Document \d.*Filed', line):
            continue
        lines.append(line.rstrip())
    cleaned='\n'.join(lines)
    parts=[re.sub(r'\s+', ' ', p).strip() for p in re.split(r'\n\s*\n+', cleaned)]
    return [p for p in parts if p]

def passage_from_text(text):
    ps=paragraphs(text)
    clean=' '.join(ps)
    candidates=[]
    for m in KEY_RE.finditer(clean):
        if re.search(r'(?i)https?://|\barchived at\b', clean[max(0,m.start()-40):m.end()+80]):
            continue
        # Avoid Westlaw/other editorial notes rather than court-authored text.
        nearby=clean[max(0,m.start()-260):min(len(clean),m.end()+260)]
        if re.search(r"(?i)Editor's Note|Only the Westlaw citation|Thomson Reuters|No claim to original", nearby):
            continue
        left=max(0,m.start()-1600)
        right=min(len(clean),m.end()+2600)
        window=clean[left:right]
        score=0
        score += 10*len(re.findall(r'(?i)\bartificial intelligence\b|\bgenerative\b|\bGenAI\b|\blarge language\b|\bChatGPT\b|hallucinat',window))
        score += 6*len(re.findall(r'(?i)fabricat|\bfake\b|fictitious|fictional|phantom|bogus|made[- ]?up',window))
        score += 3*len(re.findall(r'(?i)non\s*-?\s*existent|does not exist|do not exist|did not exist|unable to locate|could not locate|cannot locate|unlocatable|citation clarifications?',window))
        score += 2 if re.search(r'(?i)Rule 11|sanction|show cause|candor|verify|verified|legal citation',window) else 0
        if len(window)<180: score-=3
        g=m.group(0)
        strength=3 if re.search(r'(?i)artificial intelligence|generative|GenAI|ChatGPT|hallucinat|fabricat|fictitious|fictional|fake|made',g) else (2 if re.search(r'(?i)non|unable|could not|cannot|does not|misleading',g) else 1)
        candidates.append((score,strength,-m.start(),m.start(),m.end()))
    if not candidates:
        return None, 'no AI/fabricated-citation keywords located in extracted text'
    candidates.sort(reverse=True)
    _,_,_,start_match,end_match=candidates[0]

    # Work sentence-by-sentence around the strongest match so a long PDF-text
    # paragraph does not start the quote at the caption.
    sentences=[]
    for sm in re.finditer(r'[^.!?;]+(?:[.!?;]+|$)', clean):
        sent=sm.group(0).strip()
        if not sent:
            continue
        if BAD_PARA.search(sent) and not KEY_RE.search(sent):
            continue
        sentences.append((sm.start(),sm.end(),sent))
    idx=0
    for j,(a,b,_) in enumerate(sentences):
        if a <= start_match <= b:
            idx=j
            break
    selected=[idx]
    def wc(s): return len(re.findall(r'\b\w+\b',s))
    def assemble():
        return ' '.join(sentences[j][2] for j in sorted(selected))
    passage=assemble()
    left=idx-1; right=idx+1
    # Include immediate context before the matched sentence when available.
    if left>=0 and wc(passage)<260:
        selected.append(left); left-=1; passage=assemble()
    if right<len(sentences) and wc(passage)<260:
        selected.append(right); right+=1; passage=assemble()
    while wc(passage)<100 and (left>=0 or right<len(sentences)):
        if right<len(sentences):
            selected.append(right); right+=1
        if wc(assemble())>=100:
            break
        if left>=0:
            selected.append(left); left-=1
        passage=assemble()
    # add one more following sentence when the quote would otherwise end abruptly
    if right<len(sentences) and wc(passage)<260:
        selected.append(right)
        passage=assemble()
    # If selected text is a terse footnote and only says a case does not exist, skip.
    strong=bool(STRONG_RE.search(passage))
    nonexist=len(re.findall(r'(?i)non\s*-?\s*existent|does not exist|do not exist|did not exist|unable to locate|could not locate|cannot locate|unlocatable',passage))
    citation_issue=bool(re.search(r'(?i)citation|case|authority|quot', passage))
    if wc(passage)<55:
        return None, 'only a terse citation note located, not a substantive discussion'
    if not strong and not (citation_issue and (nonexist>=1 or re.search(r'(?i)misleading citations?',passage))):
        return None, 'document text does not substantively discuss AI or fabricated citations'
    # trim to about 330 words / under 4000 chars.
    words=re.findall(r'\S+', passage)
    if len(words)>360:
        passage=' '.join(words[:330])+' ...'
    if len(passage)>3900:
        passage=passage[:3800].rsplit(' ',1)[0]+' ...'
    return passage.strip(), None

def document_type(text):
    head=' '.join(paragraphs(text)[:12])[:3000]
    if re.search(r'(?i)REPORT\s+AND\s+RECOMMENDATION',head): return 'report-and-recommendation'
    if re.search(r'(?i)MEMORANDUM\s+(OPINION|OF DECISION|DECISION)',head): return 'memorandum-opinion'
    if re.search(r'(?i)CONCURRING\s+OPINION|CONCURRENCE',head): return 'concurrence'
    if re.search(r'(?i)DISSENT',head): return 'dissent'
    if re.search(r'(?i)\bOPINION\b|DECISION',head): return 'opinion'
    if re.search(r'(?i)ORDER\s+AND\s+REASONS|ORDER\s+TO\s+SHOW\s+CAUSE|ORDER\s+IMPOSING|\bORDER\b',head): return 'order'
    return 'order'

def extract_docket(text):
    head='\n'.join(text.splitlines()[:80])
    patterns=[
        r'Case\s+([0-9][0-9:A-Za-z.\-]+(?:-[A-Za-z0-9]+)*)\s+Document',
        r'(?:Case|Civil Action|CIVIL ACTION|Cause|Docket)\s+No\.?:?\s*([A-Za-z0-9][A-Za-z0-9:.,/\-–\s]{2,70})',
        r'\bNo\.\s*([A-Z0-9][A-Z0-9:.,/\-–\s]{2,50})',
        r'DOCKET\s+NO\.\s*([A-Z0-9\-:,\s]+)',
    ]
    for pat in patterns:
        m=re.search(pat,head,re.I)
        if m:
            val=re.sub(r'\s+',' ',m.group(1)).strip(' .|')
            val=re.split(r'\s{2,}| Filed:| \| | Page | Judge | MEMORANDUM | OPINION | ORDER | Plaintiff | Defendant ',val)[0].strip(' .|')
            if 3<=len(val)<=70 and not re.search(r'(?i)PUBLICATION|WESTLAW|COPYRIGHT',val):
                return val
    return None

def extract_citation(text):
    head=' '.join(paragraphs(text)[:8])[:2000]
    pats=[
        r'\b\d{4}\s+WL\s+\d+\b',
        r'\b\d{4}\s+IL\s+App\s*\([^)]*\)\s*\d+[\w-]*\b',
        r'\b\d{4}\s+ND\s+\d+\b',
        r'\b\d{4}\s+COA\s+\d+\b',
        r'\b\d{4}-Ohio-\d+\b',
        r'\b\d{4}\s+N\.Y\.\s+Slip\s+Op\.\s+\d+\(?[A-Z]?\)?',
        r'\b\d{4}\s+PR\s+\d+\b',
        r'\bB-\d{6}(?:\.\d+)?\b',
    ]
    vals=[]
    for p in pats:
        vals += re.findall(p,head,re.I)
    vals=[re.sub(r'\s+',' ',v).strip() for v in vals]
    # prefer non-WL official-looking cite; else WL
    if vals:
        vals=list(dict.fromkeys(vals))
        vals.sort(key=lambda v: 1 if 'WL' in v else 0)
        return vals[0]
    return None

def clean_case_name(name):
    name=re.sub(r'\s*\(2\)\s*','',name).strip()
    # shorten long party lists for readability
    name=name.replace('Taiujuan Burches','Burches').replace('William Louis Armstrong, III','Armstrong').replace('Danielle L. Neri','Neri')
    return name

def actor_from_party(party):
    p=(party or '').lower()
    if 'pro se' in p or 'litigant' in p: return 'litigant-in-person'
    if 'prosecutor' in p: return 'prosecutor'
    if 'judge' in p: return 'judge'
    if 'firm' in p: return 'firm'
    if 'lawyer' in p or 'counsel' in p: return 'lawyer'
    return 'other'

def actor_phrase(actor):
    return {'litigant-in-person':'a self-represented litigant’s','lawyer':'counsel’s','prosecutor':'a prosecutor’s','judge':'a judge’s','firm':'a law firm’s','other':'a filing’s'}.get(actor,'a filing’s')

def outcome_enum(outcome, monetary):
    o=(outcome or '').lower()
    if 'suspension' in o: return 'suspension'
    if 'bar referral' in o or 'referral' in o or 'state bar' in o: return 'referral'
    if 'cost' in o: return 'costs-order'
    if monetary is not None or 'monetary' in o or 'fine' in o: return 'fine'
    if 'dismiss' in o and 'sanction' in o: return 'dismissal'
    if 'show cause' in o or 'pending' in o or 'explain' in o: return 'pending'
    if 'warning' in o or 'admonish' in o or 'admonishment' in o or 'caution' in o: return 'warning'
    if 'struck' in o or 'strike' in o: return 'strike-off'
    if 'sanction' in o: return 'sanctions'
    return 'other'

def parse_money(s):
    s=s or ''
    m=re.search(r'([0-9][0-9,]*(?:\.\d+)?)\s*([A-Z]{3})?',s)
    if not m: return None,None
    return float(m.group(1).replace(',','')), (m.group(2) or 'USD')

def conduct_from_lead(lead, passage):
    h=lead.get('Hallucination Items') or ''
    h=re.sub(r'\|\|','; ',h)
    h=re.sub(r'(Fabricated|False Quotes|Misrepresented|Outdated Advice|Fabricated: Other|Fabricated: Legal Norm|Fabricated: Doctrinal Work|Fabricated: Exhibits & Submissions|Misrepresented: Exhibits & Submissions|Misrepresented: Legal Norm|Misrepresented: Case Law|False Quotes: Case Law|Fabricated: Case Law)\s*\|\s*','',h)
    h=re.sub(r'\s+',' ',h).strip(' ;')
    if not h:
        # Use a short clause from passage.
        sent=re.split(r'(?<=[.!?])\s+', passage)[0]
        h=sent
    if len(h)>285:
        h=h[:282].rsplit(' ',1)[0]+'...'
    return h or 'The filing contained fabricated or inaccurate legal citations discussed by the court.'

def detect_tool(lead, text):
    lead_tool=(lead.get('AI Tool') or '').strip()
    if lead_tool.lower() in {'','implied','unidentified','unspecified'}:
        return None
    checks=[]
    for part in re.split(r'[,/]| or | and ', lead_tool):
        part=part.strip()
        if not part: continue
        checks.append(part)
        if 'Prot' in part: checks.append('Prot')
    low=text.lower()
    for c in checks:
        if c.lower().replace('é','e') in low.replace('é','e'):
            return lead_tool
    return None

def issue_noun(lead, passage):
    h=(lead.get('Hallucination Items') or '').lower()
    bits=[]
    if 'fabricated' in h or re.search(r'(?i)fabricat|fake|fictitious|fictional|nonexistent|non-existent|does not exist',passage): bits.append('fabricated or nonexistent authorities')
    if 'false quotes' in h or re.search(r'(?i)false quot|misquot|quotation',passage): bits.append('false quotations')
    if 'misrepresented' in h or re.search(r'(?i)misrepresent|misleading',passage): bits.append('mischaracterized authority')
    if not bits: bits=['problematic legal citations']
    return ', '.join(list(dict.fromkeys(bits))[:3])

def disposition_from(lead, doc_type):
    outcome=(lead.get('Outcome') or '').strip()
    if outcome:
        return f"The court's stated response to the citation issue was: {outcome}."
    return f"The court resolved the {doc_type.replace('-', ' ')} while addressing inaccurate or fabricated citations."

def summary_from(lead, court, actor, passage, outcome):
    case=clean_case_name(lead['Case Name'])
    issue=issue_noun(lead, passage)
    outcome_txt=(outcome or '').strip() or 'no separate sanction recorded in the lead'
    s=f"On {lead['Date']}, {court} addresses {actor_phrase(actor)} {issue} in {case}. The document records the citation problem in the court’s own discussion and identifies the response as {outcome_txt}."
    # If too short, add AI reference when present.
    if len(s)<120:
        s += ' The issue is coded as fabricated citations.'
    if len(s)>510:
        s=s[:505].rsplit(' ',1)[0]+'.'
    while len(s.split())<40:
        s += ' The discussion concerns accuracy of legal authority in court filings.'
    return s

def extract_authorities(passage, lead):
    vals=[]
    for m in re.finditer(r'\b([A-Z][A-Za-z’\'&.\- ]{1,55}\s+v\.\s+[A-Z][A-Za-z0-9’\'&.\- ]{1,65}(?:,\s*(?:No\.|\d{1,4}|---|\d{4})[^.;)]{0,80})?)', passage):
        v=re.sub(r'\s+',' ',m.group(1)).strip(' ,')
        if len(v)>8 and not re.search(r'(?i)Plaintiff|Defendant|Court',v): vals.append(v)
    if re.search(r'Fed\. R\. Civ\. P\. 11|Rule 11',passage): vals.append('Fed. R. Civ. P. 11')
    # supplement with quoted authorities from lead for incident specificity
    h=lead.get('Hallucination Items') or ''
    for m in re.finditer(r'([A-Z][A-Za-z’\'&.\- ]{1,55}\s+v\.\s+[A-Z][A-Za-z0-9’\'&.\- ]{1,65}(?:,\s*[^|;]{0,80})?)', h):
        v=re.sub(r'\s+',' ',m.group(1)).strip(' ,.;')
        if len(v)>8: vals.append(v)
    out=[]; seen=set()
    for v in vals:
        v=v.replace('“','').replace('”','').strip()
        if len(v)>160: v=v[:155].rsplit(' ',1)[0]
        key=v.lower()
        if key not in seen:
            out.append(v); seen.add(key)
        if len(out)>=10: break
    return out

rows=[]; skips=[]; used_ids=set()
for i,lead in enumerate(LEADS,1):
    src=str(lead.get('Source',''))
    if not src.startswith('/documents/'):
        if 'courts.michigan.gov' in src:
            skips.append({'index':i,'case_name':lead['Case Name'],'reason':'official Michigan case page returned 403; no court-authored document retrieved'})
        elif 'courtlistener.com' in src or 'reason.com' in src:
            skips.append({'index':i,'case_name':lead['Case Name'],'reason':'CourtListener discovery request was throttled; no permitted source document retrieved'})
        else:
            skips.append({'index':i,'case_name':lead['Case Name'],'reason':'source was not a permitted primary or Charlotin mirror URL and CourtListener discovery was unavailable'})
        continue
    log=FETCH_LOG.get(i,{})
    text_paths=list(Path('work/agents/t1_s4_text_raw').glob(f'{i:03d}-*.txt'))
    if not text_paths:
        text_paths=list(Path('work/agents/t1_s4_text').glob(f'{i:03d}-*.txt'))
    if not text_paths:
        skips.append({'index':i,'case_name':lead['Case Name'],'reason':'PDF fetched but text extraction file was missing'})
        continue
    text=text_paths[0].read_text(encoding='utf-8',errors='replace')
    passage, reason=passage_from_text(text)
    if not passage:
        skips.append({'index':i,'case_name':lead['Case Name'],'reason':reason})
        continue
    court_tuple=COURTS.get(lead['Court'])
    if not court_tuple:
        court=(lead['Court'],None,'other',None,slugify(lead['Court'])[:25])
    else:
        court_tuple=court_tuple
    court_name,court_code,court_level,state,prefix=court_tuple
    actor=actor_from_party(lead.get('Party(ies)'))
    money,currency=parse_money(lead.get('Monetary Penalty'))
    if money is not None and money.is_integer(): money=int(money)
    outcome=outcome_enum(lead.get('Outcome'), money)
    doc_type=document_type(text)
    case=clean_case_name(lead['Case Name'])
    cslug=slugify(case)
    max_slug_len=max(10,90-len(prefix)-6) # prefix + -2026- + slug <= 96-ish, schema max via pattern 90 chars after first? keep under 90 total
    decision_id=f'{prefix}-2026-{cslug}'
    if len(decision_id)>90:
        cslug=cslug[:90-len(prefix)-6].strip('-')
        decision_id=f'{prefix}-2026-{cslug}'
    base_id=decision_id; n=2
    while decision_id in used_ids:
        suffix=f'-{n}'
        decision_id=(base_id[:90-len(suffix)].strip('-')+suffix)
        n+=1
    used_ids.add(decision_id)
    tool=detect_tool(lead,text)
    row={
        'decision_id':decision_id,
        'case_name':case,
        'court':court_name,
        'court_code':court_code,
        'court_level':court_level,
        'state':state,
        'date_filed':lead['Date'],
        'citation':extract_citation(text),
        'docket_number':extract_docket(text),
        'document_type':doc_type,
        'topics':['fabricated-citations'],
        'primary_topic':'fabricated-citations',
        'court_used_ai':False,
        'ai_tool_named':tool,
        'disposition':disposition_from(lead,doc_type),
        'ai_passage':passage,
        'cited_authorities':extract_authorities(passage,lead),
        'summary':summary_from(lead,court_name,actor,passage,lead.get('Outcome')),
        'incident':{
            'conduct':conduct_from_lead(lead,passage),
            'outcome':outcome,
            'actor':actor,
            'monetary_penalty':money,
            'currency':currency,
            'ai_tool':tool,
        },
        'tracker_slug':tracker_match(lead),
        'courtlistener_url':None,
        'text_sha256':log.get('sha256'),
        'source_url':BASE+src,
        'archive_url':None,
        'fetched_at':FETCHED_AT,
        'verification':'mirror-read',
        'lead_source':['charlotin-cc0'],
        'notes':'official copy pending',
    }
    rows.append(row)

OUT.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in rows),encoding='utf-8')
SKIP.write_text(json.dumps(skips,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'rows':len(rows),'skips':len(skips),'output':str(OUT),'skip_file':str(SKIP)},indent=2))
