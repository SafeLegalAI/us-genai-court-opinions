import json, pathlib, re, subprocess, time, hashlib, html as htmlmod
from urllib.parse import urlparse, urlunparse, quote, unquote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib import robotparser
from bs4 import BeautifulSoup

UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
ROOT=pathlib.Path('.')
SRC=ROOT/'work'/'sources'; TXT=ROOT/'work'/'texts'; META=ROOT/'work'/'research'/'fetch_metadata.json'
SRC.mkdir(parents=True, exist_ok=True); TXT.mkdir(parents=True, exist_ok=True)

def safe_slug(s):
    s=re.sub(r'[^A-Za-z0-9]+','-',s).strip('-').lower()
    return s[:80] or 'doc'

def norm_url(url):
    p=urlparse(url)
    path=quote(unquote(p.path), safe='/%')
    query=quote(unquote(p.query), safe='=&?/:,%+-_.')
    return urlunparse((p.scheme,p.netloc,path,p.params,query,p.fragment))

# Build candidates from CourtListener discovery files.
candidates={}
for f in pathlib.Path('work/research/courtlistener').glob('*.json'):
    try: data=json.load(open(f))
    except Exception: continue
    for r in data.get('results',[]):
        ops=r.get('opinions') or []
        if not ops: continue
        o=ops[0]
        url=o.get('download_url')
        if not url: continue
        host=urlparse(url).netloc.lower()
        # Skip clearly non-primary hosts.
        if host in {'colorado.vlex.io','www.socialaw.com'}:
            continue
        key=url
        item=candidates.setdefault(key, {'url':url, 'queries':set(), 'case':r.get('caseName'), 'date':r.get('dateFiled'), 'court':r.get('court_id'), 'docket':r.get('docketNumber'), 'cluster_id':r.get('cluster_id')})
        item['queries'].add(f.stem)
# Known direct leads from task not always in CL results.
for url,case,date,court,docket,lead in [
 ('https://media.ca11.uscourts.gov/opinions/pub/files/202212581.pdf','Snell v. United Specialty Insurance Co.','2024-05-28','ca11','22-12581','user-lead'),
 ('https://www.dccourts.gov/sites/default/files/2025-02/Ross-v-United-States-23-CM-1067-S.pdf','Ross v. United States','2025-02-20','dc','23-CM-1067','user-lead'),
 ('https://nycourts.gov/reporter/3dseries/2026/2026_00825.htm','Matter of M.S.','2026-02-17','ny','No. 7','user-lead'),
 ('https://www2.ca3.uscourts.gov/opinarch/261313np.pdf','Bryan v. City of Philadelphia','2026-07-17','ca3','26-1313','user-lead'),
]:
    item=candidates.setdefault(url, {'url':url, 'queries':set(), 'case':case, 'date':date, 'court':court, 'docket':docket, 'cluster_id':None})
    item['queries'].add(lead)

robots_cache={}
host_last={}
host_blocked={}

def robots_ok(url):
    p=urlparse(url)
    host=p.netloc.lower()
    if host in host_blocked:
        return False, f'host-blocked:{host_blocked[host]}'
    if host not in robots_cache:
        rurl=f'{p.scheme}://{p.netloc}/robots.txt'
        rp=robotparser.RobotFileParser()
        try:
            req=Request(rurl,headers={'User-Agent':UA})
            with urlopen(req,timeout=20) as resp:
                content=resp.read(200000).decode('utf-8','ignore').splitlines()
                status=getattr(resp,'status',200)
            rp.parse(content)
            robots_cache[host]=rp
            print('robots',host,status,'lines',len(content))
        except HTTPError as e:
            # 404/5xx robots means no usable robots; 403/429 means do not fetch this host.
            print('robots-error',host,e.code)
            if e.code in (403,429):
                host_blocked[host]=f'robots-{e.code}'
                return False, f'robots-{e.code}'
            rp.parse([]); robots_cache[host]=rp
        except Exception as e:
            print('robots-error',host,type(e).__name__)
            rp.parse([]); robots_cache[host]=rp
    rp=robots_cache[host]
    ok=rp.can_fetch(UA,url)
    return ok, 'robots-disallow' if not ok else 'ok'

def fetch(url, slug):
    p=urlparse(url); host=p.netloc.lower()
    now=time.time(); delay=1.1-(now-host_last.get(host,0))
    if delay>0: time.sleep(delay)
    host_last[host]=time.time()
    nurl=norm_url(url)
    req=Request(nurl,headers={'User-Agent':UA,'Accept':'application/pdf,text/html,*/*'})
    with urlopen(req,timeout=60) as resp:
        data=resp.read(30_000_000)
        ct=resp.headers.get('content-type','')
        status=getattr(resp,'status',200)
        final=resp.geturl()
    ext='.pdf' if (b'%PDF' in data[:20] or 'pdf' in ct.lower() or nurl.lower().split('?')[0].endswith('.pdf')) else '.html'
    path=SRC/(slug+ext)
    path.write_bytes(data)
    return path, ct, status, final, hashlib.sha256(data).hexdigest(), len(data)

def extract(path, slug):
    out=TXT/(slug+'.txt')
    if path.suffix.lower()=='.pdf':
        cp=subprocess.run(['pdftotext','-layout',str(path),'-'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120)
        if cp.returncode!=0:
            out.write_text(cp.stderr.decode('utf-8','ignore'))
            return out, False, cp.stderr.decode('utf-8','ignore')[:200]
        out.write_bytes(cp.stdout)
        return out, True, ''
    data=path.read_text(errors='ignore')
    soup=BeautifulSoup(data,'html.parser')
    for tag in soup(['script','style','noscript']): tag.decompose()
    text=soup.get_text('\n')
    lines=[re.sub(r'\s+',' ',ln).strip() for ln in text.splitlines()]
    text='\n'.join([ln for ln in lines if ln])
    out.write_text(text)
    return out, True, ''

meta=[]
for idx,(url,item) in enumerate(candidates.items(),1):
    slug=safe_slug(f"{item.get('date','')}-{item.get('court','')}-{item.get('case','doc')}")
    item['queries']=sorted(item['queries'])
    item['slug']=slug
    print(f'[{idx}/{len(candidates)}] {slug} {url}')
    ok,reason=robots_ok(url)
    item['robots']=reason
    if not ok:
        item['fetched']=False; meta.append(item); continue
    try:
        path,ct,status,final,sha,nbytes=fetch(url,slug)
        item.update({'fetched':True,'raw_path':str(path),'content_type':ct,'status':status,'final_url':final,'text_sha256':sha,'bytes':nbytes})
        if nbytes>25_000_000:
            item['extract_ok']=False; item['extract_error']='over-25MB'
        else:
            tpath,ok2,err=extract(path,slug)
            item.update({'text_path':str(tpath),'extract_ok':ok2,'extract_error':err})
            if ok2:
                item['text_chars']=len(tpath.read_text(errors='ignore'))
        print('  fetched',status,ct,nbytes,'extract',item.get('extract_ok'))
    except HTTPError as e:
        item.update({'fetched':False,'fetch_error':f'HTTP {e.code}'})
        print('  fetch-error HTTP',e.code)
        if e.code in (403,429): host_blocked[urlparse(url).netloc.lower()]=f'fetch-{e.code}'
    except Exception as e:
        item.update({'fetched':False,'fetch_error':repr(e)[:300]})
        print('  fetch-error',repr(e)[:160])
    meta.append(item)
    META.write_text(json.dumps(meta,indent=2))
META.write_text(json.dumps(meta,indent=2))
print('done',len(meta),'fetched',sum(1 for m in meta if m.get('fetched')))
