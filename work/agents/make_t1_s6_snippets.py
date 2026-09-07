import json, glob, os, re, textwrap
leads=json.load(open('work/leads/t1-slice-6.json'))
texts={int(os.path.basename(f)[:3]):f for f in glob.glob('work/agents/t1-s6-source_text/*.txt')}
kw=re.compile(r'(generative|artificial intelligence|\bAI\b|ChatGPT|hallucinat|non-existent|nonexistent|fictitious|fabricat|fake|bogus|phantom|invented|made up|made-up|invalid citation)',re.I)
lines=[]
for idx,l in enumerate(leads,1):
    lines.append(f"\n===== {idx:03d} {l.get('Date')} {l.get('Court')} | {l.get('Case Name')} =====")
    lines.append(f"Outcome: {l.get('Outcome')} | Party: {l.get('Party(ies)')} | Tool: {l.get('AI Tool')} | Penalty: {l.get('Monetary Penalty')}")
    lines.append(f"Hallucination: {l.get('Hallucination Items','')[:800]}")
    f=texts.get(idx)
    if not f:
        lines.append('NO TEXT')
        continue
    txt=open(f,encoding='utf-8',errors='ignore').read()
    all_lines=txt.splitlines()
    hits=[]
    for i,line in enumerate(all_lines):
        if kw.search(line): hits.append(i)
    lines.append(f"Text file: {os.path.basename(f)} hits={len(hits)}")
    if hits:
        chosen=[]
        for h in hits[:4]:
            if chosen and h-chosen[-1] < 8: continue
            chosen.append(h)
            if len(chosen)>=2: break
        for h in chosen:
            start=max(0,h-6); end=min(len(all_lines),h+12)
            snippet='\n'.join(f"{j+1}: {all_lines[j]}" for j in range(start,end))
            lines.append('--- snippet ---\n'+snippet)
    # conclusion-ish tail lines with sanctions/warn/ordered
    tail='\n'.join(all_lines[-80:])
    tail_hits=[]
    for m in re.finditer(r'.{0,120}(sanction|warn|caution|ordered|ORDERED|dismiss|affirm|grant|deny|strike|refer).{0,160}', tail, re.I|re.S):
        s=' '.join(m.group(0).split())
        if s not in tail_hits: tail_hits.append(s)
        if len(tail_hits)>=3: break
    if tail_hits:
        lines.append('--- tail cues ---')
        lines += tail_hits
open('work/agents/t1-s6-audit-snippets.txt','w',encoding='utf-8').write('\n'.join(lines))
