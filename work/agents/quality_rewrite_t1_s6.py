import json, glob, re, os, textwrap
from pathlib import Path

leads=json.load(open('work/leads/t1-slice-6.json'))
rows=[json.loads(l) for l in open('work/agents/decisions-t1-s6.jsonl') if l.strip()]
texts={int(Path(f).name[:3]):Path(f) for f in glob.glob('work/agents/t1-s6-source_text/*.txt')}

# Match output row to lead index by source URL.
lead_url={}
for i,l in enumerate(leads,1):
    src=(l.get('Source') or '').strip()
    if src:
        lead_url[(src if src.startswith('http') else 'https://www.damiencharlotin.com'+src)] = i
row_idx={i:lead_url.get(r['source_url']) for i,r in enumerate(rows)}

NUM={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve'}

def clean(s):
    s=(s or '').replace('\x0c',' ')
    s=re.sub(r'Case \d:[^\n]{0,120}Page(?: ID)?[^\n]{0,80}', ' ', s)
    s=re.sub(r'Page \d+ of \d+', ' ', s)
    s=re.sub(r'PageID\s*#?:\s*\d+', ' ', s)
    s=re.sub(r'\s+', ' ', s).strip()
    return s

def sentencize(s):
    s=clean(s).strip(' ;,')
    if not s: return s
    s=s[0].upper()+s[1:]
    if s[-1] not in '.!?': s+='.'
    return s

def court_short(court):
    c=court.replace('United States District Court for the ','').replace('United States Court of Appeals for the ','')
    c=c.replace('District Court of Appeal of Florida','Florida District Court of Appeal')
    c=c.replace('Court of Appeals of Washington','Washington Court of Appeals')
    c=c.replace('Court of Appeals of Arizona','Arizona Court of Appeals')
    c=c.replace('Appellate Court of Illinois','Illinois Appellate Court')
    return c

def actor_phrase(actor, possessive=False):
    base={
        'lawyer':'counsel',
        'litigant-in-person':'a self-represented party',
        'expert':'an expert',
        'judge':'a judge',
        'firm':'a law firm',
        'prosecutor':'a prosecutor',
        'other':'a filer',
    }.get(actor,'a filer')
    if possessive:
        return "counsel's" if actor=='lawyer' else ("the self-represented party's" if actor=='litigant-in-person' else f"{base}'s")
    return base

def filing_noun(text):
    t=text.lower()
    if 'reply brief' in t: return 'reply brief'
    if 'opening brief' in t: return 'opening brief'
    if 'appellee' in t and 'brief' in t: return 'appellee brief'
    if 'appellant' in t and 'brief' in t: return 'appellate brief'
    if 'brief' in t: return 'brief'
    if 'motion' in t: return 'motion'
    if 'complaint' in t: return 'complaint'
    if 'response' in t: return 'response'
    if 'expert' in t: return 'expert submission'
    return 'filing'

def split_hall(h):
    return [clean(x) for x in re.split(r'\s*\|\|\s*', h or '') if clean(x)]

def strip_category(part):
    return clean(re.sub(r'^(Fabricated|False Quotes?|Misrepresented|Misstated|Invalid|Fake):\s*[^|;]{0,80}\s*(?:\||;)?\s*', '', part, flags=re.I))

def examples_from(text, maxn=3):
    vals=[]
    def add(x):
        x=clean(x).strip(' .;,')
        if len(x)<3 or len(x)>95: return
        low=x.lower()
        bad=('fabricated','case law','legal norm','exhibits','submissions','brief','court','plaintiff','defendant','appellant','appellee','respondent','petitioner')
        if low in bad or low.startswith(('court ','plaintiff ','defendant ','appellant ','appellee ','respondent ','petitioner ')): return
        # avoid long prose fragments without citation/case-like capitalization
        if len(x.split())>12: return
        if x not in vals: vals.append(x)
    for m in re.finditer(r'[“"\']([^“”"\']{3,120})[”"\']', text): add(m.group(1))
    # named v. authorities not in quotes
    for m in re.finditer(r'\b[A-Z][A-Za-z0-9.&’\'\-]+(?:\s+[A-Z][A-Za-z0-9.&’\'\-]+){0,5}\s+v\.\s+[A-Z][A-Za-z0-9.&’\'\-]+(?:\s+[A-Z][A-Za-z0-9.&’\'\-]+){0,6}(?:,\s*\d{4}\s+WL\s+\d+|,\s*\d+\s+[A-Z][A-Za-z. ]+\s+\d+)?', text):
        add(m.group(0))
    return vals[:maxn]

def conduct_sentence(lead, row):
    h=lead.get('Hallucination Items') or ''
    parts=[strip_category(p) for p in split_hall(h)]
    parts=[p for p in parts if p and not re.fullmatch(r'(Fabricated|False Quotes?|Misrepresented|Misstated):?\s*[^.;|]{0,80}', p, re.I)]
    source=' '.join(parts) or row['ai_passage']
    lower=(h+' '+row['ai_passage']).lower()
    cats=[]
    if re.search(r'non-?existent|does not exist|fictitious|fictional|phantom|fake case', lower): cats.append('nonexistent authorities')
    if re.search(r'quote|quotation|misquot', lower): cats.append('fabricated or misattributed quotations')
    if re.search(r'misrepresent|mischaracter|does not support|unrelated|inapplicable|unsupported', lower): cats.append('mischaracterized authority')
    if re.search(r'statute|rule|c\.f\.r\.|legal norm|regulation', lower): cats.append('incorrect statutory or rule text')
    if re.search(r'image|exhibit|submission|chart', lower): cats.append('defective exhibits or submissions')
    if not cats: cats.append('defective legal authorities')
    ex=examples_from(h,3)
    noun=filing_noun(h+' '+row['ai_passage'])
    who=actor_phrase(row['incident']['actor'], True).capitalize()
    count=len(parts)
    if count<=1 and ex:
        desc=f"{who} {noun} cited or quoted {ex[0]}, which the court found nonexistent, unsupported, or not saying what the filing asserted."
    elif ex:
        desc=f"{who} {noun} contained {NUM.get(count, str(count))} citation defects, including {', '.join(ex)}, involving {', '.join(cats[:2])}."
    else:
        desc=f"{who} {noun} contained {NUM.get(count, str(count))} citation defects involving {', '.join(cats[:3])}."
    return textwrap.shorten(sentencize(desc), width=298, placeholder='...')

def action_cues(txt):
    txt=txt.replace('\x0c',' ')
    lines=[clean(x) for x in txt.splitlines()]
    # remove publisher/editor lines
    lines=[x for x in lines if x and not re.search(r'© 2026 Thomson Reuters|No claim to original|Only the Westlaw citation|Editor\'s Note|All Citations|End of Document|Not Reported|Slip Copy', x, re.I)]
    candidates=[]
    zones=[]
    joined=' '.join(lines)
    # headings and tail
    for i,l in enumerate(lines):
        if re.search(r'\b(CONCLUSION|ORDER|RECOMMENDATION|DISPOSITION)\b', l, re.I):
            zones.append(' '.join(lines[i:i+35]))
    zones.append(' '.join(lines[-130:]))
    # also opening proceedings/title often states order accurately
    zones.append(' '.join(lines[:80]))
    pats=[
        r'(?:For (?:the )?(?:foregoing|above|these) reasons,?\s*)?(?:the Court|this Court|we|I|the undersigned)\s+(?:therefore\s+|accordingly\s+|will\s+)?(?:GRANTS?|DENIES?|DISMISSES?|AFFIRMS?|REVERSES?|REMANDS?|RECOMMENDS?|ORDERS?|STRIKES?|REFERS?|SANCTIONS?)[^.]{20,520}\.',
        r'IT IS (?:THEREFORE )?ORDERED[^.]{20,520}\.',
        r'(?:AFFIRMED|REVERSED|REMANDED|DISMISSED|VACATED)[^.]{0,260}\.',
        r'Proceedings:\s*[^.]{20,420}',
        r'Order\s+\([^)]{10,240}\)',
    ]
    for z in zones:
        for pat in pats:
            for m in re.finditer(pat, z, re.I):
                s=clean(m.group(0))
                if len(s)>35 and not re.search(r'citation references|invalid citations|attorneys and law firms', s, re.I):
                    candidates.append(s)
    # Prefer candidates with merits verbs, not just ancillary notice.
    def score(s):
        sc=0
        if re.search(r'grant|deny|dismiss|affirm|reverse|remand|recommend', s, re.I): sc+=6
        if re.search(r'sanction|strike|show cause|refer|admonish|warn|caution|fee|cost', s, re.I): sc+=4
        if len(s)<260: sc+=2
        if s.lower().startswith('proceedings'): sc-=3
        return sc
    candidates=sorted(dict.fromkeys(candidates), key=score, reverse=True)
    return candidates[:5]

def normalize_main_action(cue):
    if not cue: return ''
    s=clean(cue)
    s=re.sub(r'^(For (?:the )?(?:foregoing|above|these) reasons,?\s*)', '', s, flags=re.I)
    s=re.sub(r'^(IT IS (?:THEREFORE )?ORDERED that\s*)', '', s, flags=re.I)
    s=re.sub(r'^(Proceedings:\s*)', '', s, flags=re.I)
    s=re.sub(r'^(?:The Court|This Court|the undersigned)\s+', '', s, flags=re.I)
    s=re.sub(r'^(?:we|I)\s+', '', s, flags=re.I)
    s=s.strip(' .;')
    # lowercase leading all-caps verbs
    repl={'GRANTS':'granted','GRANT':'granted','DENIES':'denied','DENY':'denied','DISMISSES':'dismissed','DISMISS':'dismissed','AFFIRMS':'affirmed','AFFIRMED':'affirmed','REVERSES':'reversed','REVERSED':'reversed','REMANDS':'remanded','REMANDED':'remanded','RECOMMENDS':'recommended','ORDERED':'ordered','ORDERS':'ordered','STRIKES':'struck','STRUCK':'struck','REFERS':'referred','SANCTIONS':'sanctioned'}
    words=s.split()
    if words:
        key=words[0].strip(',').upper()
        if key in repl: words[0]=repl[key]
        s=' '.join(words)
    s=re.sub(r'\bwill grant\b','granted',s,flags=re.I)
    s=re.sub(r'\bwill deny\b','denied',s,flags=re.I)
    s=re.sub(r'\bwill dismiss\b','dismissed',s,flags=re.I)
    s=re.sub(r'\bwill affirm\b','affirmed',s,flags=re.I)
    s=re.sub(r'\s+', ' ', s)
    return s[:420].strip(' .')

def money_phrase(row):
    val=row['incident'].get('monetary_penalty')
    if val is None: return None
    if isinstance(val,float) and val.is_integer(): val=int(val)
    return f"${val:,}"

def ai_action(lead,row):
    out=row['incident']['outcome']
    actor=row['incident']['actor']
    who='counsel' if actor=='lawyer' else ('the self-represented party' if actor=='litigant-in-person' else actor_phrase(actor))
    p=(row['ai_passage']+' '+(lead.get('Outcome') or '')).lower()
    amt=money_phrase(row)
    if amt:
        if 'cost' in p or 'fee' in p or out=='costs-order':
            return f"ordered {who} to pay or reimburse {amt} in fees or costs tied to the defective filing"
        return f"ordered {who} to pay {amt} for the citation defects"
    if out=='pending':
        return f"ordered {who} to show cause why sanctions or other corrective action should not issue"
    if out=='referral':
        return f"referred {who} to disciplinary authorities"
    if out=='costs-order':
        return f"awarded or reserved fees and costs caused by the defective filing"
    if out=='fine':
        return f"imposed a monetary sanction for the citation defects"
    if out=='dismissal':
        return f"relied on the defective authorities in dismissing claims or denying further leave"
    if out=='sanctions':
        return f"imposed sanctions for the defective authorities"
    # lead-specific outcomes without monetary penalties
    lo=(lead.get('Outcome') or '').lower()
    if 'brief struck' in lo or 'struck' in lo:
        return f"struck or disregarded the defective filing"
    if 'waived' in lo:
        return f"deemed the unsupported arguments waived"
    if 'refile' in lo:
        return f"allowed a corrected filing after identifying the defective authorities"
    if 'exclude' in lo or 'cross-examination' in lo:
        return f"declined exclusion but left the citation defects for cross-examination"
    if 'share decision' in lo:
        return f"ordered counsel to circulate the decision within the firm"
    if 'reprimand' in lo or 'admon' in lo or 'warning' in lo or out=='warning':
        if 'strike' in p and 'sanction' in p:
            return f"warned that future defective filings may be stricken or sanctioned"
        return f"warned {who} to verify legal authorities before future filings"
    return f"declined further sanctions while identifying the citation defects"

def disposition(lead,row,txt):
    cues=action_cues(txt)
    main=normalize_main_action(cues[0] if cues else '')
    extra=ai_action(lead,row)
    # If the main action is only the AI action, avoid duplication.
    if not main or re.search(r'citation|AI|hallucinat|sanction|show cause|warn|admonish|refer|strike', main, re.I):
        s=f"The court {extra}."
        # For merits-free AI orders, append main if it has a concrete order.
        if main and not extra.lower() in main.lower():
            s=f"The court {main[0].lower()+main[1:]} and {extra}."
    else:
        s=f"The court {main[0].lower()+main[1:]} and {extra}."
    return textwrap.shorten(sentencize(s), width=238, placeholder='...')

def summary(lead,row,disp,conduct):
    c=court_short(row['court'])
    date=row['date_filed']
    actor=actor_phrase(row['incident']['actor'])
    # Make a concise conduct clause without repeated possessive.
    cond=conduct.rstrip('.')
    cond=re.sub(r"^(Counsel's|The self-represented party's|An expert's|A filer's)\s+", '', cond, flags=re.I)
    cond=cond[0].lower()+cond[1:] if cond else 'filing contained defective legal authorities'
    # exact order from disposition with leading The court removed
    order=re.sub(r'^The court\s+', '', disp.rstrip('.'), flags=re.I)
    s=f"{c} on {date} found that {actor} filed a {cond}. The court {order}."
    words=s.split()
    if len(words)>60:
        # shorten conduct first
        cond_short=textwrap.shorten(cond, width=150, placeholder='...')
        s=f"{c} on {date} found that {actor} filed a {cond_short}. The court {order}."
        words=s.split()
    if len(words)>60:
        order_short=textwrap.shorten(order, width=190, placeholder='...')
        s=f"{c} on {date} found that {actor} filed a {cond_short}. The court {order_short}."
    if len(s.split())<40:
        s=s.rstrip('.')+" after reviewing the challenged filing and the cited legal materials."
    return sentencize(s)

new=[]
for pos,row in enumerate(rows):
    idx=row_idx[pos]
    if not idx: raise SystemExit(f'no lead for row {pos+1} {row["decision_id"]}')
    lead=leads[idx-1]
    txt=texts[idx].read_text(encoding='utf-8',errors='ignore') if idx in texts else row['ai_passage']
    cond=conduct_sentence(lead,row)
    # set USD when any amount lacks currency
    if row['incident'].get('monetary_penalty') is not None and not row['incident'].get('currency'):
        row['incident']['currency']='USD'
    row['incident']['conduct']=cond
    disp=disposition(lead,row,txt)
    row['disposition']=disp
    row['summary']=summary(lead,row,disp,cond)
    new.append(row)

Path('work/agents/decisions-t1-s6.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in new),encoding='utf-8')
print(f'rewrote {len(new)} rows')
