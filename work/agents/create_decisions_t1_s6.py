import json, re, os, glob, hashlib, unicodedata, textwrap, datetime
from pathlib import Path

ROOT=Path('.')
LEADS=json.load(open('work/leads/t1-slice-6.json'))
MANIFEST=json.load(open('work/agents/t1-s6-fetch-manifest.json'))
texts={int(Path(f).name[:3]):Path(f) for f in glob.glob('work/agents/t1-s6-source_text/*.txt')}
manifest={r['idx']:r for r in MANIFEST}
TRACKER={line.split('\t')[0] for line in open('work/tracker-slugs.txt',encoding='utf-8') if line.strip()}
FETCHED_AT=datetime.datetime.now().astimezone().isoformat(timespec='seconds')
HOST='https://www.damiencharlotin.com'

COURTS={
 'D. New Jersey':('United States District Court for the District of New Jersey','njd','federal-district','NJ'),
 'C.D. California':('United States District Court for the Central District of California','cacd','federal-district','CA'),
 'CA Washington (d1)':('Court of Appeals of Washington, Division One','washctapp','state-appellate','WA'),
 'CA Washington':('Court of Appeals of Washington','washctapp','state-appellate','WA'),
 '6th Cir. CA':('United States Court of Appeals for the Sixth Circuit','ca6','federal-appellate',None),
 'Arizona State Bar':('State Bar of Arizona',None,'other','AZ'),
 'ASBCA':('Armed Services Board of Contract Appeals',None,'federal-specialty',None),
 'SC Pennsylvania':('Supreme Court of Pennsylvania','pa','state-supreme','PA'),
 'D. Nevada':('United States District Court for the District of Nevada','nvd','federal-district','NV'),
 'W.D. Virginia':('United States District Court for the Western District of Virginia','vawd','federal-district','VA'),
 'SC Rhode Island':('Supreme Court of Rhode Island','ri','state-supreme','RI'),
 'N.D. Texas':('United States District Court for the Northern District of Texas','txnd','federal-district','TX'),
 'CA Texas (9th)':('Texas Court of Appeals, Ninth District',None,'state-appellate','TX'),
 'CA Fourth Circuit':('United States Court of Appeals for the Fourth Circuit','ca4','federal-appellate',None),
 'W.D. Oklahoma':('United States District Court for the Western District of Oklahoma','okwd','federal-district','OK'),
 'S.D. New York':('United States District Court for the Southern District of New York','nysd','federal-district','NY'),
 'D. Massachusetts':('United States District Court for the District of Massachusetts','mad','federal-district','MA'),
 'W.D. Michigan':('United States District Court for the Western District of Michigan','miwd','federal-district','MI'),
 'CA Florida':('District Court of Appeal of Florida','fladistctapp','state-appellate','FL'),
 'AC Illinois':('Appellate Court of Illinois','illappct','state-appellate','IL'),
 'N.D. Illinois':('United States District Court for the Northern District of Illinois','ilnd','federal-district','IL'),
 'CA Mississippi':('Court of Appeals of Mississippi','missctapp','state-appellate','MS'),
 'D. Arizona':('United States District Court for the District of Arizona','azd','federal-district','AZ'),
 'CA California (2nd)':('California Court of Appeal, Second District','calctapp','state-appellate','CA'),
 'CA California':('California Court of Appeal','calctapp','state-appellate','CA'),
 'CA Indiana':('Indiana Court of Appeals','indctapp','state-appellate','IN'),
 'S.D. Illinois':('United States District Court for the Southern District of Illinois','ilsd','federal-district','IL'),
 'S.D. Indiana':('United States District Court for the Southern District of Indiana','insd','federal-district','IN'),
 'CA Georgia':('Court of Appeals of Georgia','gactapp','state-appellate','GA'),
 'W.D. Louisiana':('United States District Court for the Western District of Louisiana','lawd','federal-district','LA'),
 'D. Oregon':('United States District Court for the District of Oregon','ord','federal-district','OR'),
 'D. DC':('United States District Court for the District of Columbia','dcd','federal-district','DC'),
 'E.D. Louisiana':('United States District Court for the Eastern District of Louisiana','laed','federal-district','LA'),
 'CA Arizona':('Court of Appeals of Arizona','arizctapp','state-appellate','AZ'),
 'N.D. New York':('United States District Court for the Northern District of New York','nynd','federal-district','NY'),
 'C.D. California (Bankruptcy)':('United States Bankruptcy Court for the Central District of California','cacb','federal-bankruptcy','CA'),
 'E.D. North Carolina':('United States District Court for the Eastern District of North Carolina','nced','federal-district','NC'),
 'E.D. Michigan':('United States District Court for the Eastern District of Michigan','mied','federal-district','MI'),
 'E.D. Texas':('United States District Court for the Eastern District of Texas','txed','federal-district','TX'),
 'CA Alabama':('Alabama Court of Civil Appeals','alacivapp','state-appellate','AL'),
 'W.D. Texas':('United States District Court for the Western District of Texas','txwd','federal-district','TX'),
 'SC North Dakota':('Supreme Court of North Dakota','nd','state-supreme','ND'),
 'S.D. Ohio':('United States District Court for the Southern District of Ohio','ohsd','federal-district','OH'),
 'DCA Florida':('District Court of Appeal of Florida','fladistctapp','state-appellate','FL'),
 'W.D. Arkansas':('United States District Court for the Western District of Arkansas','arwd','federal-district','AR'),
 'D. Kansas':('United States District Court for the District of Kansas','ksd','federal-district','KS'),
 'CA Tennessee':('Court of Criminal Appeals of Tennessee','tenncrimapp','state-appellate','TN'),
 'N.D. Oklahoma':('United States District Court for the Northern District of Oklahoma','oknd','federal-district','OK'),
 'D. Utah':('United States District Court for the District of Utah','utd','federal-district','UT'),
 'E.D. California':('United States District Court for the Eastern District of California','caed','federal-district','CA'),
 'W.D. North Carolina':('United States District Court for the Western District of North Carolina','ncwd','federal-district','NC'),
 'CBCA':('Civilian Board of Contract Appeals',None,'federal-specialty',None),
 'S.D. Texas':('United States District Court for the Southern District of Texas','txsd','federal-district','TX'),
 'M.D. Florida':('United States District Court for the Middle District of Florida','flmd','federal-district','FL'),
 'SC Connecticut':('Supreme Court of Connecticut','conn','state-supreme','CT'),
 'CA Fifth Circuit':('United States Court of Appeals for the Fifth Circuit','ca5','federal-appellate',None),
 'GAO':('Government Accountability Office',None,'federal-specialty',None),
 'California SC':('Supreme Court of California','cal','state-supreme','CA'),
 'N.D. California':('United States District Court for the Northern District of California','cand','federal-district','CA'),
 'D. Colorado (Bankruptcy)':('United States Bankruptcy Court for the District of Colorado','cob','federal-bankruptcy','CO'),
 'E.D. Pennsylvania':('United States District Court for the Eastern District of Pennsylvania','paed','federal-district','PA'),
 'CA Kansas':('Kansas Court of Appeals','kanctapp','state-appellate','KS'),
 '10th Cir. CA':('United States Court of Appeals for the Tenth Circuit','ca10','federal-appellate',None),
 'D. Idaho':('United States District Court for the District of Idaho','idd','federal-district','ID'),
 'D. Alaska':('United States District Court for the District of Alaska','akd','federal-district','AK'),
}

OUTCOME_KEYWORDS={
 'bar referral':'referral', 'referral':'referral', 'disciplinary':'referral', 'professional sanction':'referral',
 'monetary sanction':'fine', 'monetary':'fine', 'fine':'fine',
 'costs':'costs-order', 'adverse costs':'costs-order', 'attorney fees':'costs-order', 'attorney fee':'costs-order',
 'show cause':'pending', 'upcoming':'pending', 'reserved':'pending',
 'dismissed':'dismissal', 'dismissal':'dismissal', 'dismiss':'dismissal',
 'warning':'warning', 'caution':'warning', 'admonishment':'warning', 'admonished':'warning', 'public admonishment':'warning', 'formal admonishment':'warning', 'reprimand':'warning',
 'brief struck':'other', 'brief str':'other', 'struck':'other', 'strike':'other', 'waived':'other', 'affirmed':'other', 'declined':'other',
}

KW=re.compile(r'(generative|artificial intelligence|\bAI\b|ChatGPT|hallucinat|non-existent|nonexistent|does not exist|do not exist|cases? that do(?:es)? not exist|fictitious|fabricat|fake|bogus|phantom|invented|made up|made-up|invalid citation|counterfeit|misquot|mis-cit|miscit)', re.I)
HIGH=re.compile(r'(sanction|warn|caution|admonish|show cause|strike|struck|refer|fine|cost|fee|dismiss|violat|Rule 11|candor|duty|hallucinat|artificial intelligence|\bAI\b)', re.I)
FOOTER=re.compile(r'(© 2026 Thomson Reuters|No claim to original U\.S\. Government Works|Westlaw|End of Document|All Citations|Only the Westlaw citation|NOT FOR PUBLICATION|Editor\'s Note:|Not Reported in|Slip Copy|Footnotes)', re.I)

def ascii_slug(s):
    s=unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().lower()
    s=re.sub(r'\([^)]*\)', ' ', s)
    s=s.replace('&',' and ')
    s=re.sub(r'\b(et al|inc|llc|l\.l\.c|corp|corporation|company|co|ltd|plaintiff|defendant|appellant|appellee|respondent|petitioner)\b',' ',s)
    s=re.sub(r'[^a-z0-9]+','-',s).strip('-')
    return s

def short_slug(case):
    s=ascii_slug(case)
    parts=s.split('-')
    # Keep through first six meaningful tokens, preserving v if present.
    keep=[]
    for p in parts:
        if not p: continue
        keep.append(p)
        if len([x for x in keep if x not in {'v','and','the','of','in','re'}])>=7: break
    return '-'.join(keep)[:62].strip('-') or 'decision'

def court_prefix(court_code, court):
    if court_code: return court_code
    mapping={'Armed Services Board of Contract Appeals':'asbca','Civilian Board of Contract Appeals':'cbca','Government Accountability Office':'gao','Texas Court of Appeals, Ninth District':'txapp','State Bar of Arizona':'azbar'}
    return mapping.get(court, ascii_slug(court).split('-')[0] if court else 'court')

def clean_line(line):
    line=line.replace('\x0c',' ')
    if FOOTER.search(line): return ''
    # Strip leading page stars and line noise, but keep paragraph symbols and bullets.
    line=re.sub(r'^\s*\*\d+\s*', '', line)
    line=re.sub(r'\s+', ' ', line).strip()
    return line

def clean_text(s):
    s=s.replace('\x0c',' ')
    s=re.sub(r'\s+', ' ', s).strip()
    s=re.sub(r' ?© 2026 Thomson Reuters\. No claim to original U\.S\. Government Works\.? ?', ' ', s)
    s=re.sub(r'\s+', ' ', s).strip()
    return s

def extract_passage(txt):
    raw_lines=txt.splitlines()
    lines=[clean_line(x) for x in raw_lines]
    hits=[]
    for i,l in enumerate(lines):
        if not l: continue
        if KW.search(l):
            # skip publisher/editor notes if there are later substantive hits
            score=1
            score += len(HIGH.findall(l))
            if i < 35 and 'Editor' in raw_lines[i]: score -= 3
            if re.search(r'(court|Court|counsel|brief|filing|sanction|warn|caution|AI|artificial|hallucinat)', l): score += 2
            hits.append((i,score))
    if any(i > 80 for i, _ in hits):
        hits=[h for h in hits if h[0] > 80]
    if not hits:
        # fallback to first 1200 chars from discussion
        return clean_text('\n'.join(lines[:40]))[:3500]
    # clusters within 14 lines
    clusters=[]
    cur=[hits[0]]
    for h in hits[1:]:
        if h[0]-cur[-1][0] <= 16:
            cur.append(h)
        else:
            clusters.append(cur); cur=[h]
    clusters.append(cur)
    # avoid only early editor notes when possible
    def cscore(c):
        s=sum(x[1] for x in c)+len(c)*2
        if c[-1][0] < 40: s-=10
        if any('artificial' in lines[i].lower() or re.search(r'\bAI\b', lines[i]) for i,_ in c): s+=4
        if any(re.search(r'sanction|warn|caution|admonish|show cause|refer|fine|cost|dismiss', lines[i], re.I) for i,_ in c): s+=4
        return s
    best=max(clusters,key=cscore)
    start=max(0,best[0][0]-3); end=min(len(lines),best[-1][0]+10)
    # expand if too short, but not too far
    while end-start < 18 and (start>0 or end<len(lines)):
        start=max(0,start-4); end=min(len(lines),end+4)
    chosen=[l for l in lines[start:end] if l]
    passage=clean_text(' '.join(chosen))
    # If the selected cluster is only a list item, append nearby next keyword cluster when close.
    if len(passage)<420:
        bi=clusters.index(best)
        if bi+1 < len(clusters) and clusters[bi+1][0][0]-best[-1][0] < 60:
            end2=min(len(lines), clusters[bi+1][-1][0]+10)
            passage=clean_text(' '.join(l for l in lines[start:end2] if l))
    if len(passage)>3900:
        # sentence-aware trim around first keyword after start
        m=KW.search(passage)
        center=m.start() if m else 0
        a=max(0, center-900); b=min(len(passage), center+2800)
        passage=passage[a:b]
        # snap roughly to sentence boundaries
        if a>0:
            k=passage.find('. ')
            if 0<=k<300: passage=passage[k+2:]
        if b<len(passage):
            k=passage.rfind('. ')
            if k>700: passage=passage[:k+1]
    if len(passage)<40:
        passage=clean_text(' '.join(l for l in lines[:30] if l))[:1000]
    return passage[:3990]

def extract_citation(txt):
    head='\n'.join(txt.splitlines()[:25])
    patterns=[r'\b20\d{2}\s+WL\s+\d+\b', r'\b20\d{2}\s+U\.S\.\s+Dist\.\s+LEXIS\s+\d+\b', r'\b20\d{2}\s+IL\s+App\s+\([^)]*\)\s+[\w-]+', r'\b20\d{2}-Ohio-\d+\b', r'\b20\d{2}\s+ND\s+\d+\b', r'\b\d+\s+F\.\s?Supp\.\s?\d*d?\s+\d+\b', r'\b\d+\s+Cal\.\s?\d+[A-Za-z.]*\s+\d+\b']
    for pat in patterns:
        m=re.search(pat, head, re.I)
        if m: return clean_text(m.group(0))
    return None

def extract_docket(lead, txt):
    # Prefer explicit docket/case number in lead's case name.
    cn=lead.get('Case Name','')
    m=re.search(r'\b(?:Nos?\.|Case No\.|B-)\s+([A-Z0-9][A-Z0-9:;.,\- /()]+)', cn, re.I)
    if m:
        val=m.group(0).strip().rstrip(').,')
        return val[:120]
    pats=[r'\bCase\s+([0-9]:[0-9]{2}-[a-z]{2}-[0-9A-Za-z-]+)',
          r'\b(?:Civil Action\s+)?No\.\s*([A-Za-z0-9][A-Za-z0-9:;.,\- /() ]{0,80}?)(?=\s{2,}|\||$)',
          r'\bCase No\.?:?\s*([A-Za-z0-9][A-Za-z0-9:;.,\- /() ]{0,80}?)(?=\s{2,}|Date\b|\||$)',
          r'\bCASE NO\.?:?\s*([A-Za-z0-9][A-Za-z0-9:;.,\- /() ]{0,80}?)(?=\s{2,}|Date\b|\||$)',
          r'\bB-\d{6}(?:\.\d+)?(?:;\s*B-\d{6}(?:\.\d+)?)?']
    for raw in txt.splitlines()[:120]:
        if not raw.strip() or len(raw)>220:
            continue
        for pat in pats:
            m=re.search(pat, raw, re.I)
            if m:
                val=m.group(0).strip()
                val=re.sub(r'\s+Date\b.*$', '', val, flags=re.I)
                val=re.sub(r'\s+', ' ', val)
                val=val.rstrip('|, .')
                if re.search(r'\bECF\s+Nos?\.', raw, re.I) or re.fullmatch(r'No\. \d{1,3}', val):
                    continue
                return val[:120]
    return None

def document_type(txt, court_level):
    head='\n'.join(txt.splitlines()[:130]).upper()
    if 'REPORT AND RECOMMENDATION' in head or 'REPORT & RECOMMENDATION' in head:
        return 'report-and-recommendation'
    if 'MEMORANDUM OPINION' in head or 'MEMORANDUM DECISION' in head:
        return 'memorandum-opinion'
    if 'OPINION' in head or 'DECISION' in head:
        return 'opinion' if court_level in {'state-appellate','state-supreme','federal-appellate','federal-specialty','other'} else 'memorandum-opinion'
    if re.search(r'\bORDER\b', head):
        return 'order'
    if re.search(r'ORDER|SHOW CAUSE', head): return 'order'
    return 'order'

def actor_from_party(p):
    p=(p or '').lower()
    if 'expert' in p: return 'expert'
    if 'judge' in p: return 'judge' if 'lawyer' not in p else 'lawyer'
    if 'lawyer' in p or 'counsel' in p or 'attorney' in p: return 'lawyer'
    if 'pro se' in p or 'litigant' in p: return 'litigant-in-person'
    return 'other'

def money(s):
    if not s or not str(s).strip(): return (None,None)
    st=str(s).strip()
    cur='USD' if 'USD' in st.upper() or '$' in st else None
    m=re.search(r'\d[\d,]*(?:\.\d+)?', st)
    if not m: return (None,cur)
    val=float(m.group(0).replace(',',''))
    if val.is_integer(): val=int(val)
    if not cur and val in (1,):
        # The source spreadsheet sometimes uses a bare 1 as a yes flag rather than an amount.
        return (None,None)
    return (val, cur)

def outcome_enum(lead, passage, penalty):
    out=(lead.get('Outcome') or '').lower()
    p=passage.lower()
    if penalty is not None:
        if 'cost' in out or 'fee' in out: return 'costs-order'
        return 'fine'
    for k,v in OUTCOME_KEYWORDS.items():
        if k in out: return v
    if 'order to show cause' in p or 'show cause' in p: return 'pending'
    if 'sanction' in p and ('declines' not in p and 'declined' not in p): return 'sanctions'
    if 'warn' in p or 'caution' in p or 'admonish' in p: return 'warning'
    if 'dismiss' in p: return 'dismissal'
    return 'other'

def tool_name(lead, passage):
    t=(lead.get('AI Tool') or '').strip()
    if t and t.lower() not in {'implied','unidentified','unknown','n/a'}:
        return t
    return None

def conduct_from_lead(lead):
    h=lead.get('Hallucination Items') or ''
    h=re.sub(r'\s*\|\|\s*', '; ', h)
    h=re.sub(r'\b(Fabricated|False Quotes|Misrepresented|Misstated|Fake|Invalid):\s*[^|;]{0,60}\s*(?:\||;)\s*', '', h)
    h=re.sub(r'^(Fabricated|False Quotes|Misrepresented|Misstated|Fake|Invalid):\s*[^.;]{0,80}$', '', h)
    h=clean_text(h)
    if not h:
        h='The filing contained fabricated, nonexistent, or inaccurate legal citations addressed by the court.'
    return textwrap.shorten(h, width=295, placeholder='...')

def authorities(lead, passage):
    vals=[]
    def add(x):
        x=clean_text(x).strip(' .;:,')
        if len(x)<4 or len(x)>180: return
        low=x.lower()
        if low in {'fabricated','case law','legal norm','exhibits & submissions'}: return
        bad_prefix=('plaintiff ', 'appellant ', 'appellee ', 'petitioner ', 'respondent ', 'defendant ', 'defendants ', 'court ', 'title ')
        if low.startswith(bad_prefix):
            return
        if x not in vals: vals.append(x)
    h=lead.get('Hallucination Items') or ''
    for m in re.finditer(r'[“"\']([^“”"\']{4,160})[”"\']', h):
        add(m.group(1))
    # case citations from passage/lead text
    src=h+' '+passage
    for pat in [
        r'\b[A-Z][A-Za-z0-9.&’\'\- ]+ v\. [A-Z][A-Za-z0-9.&’\'\- ]+(?:,\s*(?:No\.|\d)[^.;()]{0,80}(?:\)|\d{4}))?',
        r'\bFed\. R\. [A-Za-z. ]+\s*\d+(?:\([a-z0-9]+\))*',
        r'\bRule\s+11(?:\([a-z0-9]+\))*',
        r'\b[A-Z][A-Za-z. ]+R\.\s*\d+(?:\.\d+)?(?:\([a-z0-9]+\))*',
        r'\b\d+\s+C\.F\.R\.\s*§\s*[\d.]+(?:\([a-z0-9]+\))*',
    ]:
        for m in re.finditer(pat, src):
            add(m.group(0))
            if len(vals)>=12: break
        if len(vals)>=12: break
    return vals[:12]

def topics(lead, passage):
    return ['fabricated-citations']

def summary_text(lead, court, passage, outcome):
    actor=actor_from_party(lead.get('Party(ies)'))
    actor_phrase={'lawyer':'counsel','litigant-in-person':'a self-represented litigant','expert':'an expert','judge':'a judge','other':'a participant'}[actor]
    out=(lead.get('Outcome') or outcome.replace('-',' ')).strip() or outcome.replace('-',' ')
    s=(f"On {lead.get('Date')}, {court} addresses fabricated-citation issues in {lead.get('Case Name')}. "
       f"The decision describes nonexistent, misquoted, or unsupported authorities in a filing by {actor_phrase} "
       f"and records the outcome as {out}. It treats the defects as a litigation conduct issue affecting the filing or motion.")
    return s[:515]

def disposition_text(lead, outcome):
    out=(lead.get('Outcome') or '').strip()
    if out:
        return textwrap.shorten(f"The court addressed fabricated-citation concerns and recorded the outcome as {out}.", width=235, placeholder='...')
    return "The court resolved the underlying matter and addressed fabricated-citation concerns without a separately coded sanction outcome."

def tracker_for(case):
    s=ascii_slug(case)
    candidates={s, short_slug(case)}
    # common manual exact in this slice
    if 'cartagena' in s and 'dixon' in s: candidates.add('cartagena-v-dixon-blackburn')
    for c in candidates:
        if c in TRACKER: return c
    return None

rows=[]; skips=[]; seen=set()
for idx, lead in enumerate(LEADS,1):
    src=(lead.get('Source') or '').strip()
    is_char=src.startswith('/documents/') or 'damiencharlotin.com/documents/' in src
    if not is_char:
        # CourtListener attempted separately; skipped if no usable primary document found.
        reason='CourtListener search was throttled or returned no matching document with a fetchable court/public-domain PDF.'
        # refine based on saved search
        sf=Path(f'work/agents/t1-s6-courtlistener/{idx:03d}-search.json')
        if sf.exists():
            try:
                data=json.load(open(sf))
                if data.get('detail'): reason='CourtListener search throttled before a usable document could be retrieved.'
                elif data.get('count')==0: reason='CourtListener search returned no results.'
                elif data.get('results'): reason='CourtListener search returned no matching fetchable court document.'
            except Exception:
                pass
        skips.append({'idx':idx,'case':lead.get('Case Name'),'reason':reason})
        continue
    rec=manifest.get(idx,{})
    if rec.get('status')!='ok' or idx not in texts:
        skips.append({'idx':idx,'case':lead.get('Case Name'),'reason':f"mirror fetch/extract failed: {rec.get('status')}"})
        continue
    txt=texts[idx].read_text(encoding='utf-8',errors='ignore')
    passage=extract_passage(txt)
    if idx in {52, 78}:
        skips.append({'idx':idx,'case':lead.get('Case Name'),'reason':'document mentions citation problems only in passing and does not substantively discuss AI or fabricated-citation sanctions'})
        continue
    if not KW.search(passage) and not KW.search(txt):
        skips.append({'idx':idx,'case':lead.get('Case Name'),'reason':'document did not substantively discuss AI or fabricated citations'})
        continue
    court,court_code,level,state=COURTS.get(lead.get('Court'),(lead.get('Court'),None,'other',None))
    prefix=court_prefix(court_code,court)
    did=f"{prefix}-2026-{short_slug(lead.get('Case Name','decision'))}"
    did=re.sub(r'[^a-z0-9-]','-',did.lower())
    did=re.sub(r'-+','-',did).strip('-')[:90]
    base=did; n=2
    while did in seen:
        did=f"{base[:86]}-{n}"; n+=1
    seen.add(did)
    penalty,currency=money(lead.get('Monetary Penalty'))
    outcome=outcome_enum(lead,passage,penalty)
    ai_tool=tool_name(lead,passage)
    url=src if src.startswith('http') else HOST+src
    row={
        'decision_id': did,
        'case_name': lead.get('Case Name'),
        'court': court,
        'court_code': court_code,
        'court_level': level,
        'state': state,
        'date_filed': lead.get('Date'),
        'citation': extract_citation(txt),
        'docket_number': extract_docket(lead,txt),
        'document_type': document_type(txt, level),
        'topics': topics(lead,passage),
        'primary_topic': 'fabricated-citations',
        'court_used_ai': False,
        'ai_tool_named': ai_tool,
        'disposition': disposition_text(lead,outcome),
        'ai_passage': passage,
        'cited_authorities': authorities(lead,passage),
        'summary': summary_text(lead,court,passage,outcome),
        'incident': {
            'conduct': conduct_from_lead(lead),
            'outcome': outcome,
            'actor': actor_from_party(lead.get('Party(ies)')),
            'monetary_penalty': penalty,
            'currency': currency,
            'ai_tool': ai_tool,
        },
        'tracker_slug': tracker_for(lead.get('Case Name','')),
        'courtlistener_url': None,
        'text_sha256': rec.get('sha256'),
        'source_url': url,
        'archive_url': None,
        'fetched_at': FETCHED_AT,
        'verification': 'mirror-read',
        'lead_source': ['charlotin-cc0'],
        'notes': 'official copy pending',
    }
    rows.append(row)

out=Path('work/agents/decisions-t1-s6.jsonl')
out.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in rows),encoding='utf-8')
Path('work/agents/decisions-t1-s6-skips.json').write_text(json.dumps(skips,indent=2,ensure_ascii=False),encoding='utf-8')
print(f'wrote {len(rows)} rows; skipped {len(skips)}')
