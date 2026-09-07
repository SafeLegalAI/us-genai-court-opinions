import json, urllib.request, urllib.parse, time, hashlib
from pathlib import Path
UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
files=['work/agents/decisions-topics-b.jsonl','work/agents/litigation-a.jsonl']
rows=[]
for file in files:
    for line in open(file):
        r=json.loads(line); r['_file']=file; rows.append(r)
urls=[]
for r in rows:
    u=r.get('source_url')
    if u and u not in urls: urls.append(u)
res={}
Path('work/research').mkdir(exist_ok=True)
for n,u in enumerate(urls,1):
    print(f'[{n}/{len(urls)}] {u}', flush=True)
    rec={'source_url':u,'attempted':True,'save_status':None,'archive_url':None,'error':None}
    save='https://web.archive.org/save/'+u
    try:
        req=urllib.request.Request(save, headers={'User-Agent':UA})
        opener=urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
        with opener.open(req, timeout=25) as resp:
            rec['save_status']=getattr(resp,'status',None)
            final=resp.geturl()
            loc=resp.headers.get('Content-Location') or resp.headers.get('Location')
            if final and '/web/' in final:
                rec['archive_url']=final
            elif loc:
                rec['archive_url']=urllib.parse.urljoin('https://web.archive.org/',loc)
    except Exception as e:
        rec['error']=type(e).__name__+': '+str(e)[:220]
    # Whether save worked or not, look for the latest available successful memento.
    if not rec['archive_url']:
        try:
            cdx='https://web.archive.org/cdx?'+urllib.parse.urlencode({'url':u,'output':'json','fl':'timestamp,statuscode,original','filter':'statuscode:200','limit':'1','collapse':'digest'})
            req=urllib.request.Request(cdx, headers={'User-Agent':UA})
            with urllib.request.urlopen(req, timeout=20) as resp:
                data=json.loads(resp.read().decode('utf-8'))
            if len(data)>1:
                ts=data[1][0]
                rec['archive_url']='https://web.archive.org/web/'+ts+'/'+u
        except Exception as e:
            rec['cdx_error']=type(e).__name__+': '+str(e)[:220]
    res[u]=rec
    time.sleep(2)
Path('work/research/wayback_results.json').write_text(json.dumps(res,indent=2,ensure_ascii=False))
# update rows
for file in files:
    out=[]
    for line in open(file):
        r=json.loads(line)
        if not r.get('archive_url'):
            r['archive_url']=res.get(r.get('source_url'),{}).get('archive_url')
        out.append(r)
    with open(file,'w') as f:
        for r in out:
            f.write(json.dumps(r,ensure_ascii=False)+'\n')
print('done', sum(1 for v in res.values() if v.get('archive_url')), 'archives')
