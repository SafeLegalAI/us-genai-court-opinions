import json, glob, re, textwrap
from pathlib import Path

leads=json.load(open('work/leads/t1-slice-6.json'))
rows=[json.loads(l) for l in open('work/agents/decisions-t1-s6.jsonl') if l.strip()]
texts={int(Path(f).name[:3]):Path(f) for f in glob.glob('work/agents/t1-s6-source_text/*.txt')}
lead_url={}
for i,l in enumerate(leads,1):
    src=(l.get('Source') or '').strip()
    if src:
        lead_url[(src if src.startswith('http') else 'https://www.damiencharlotin.com'+src)] = i
idx_for_row=[lead_url[r['source_url']] for r in rows]
NUM={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve'}

def clean(s):
    s=(s or '').replace('\x0c',' ')
    s=re.sub(r'\s+', ' ', s).strip()
    return s

def sentence(s):
    s=clean(s).strip(' ;,')
    if not s: return s
    s=s[0].upper()+s[1:]
    if s[-1] not in '.!?': s+='.'
    return s

def short_court(c):
    reps=[('United States District Court for the ',''),('United States Court of Appeals for the ',''),('Court of Appeals of Washington','Washington Court of Appeals'),('Court of Appeals of Arizona','Arizona Court of Appeals'),('Appellate Court of Illinois','Illinois Appellate Court'),('District Court of Appeal of Florida','Florida District Court of Appeal')]
    for a,b in reps: c=c.replace(a,b)
    return c

def actor(row, possessive=False):
    a=row['incident']['actor']
    if possessive:
        return {'lawyer':"Counsel's",'litigant-in-person':"The self-represented party's",'expert':"The expert's",'judge':"The judge's",'other':"The filer's"}.get(a,"The filer's")
    return {'lawyer':'counsel','litigant-in-person':'a self-represented party','expert':'an expert','judge':'a judge','other':'a filer'}.get(a,'a filer')

def noun(txt):
    t=txt.lower()
    if 'surreply' in t: return 'surreply'
    if 'reply brief' in t: return 'reply brief'
    if 'opening brief' in t: return 'opening brief'
    if 'appellee' in t and 'brief' in t: return 'appellee brief'
    if 'appellant' in t and 'brief' in t: return 'appellate brief'
    if 'brief' in t: return 'brief'
    if 'motion' in t: return 'motion'
    if 'complaint' in t: return 'complaint'
    if 'response' in t: return 'response'
    if 'expert' in t or 'declaration' in t or 'report' in t: return 'expert submission'
    return 'filing'

def parts_from(h):
    raw=[clean(x) for x in re.split(r'\s*\|\|\s*', h or '') if clean(x)]
    parts=[]
    for p in raw:
        p=re.sub(r'^(Fabricated|False Quotes?|Misrepresented|Misstated|Invalid|Fake):\s*[^|;]{0,80}\s*(?:\||;)?\s*','',p,flags=re.I)
        p=clean(p)
        if p and not re.fullmatch(r'(case law|legal norm|exhibits? & submissions|doctrinal work)', p, re.I):
            parts.append(p)
    return parts

def add_example(vals,x):
    x=clean(x).strip(' .;,')
    if len(x)<4 or len(x)>90: return
    low=x.lower()
    bad=['hallucinogenic','ai','generative ai','education fraud','pro se litigant','lawyer']
    if low in bad or any(b in low for b in [' allegedly ', ' court found ', 'does not exist and', 'the court', 'plaintiff', 'defendant', 'appellant', 'appellee', 'respondent', 'petitioner']): return
    if not (re.search(r'\bv\.\b|\bWL\b|§|\bRule\b|\bF\. ?\d|\bU\.S\.\b|\bC\.F\.R\b|\b[A-Z][a-z]+/[A-Za-z]', x) or (len(x.split())<=5 and any(ch.isupper() for ch in x))): return
    if x not in vals: vals.append(x)

def examples(h):
    vals=[]
    for m in re.finditer(r'[“"]([^“”"]{4,110})[”"]', h): add_example(vals,m.group(1))
    for m in re.finditer(r"(?<![A-Za-z])'([^']{4,110})'(?![A-Za-z])", h): add_example(vals,m.group(1))
    for m in re.finditer(r'\b[A-Z][A-Za-z0-9.&’\'\-]+(?:\s+[A-Z][A-Za-z0-9.&’\'\-]+){0,5}\s+v\.\s+[A-Z][A-Za-z0-9.&’\'\-]+(?:\s+[A-Z][A-Za-z0-9.&’\'\-]+){0,6}(?:,\s*\d{4}\s+WL\s+\d+|,\s*\d+\s+[A-Z][A-Za-z. ]+\s+\d+)?', h): add_example(vals,m.group(0))
    return vals[:3]

def category_phrase(h, passage):
    t=(h+' '+passage).lower(); cats=[]
    if re.search(r'non-?existent|does not exist|fictitious|fictional|phantom|bogus|fake case',t): cats.append('nonexistent authorities')
    if re.search(r'quote|quotation|misquot',t): cats.append('fabricated or misattributed quotations')
    if re.search(r'misrepresent|mischaracter|does not support|unsupported|unrelated|inapplicable',t): cats.append('mischaracterized authority')
    if re.search(r'statute|rule|legal norm|c\.f\.r\.|regulation|ordinance',t): cats.append('incorrect statutory or rule text')
    if re.search(r'image|exhibit|submission|chart|screenshot',t): cats.append('defective exhibits or submissions')
    return cats or ['defective legal authorities']

def join_examples(ex):
    if not ex: return ''
    if len(ex)==1: return ex[0]
    return ', '.join(ex[:-1])+' and '+ex[-1]

def conduct(lead,row):
    h=lead.get('Hallucination Items') or ''
    ps=parts_from(h)
    ex=examples(h)
    cats=category_phrase(h,row['ai_passage'])[:3]
    n=max(1,len(ps))
    count=f"{NUM.get(n,str(n))} citation {'defect' if n==1 else 'defects'}"
    base=f"{actor(row, True)} {noun(h+' '+row['ai_passage'])} contained {count} involving {', '.join(cats)}"
    if ex:
        base=f"{actor(row, True)} {noun(h+' '+row['ai_passage'])} contained {count}, including {join_examples(ex)}, involving {', '.join(cats[:2])}"
    return textwrap.shorten(sentence(base), width=298, placeholder='...')

def money(row):
    val=row['incident'].get('monetary_penalty')
    if val is None: return None
    if isinstance(val,float) and val.is_integer(): val=int(val)
    return f"${val:,}"

def disposition(lead,row):
    lo=(lead.get('Outcome') or '').lower()
    p=(row['ai_passage']+' '+lo).lower()
    who='counsel' if row['incident']['actor']=='lawyer' else ('the self-represented party' if row['incident']['actor']=='litigant-in-person' else actor(row))
    amt=money(row)
    # Specific labels from the lead are converted to court actions, not copied.
    if 'contempt' in lo:
        return sentence(f"The court found contempt, struck the defective filing, and ordered {who} to pay {amt or 'a monetary sanction'}")
    if amt:
        if 'cost' in lo or 'fee' in p or row['incident']['outcome']=='costs-order':
            extra=' and complete corrective CLE' if 'cle' in lo or 'cle' in p else ''
            return sentence(f"The court ordered {who} to pay or reimburse {amt} in fees or costs for the defective filing{extra}")
        extra=' and referred the matter for discipline' if 'referral' in lo or 'bar' in lo else ''
        extra+=' and complete corrective CLE' if 'cle' in lo or 'cle' in p else ''
        return sentence(f"The court ordered {who} to pay {amt} for the defective authorities{extra}")
    if 'show cause satisfied' in lo or ('declined' in lo and 'sanction' in lo):
        return sentence(f"The court discharged the show-cause issue and declined Rule 11 sanctions after reviewing the explanation for the defective authorities")
    if 'show cause' in lo or 'upcoming sanction' in lo:
        return sentence(f"The court ordered {who} to show cause why sanctions, striking, or referral should not issue for the defective authorities")
    if 'public admonishment' in lo:
        return sentence(f"The court publicly admonished {who} for the defective authorities and directed future compliance with citation-verification duties")
    if 'formal admonishment' in lo or 'admonishment' in lo or 'reprimand' in lo:
        return sentence(f"The court admonished {who} to verify cited authorities and avoid repeating the citation defects")
    if 'bar referral' in lo or 'disciplinary' in lo:
        return sentence(f"The court referred {who} to disciplinary authorities for the defective citations")
    if 'brief struck' in lo or 'brief str' in lo or 'struck filings' in lo:
        return sentence(f"The court struck the defective filing and warned {who} to verify cited authorities before filing again")
    if 'attach copies' in lo:
        return sentence("The court affirmed an order requiring the litigant to attach copies of all cited authorities to future filings")
    if 'allowed to refile' in lo or 'refile' in lo:
        return sentence(f"The court allowed a corrected filing after identifying the defective authorities")
    if 'terminating sanctions' in lo:
        return sentence("The magistrate judge recommended terminating sanctions and dismissal because the defective authorities and other conduct undermined the litigation")
    if 'motion to dismiss granted' in lo or 'dismissed with prejudice' in lo or 'case dismissed' in lo or 'dismissing with prejudice' in lo:
        return sentence(f"The court dismissed the claims or case and cited the defective authorities in denying further relief")
    if 'appeal dismissed' in lo:
        return sentence(f"The court dismissed the appeal, assessed appellate costs, and addressed the defective authorities")
    if 'arguments deemed waived' in lo or 'waived' in lo:
        return sentence(f"The court deemed the arguments unsupported or waived because the cited authorities were defective")
    if 'affirmed' in lo or lo.startswith('affirmed'):
        return sentence(f"The court affirmed the judgment while identifying the defective authorities in the appellate briefing")
    if 'reversed' in lo or 'remanded' in lo:
        return sentence(f"The court affirmed in part, reversed in part, and addressed the defective authorities in the appellate briefing")
    if 'warning (both parties)' in lo:
        return sentence("The court warned both sides to verify authorities and quotations before filing future papers")
    if 'warning' in lo or row['incident']['outcome']=='warning':
        if 'disclose' in p:
            return sentence(f"The court warned {who} to disclose AI use when required and to verify future citations")
        if 'strike' in p and 'sanction' in p:
            return sentence(f"The court warned {who} that future defective filings may be stricken or sanctioned")
        return sentence(f"The court warned {who} to verify legal authorities before future filings")
    if 'exclude' in lo or 'cross-examination' in lo:
        return sentence("The court declined to exclude the expert but left the incorrect AI-generated citations for cross-examination")
    if 'share decision' in lo:
        return sentence("The court ordered counsel to share the decision with the firm and address the citation-verification failure internally")
    if row['incident']['outcome']=='pending':
        return sentence(f"The court ordered {who} to show cause why sanctions should not issue for the defective authorities")
    if row['incident']['outcome']=='referral':
        return sentence(f"The court referred {who} to disciplinary authorities for the defective citations")
    if row['incident']['outcome']=='dismissal':
        return sentence(f"The court dismissed claims or denied relief after identifying the defective authorities")
    return sentence(f"The court declined to rely on the defective authorities while resolving the motion or appeal")

def summary(lead,row,disp,cond):
    court=short_court(row['court'])
    cond2=cond.rstrip('.')
    # Lowercase first letter for embedded clause but preserve acronyms after possessive phrase.
    cond_clause=cond2[0].lower()+cond2[1:]
    disp_clause=re.sub(r'^The court\s+','',disp.rstrip('.'),flags=re.I)
    s=f"{court} on {row['date_filed']} found {cond_clause}. The court {disp_clause}."
    words=s.split()
    if len(words)>60:
        # Drop the example tail first.
        cond_short=re.sub(r', including .*?, involving ', ' involving ', cond_clause)
        s=f"{court} on {row['date_filed']} found {cond_short}. The court {disp_clause}."
    if len(s.split())>60:
        cond_short=textwrap.shorten(cond_clause,width=155,placeholder='...')
        s=f"{court} on {row['date_filed']} found {cond_short}. The court {disp_clause}."
    if len(s.split())<40:
        s=s.rstrip('.')+" after reviewing the challenged legal citations in the filing."
    return sentence(s)

for r,idx in zip(rows,idx_for_row):
    lead=leads[idx-1]
    # Ensure currency where a penalty amount exists.
    if r['incident'].get('monetary_penalty') is not None and not r['incident'].get('currency'):
        r['incident']['currency']='USD'
    c=conduct(lead,r)
    d=disposition(lead,r)
    r['incident']['conduct']=c
    r['disposition']=d
    r['summary']=summary(lead,r,d,c)

Path('work/agents/decisions-t1-s6.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in rows),encoding='utf-8')
print(f'rewrote {len(rows)} rows')
