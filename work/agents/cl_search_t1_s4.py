#!/usr/bin/env python3
import json, time, urllib.parse, subprocess
from pathlib import Path
UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
leads=json.load(open('work/leads/t1-slice-4.json',encoding='utf-8'))
outdir=Path('work/agents/t1_s4_cl_search'); outdir.mkdir(parents=True,exist_ok=True)
indices=[i for i,l in enumerate(leads,1) if not str(l.get('Source','')).startswith('/documents/') and 'courts.michigan.gov' not in str(l.get('Source',''))]
for n,i in enumerate(indices):
    case=leads[i-1]['Case Name']
    q=f'"{case}"'
    url='https://www.courtlistener.com/api/rest/v4/search/?'+urllib.parse.urlencode({'q':q,'type':'r','filed_after':'2026-03-01'})
    out=outdir/f'{i:03d}-search.json'
    if not out.exists():
        if n: time.sleep(12.5)
        r=subprocess.run(['curl','-sL','--fail','--max-time','60','-A',UA,url,'-o',str(out)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(i,case,'rc',r.returncode,'stderr',r.stderr.decode('utf-8','replace')[:200] if isinstance(r.stderr,bytes) else r.stderr[:200])
    else:
        print(i,case,'cached')
