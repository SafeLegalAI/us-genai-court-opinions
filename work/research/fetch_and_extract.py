import argparse, json, subprocess, time, hashlib, re
from pathlib import Path
from urllib.parse import urlparse
from html.parser import HTMLParser
UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
class TextHTML(HTMLParser):
    def __init__(self): super().__init__(); self.skip=0; self.parts=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower() in ('script','style','noscript'): self.skip+=1
        if tag.lower() in ('p','br','div','li','tr','h1','h2','h3','h4','td','th'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag.lower() in ('script','style','noscript') and self.skip: self.skip-=1
        if tag.lower() in ('p','div','li','tr','h1','h2','h3','h4'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def html_to_text(b):
    for enc in ('utf-8','windows-1252','latin1'):
        try:
            s=b.decode(enc); break
        except UnicodeDecodeError: pass
    else: s=b.decode('utf-8','ignore')
    p=TextHTML(); p.feed(s)
    text=''.join(p.parts)
    text=re.sub(r'\n[ \t]+','\n',text)
    text=re.sub(r'[ \t]+',' ',text)
    text=re.sub(r'\n{3,}','\n\n',text)
    return text.strip()+"\n"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('manifest'); args=ap.parse_args()
    items=json.load(open(args.manifest))
    meta=[]; last_seen={}
    crawl_delay={'www.iowacourts.gov':30,'www.ca10.uscourts.gov':10,'www.ded.uscourts.gov':10,'www.ftc.gov':5,'storage.courtlistener.com':5}
    for it in items:
        kind=it.get('kind','decisions'); id_=it['id']; url=it['fetch_url']
        srcdir=Path('work/sources')/kind; txtdir=Path('work/texts')/kind
        srcdir.mkdir(parents=True, exist_ok=True); txtdir.mkdir(parents=True, exist_ok=True)
        out=srcdir/(id_+'.bin'); txt=txtdir/(id_+'.txt')
        host=urlparse(url).netloc
        delay=crawl_delay.get(host,1)
        now=time.time(); wait=max(0, last_seen.get(host,0)+delay-now)
        if wait: time.sleep(wait)
        elif delay: time.sleep(min(1,delay))
        last_seen[host]=time.time()
        print('FETCH', id_, url)
        if not out.exists() or out.stat().st_size==0:
            res=subprocess.run(['curl','-sL','--max-time','60','-A',UA,url,'-o',str(out)], stderr=subprocess.PIPE)
            if res.returncode!=0:
                print(' curl failed',res.returncode,res.stderr.decode('utf-8','ignore')[:200])
        b=out.read_bytes() if out.exists() else b''
        sha=hashlib.sha256(b).hexdigest() if b else None
        if b.startswith(b'%PDF'):
            try:
                res=subprocess.run(['pdftotext','-layout',str(out),'-'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
                text=res.stdout.decode('utf-8','replace')
                if not text.strip(): text=res.stderr.decode('utf-8','replace')
            except Exception as e:
                text=f'[pdftotext failed: {e}]\n'
        else:
            text=html_to_text(b)
        txt.write_text(text)
        meta.append({**it,'saved':str(out),'text_path':str(txt),'text_sha256':sha,'bytes':len(b),'is_pdf':b.startswith(b'%PDF')})
        print(' -> bytes',len(b),'pdf',b.startswith(b'%PDF'),'sha',sha,'text',len(text))
    Path(args.manifest).with_suffix('.meta.json').write_text(json.dumps(meta,indent=2))
if __name__=='__main__': main()
