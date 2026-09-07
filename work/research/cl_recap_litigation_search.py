import json, time, urllib.parse, urllib.request
from pathlib import Path
UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
queries={
 'tr-ross':'"Thomson Reuters" "ROSS Intelligence" "20-cv-00613"',
 'tr-ross-appeal':'"25-2153" "ROSS Intelligence"',
 'west-legalease':'"West Publishing" "LegalEase" "18-cv-01445"',
 'faridian-donotpay':'"Faridian" "DoNotPay" "23-cv-01692"',
 'millerking-donotpay':'"MillerKing" "DoNotPay" "23-cv-00863"',
 'evenup-butler':'"EvenUp" "Butler Labs" "25-cv-08199"',
}
outdir=Path('work/research/cl-litigation'); outdir.mkdir(parents=True, exist_ok=True)
base='https://www.courtlistener.com/api/rest/v4/search/'
for i,(name,q) in enumerate(queries.items(),1):
    params={'q':q,'type':'r','order_by':'dateFiled desc'}
    url=base+'?'+urllib.parse.urlencode(params)
    print('QUERY',name,url, flush=True)
    req=urllib.request.Request(url, headers={'User-Agent':UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp: data=resp.read()
        (outdir/f'{name}.json').write_bytes(data); j=json.loads(data)
        print('count',j.get('count'),'detail',j.get('detail'), flush=True)
        for r in j.get('results',[])[:5]:
            print(r.get('dateFiled'), r.get('court_id'), r.get('caseName'), r.get('docketNumber'), r.get('docket_id'), r.get('absolute_url'), flush=True)
            print((' '.join((r.get('snippet') or '').split()))[:500], flush=True)
    except Exception as e: print('ERR',name,e, flush=True)
    if i != len(queries): time.sleep(15)
