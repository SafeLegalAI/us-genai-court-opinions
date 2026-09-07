import json, glob, os, re
from pathlib import Path
leads=json.load(open('work/leads/t1-slice-6.json'))
rows=[json.loads(l) for l in open('work/agents/decisions-t1-s6.jsonl') if l.strip()]
# map source basename to text
texts={int(Path(f).name[:3]):Path(f) for f in glob.glob('work/agents/t1-s6-source_text/*.txt')}
row_by_idx={}
for r in rows:
    # source_url contains documents path; find lead by source url suffix
    for i,l in enumerate(leads,1):
        src=(l.get('Source') or '').strip()
        url=src if src.startswith('http') else 'https://www.damiencharlotin.com'+src if src else ''
        if url==r['source_url']:
            row_by_idx[i]=r; break

kw_action=re.compile(r'\b(order(?:ed|s)?|grant(?:ed|s)?|deny(?:ing|ied|ies)?|dismiss(?:ed|es|ing)?|affirm(?:ed|s)?|reverse(?:d|s)?|remand(?:ed|s)?|strike|struck|sanction(?:ed|s)?|refer(?:red|s)?|admonish(?:ed|es)?|warn(?:ed|s)?|caution(?:ed|s)?|show cause|pay|fine|costs|fees|bar|contempt|recommend(?:ed|s)?)\b', re.I)

def clean(s): return re.sub(r'\s+',' ',s.replace('\x0c',' ')).strip()

def tail_cues(txt):
    lines=[clean(x) for x in txt.splitlines()]
    cues=[]
    # conclusion headings onwards
    for i,l in enumerate(lines):
        if re.search(r'\b(CONCLUSION|ORDER|RECOMMENDATION|DISPOSITION|Accordingly|For the foregoing|For these reasons)\b', l, re.I):
            block=' '.join(x for x in lines[i:i+30] if x)
            if len(block)>50 and kw_action.search(block): cues.append(block[:1200])
    # last 100 lines action sentences
    tail=' '.join(x for x in lines[-120:] if x)
    for m in re.finditer(r'[^.?!]{0,120}\b(?:GRANTED|DENIED|DISMISSED|AFFIRMED|REVERSED|REMANDED|ORDERED|SANCTION|WARN|CAUTION|ADMONISH|STRIKE|STRUCK|REFER|PAY|FINE|COST|FEE|SHOW CAUSE|recommend)[^.?!]{0,260}[.?!]', tail, re.I):
        s=clean(m.group(0))
        if s not in cues: cues.append(s)
    return cues[:5]

def print_range(a,b):
    for idx in range(a,b+1):
        r=row_by_idx.get(idx); l=leads[idx-1]
        if not r: continue
        print(f"\n===== LEAD {idx:03d} ROW {list(row_by_idx).index(idx)+1 if idx in row_by_idx else '?'} =====")
        print(f"CASE: {l['Case Name']}")
        print(f"COURT: {r['court']} | DATE {r['date_filed']} | ACTOR {r['incident']['actor']} | OUTCOME {l.get('Outcome')} | MONEY {l.get('Monetary Penalty')}")
        print(f"HALL: {clean(l.get('Hallucination Items',''))[:700]}")
        print(f"PASSAGE: {clean(r['ai_passage'])[:1100]}")
        tf=texts.get(idx)
        if tf:
            txt=tf.read_text(encoding='utf-8',errors='ignore')
            for c in tail_cues(txt): print('CUE:', c)

if __name__=='__main__':
    import sys
    a=int(sys.argv[1]); b=int(sys.argv[2])
    print_range(a,b)
