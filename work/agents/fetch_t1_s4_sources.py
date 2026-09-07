#!/usr/bin/env python3
import json, os, re, subprocess, time, hashlib, urllib.parse
from pathlib import Path

ROOT=Path('.')
LEADS=Path('work/leads/t1-slice-4.json')
DOC_DIR=Path('work/agents/t1_s4_docs')
TXT_DIR=Path('work/agents/t1_s4_text')
HTTP_DIR=Path('work/agents/t1_s4_http')
LOG=Path('work/agents/t1_s4_fetch_log.json')
UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
BASE='https://www.damiencharlotin.com'
DOC_DIR.mkdir(parents=True, exist_ok=True)
TXT_DIR.mkdir(parents=True, exist_ok=True)
HTTP_DIR.mkdir(parents=True, exist_ok=True)

leads=json.load(open(LEADS,encoding='utf-8'))
log=[]

def safe_name(i, src, ext='.pdf'):
    name=Path(urllib.parse.unquote(src)).name
    name=re.sub(r'[^A-Za-z0-9._%-]+','_',name)
    if len(name)>130:
        name=name[:120]+ext
    if not name.lower().endswith(ext):
        name += ext
    return f'{i:03d}-{name}'

def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check robots for the two non-CL hosts we fetch directly.
for host,url in [('charlotin','https://www.damiencharlotin.com/robots.txt'),('michigan','https://www.courts.michigan.gov/robots.txt')]:
    out=HTTP_DIR/f'{host}_robots.txt'
    if not out.exists():
        r=subprocess.run(['curl','-sL','--max-time','30','-A',UA,url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out.write_bytes(r.stdout)
        time.sleep(1)

last_charlotin=0.0
for i,lead in enumerate(leads,1):
    src=str(lead.get('Source',''))
    rec={'index':i,'case_name':lead.get('Case Name'), 'source':src, 'attempted':False}
    if src.startswith('/documents/'):
        url=BASE+src
        pdf=DOC_DIR/safe_name(i,src)
        txt=TXT_DIR/(pdf.stem+'.txt')
        rec.update({'kind':'charlotin-mirror','url':url,'pdf':str(pdf),'txt':str(txt)})
        if not pdf.exists() or pdf.stat().st_size==0:
            delay=max(0,3.05-(time.time()-last_charlotin))
            if delay:
                time.sleep(delay)
            last_charlotin=time.time()
            rec['attempted']=True
            r=subprocess.run(['curl','-sL','--fail','--max-time','60','--max-filesize','26214400','-A',UA,url,'-o',str(pdf)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            rec['curl_returncode']=r.returncode
            rec['curl_stderr']=r.stderr.decode('utf-8','replace') if isinstance(r.stderr,bytes) else r.stderr
        else:
            rec['attempted']=False
            rec['cached']=True
        if pdf.exists() and pdf.stat().st_size>0:
            rec['size']=pdf.stat().st_size
            rec['sha256']=hashlib.sha256(pdf.read_bytes()).hexdigest()
            if not txt.exists() or txt.stat().st_size==0:
                r=run(['pdftotext','-layout',str(pdf),str(txt)])
                rec['pdftotext_returncode']=r.returncode
                rec['pdftotext_stderr']=r.stderr[-1000:]
            if txt.exists():
                rec['text_size']=txt.stat().st_size
        log.append(rec)
    elif 'courts.michigan.gov' in src:
        out=HTTP_DIR/f'{i:03d}-michigan-case.html'
        rec.update({'kind':'official-page','url':src,'html':str(out),'attempted':not out.exists()})
        if not out.exists():
            r=subprocess.run(['curl','-sL','--fail','--max-time','60','-A',UA,src,'-o',str(out)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            rec['curl_returncode']=r.returncode
            rec['curl_stderr']=r.stderr.decode('utf-8','replace') if isinstance(r.stderr,bytes) else r.stderr
        if out.exists():
            rec['size']=out.stat().st_size
            rec['sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
        log.append(rec)
    else:
        rec.update({'kind':'needs-courtlistener-search'})
        log.append(rec)

LOG.write_text(json.dumps(log,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'leads':len(leads),'records':len(log),'charlotin':sum(1 for r in log if r.get('kind')=='charlotin-mirror'),'needs_cl':sum(1 for r in log if r.get('kind')=='needs-courtlistener-search')},indent=2))
