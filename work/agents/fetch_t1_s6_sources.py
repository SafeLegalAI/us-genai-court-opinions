import json, os, re, subprocess, time, hashlib, datetime
from pathlib import Path
ROOT=Path('.')
leads=json.load(open('work/leads/t1-slice-6.json'))
out_dir=Path('work/agents/t1-s6-source_docs'); out_dir.mkdir(parents=True, exist_ok=True)
text_dir=Path('work/agents/t1-s6-source_text'); text_dir.mkdir(parents=True, exist_ok=True)
manifest=[]
UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
last_char=0.0
for idx, lead in enumerate(leads,1):
    src=(lead.get('Source') or '').strip()
    if not (src.startswith('/documents/') or src.startswith('https://www.damiencharlotin.com/documents/') or src.startswith('http://www.damiencharlotin.com/documents/')):
        manifest.append({'idx':idx,'case':lead.get('Case Name'),'source':src,'status':'not-charlotin'})
        continue
    url=src if src.startswith('http') else 'https://www.damiencharlotin.com'+src
    name=f"{idx:03d}-" + re.sub(r'[^A-Za-z0-9._-]+','_', Path(src).name)[:180]
    if not name.lower().endswith('.pdf'):
        name += '.pdf'
    pdf=out_dir/name
    txt=text_dir/(pdf.stem+'.txt')
    now=time.monotonic()
    wait=max(0,3.05-(now-last_char))
    if wait: time.sleep(wait)
    last_char=time.monotonic()
    rec={'idx':idx,'case':lead.get('Case Name'),'source':src,'url':url,'pdf':str(pdf),'txt':str(txt)}
    if not pdf.exists() or pdf.stat().st_size < 1000:
        try:
            cp=subprocess.run(['curl','-sL','--max-time','60','-A',UA,'-w','%{http_code} %{size_download} %{url_effective}','-o',str(pdf),url],capture_output=True,text=True,timeout=75)
            rec['curl_returncode']=cp.returncode; rec['curl_out']=cp.stdout.strip(); rec['curl_err']=cp.stderr.strip()
        except Exception as e:
            rec['status']='curl-exception'; rec['error']=repr(e); manifest.append(rec); print(idx,'curl exception',e,flush=True); continue
    else:
        rec['curl_returncode']=0; rec['curl_out']='cached'; rec['curl_err']=''
    if not pdf.exists():
        rec['status']='missing-pdf'; manifest.append(rec); print(idx,'missing pdf',flush=True); continue
    rec['bytes']=pdf.stat().st_size
    if rec['bytes'] > 25*1024*1024:
        rec['status']='too-large'; manifest.append(rec); print(idx,'too large',rec['bytes'],flush=True); continue
    try:
        sha=hashlib.sha256(pdf.read_bytes()).hexdigest(); rec['sha256']=sha
    except Exception as e:
        rec['sha256_error']=repr(e)
    if not txt.exists() or txt.stat().st_size == 0:
        cp=subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],capture_output=True,text=True,timeout=90)
        rec['pdftotext_returncode']=cp.returncode; rec['pdftotext_err']=cp.stderr.strip()
    else:
        rec['pdftotext_returncode']=0; rec['pdftotext_err']='cached'
    rec['txt_bytes']=txt.stat().st_size if txt.exists() else 0
    rec['status']='ok' if rec.get('pdftotext_returncode')==0 and rec['txt_bytes']>0 else 'extract-failed'
    manifest.append(rec)
    print(f"{idx:03d} {rec['status']} {rec.get('bytes',0)} {lead.get('Case Name')[:70]}", flush=True)
Path('work/agents/t1-s6-fetch-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print('done',len(manifest))
