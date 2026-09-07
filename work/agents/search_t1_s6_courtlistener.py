import json, urllib.parse, subprocess, time
from pathlib import Path
UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
leads=json.load(open('work/leads/t1-slice-6.json'))
out=Path('work/agents/t1-s6-courtlistener'); out.mkdir(parents=True, exist_ok=True)
last=0.0
for idx, lead in enumerate(leads,1):
    src=(lead.get('Source') or '').strip()
    if src.startswith('/documents/') or 'damiencharlotin.com/documents/' in src:
        continue
    q='"{}"'.format(lead.get('Case Name','').replace('"',''))
    url='https://www.courtlistener.com/api/rest/v4/search/?'+urllib.parse.urlencode({'q':q,'type':'r','filed_after':'2026-01-01'})
    wait=max(0,12.1-(time.monotonic()-last))
    if wait: time.sleep(wait)
    last=time.monotonic()
    fn=out/f'{idx:03d}-search.json'
    print(f'{idx:03d} search {lead.get("Case Name")}', flush=True)
    cp=subprocess.run(['curl','-sL','--max-time','60','-A',UA,'-o',str(fn),'-w','%{http_code} %{size_download}',url],capture_output=True,text=True,timeout=75)
    meta={'idx':idx,'case':lead.get('Case Name'),'url':url,'curl_code':cp.returncode,'curl_out':cp.stdout.strip(),'curl_err':cp.stderr.strip()}
    (out/f'{idx:03d}-meta.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
print('done')
