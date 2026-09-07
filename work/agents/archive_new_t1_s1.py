import json
import subprocess
import time
from pathlib import Path

archive_path = Path('work/agents/archive-results-t1-s1.json')
results = json.load(open(archive_path, encoding='utf-8')) if archive_path.exists() else {}
ids = {
    'pasuperct-2026-bisher-v-civic', 'txwd-2026-moore-v-aldridge-pite', 'cacd-2026-jabbari-v-omidvar',
    'ord-2026-united-states-v-karnezis', 'nysd-2026-santana-v-shook-hardy-bacon', 'mied-2026-al-ali-v-cvs-pharmacy',
    'txapp-2026-higgins-v-state', 'gao-2026-jaaw-group', 'vaeb-2026-in-re-mahar', 'txapp-2026-in-re-smt-sjt',
    'utd-2026-carey-v-breakell', 'nysd-2026-in-re-firestar-diamond', 'wiscapp-2026-first-community-credit-union-v-smith',
    'msnd-2026-harris-v-bank-of-america', 'illappct-2026-cole-v-lee', 'txapp-2026-in-re-qc-pc',
    'cod-2026-maloit-v-maloit', 'ca10-2026-robinson-v-oglala-sioux-tribe', 'tnctapp-2026-harding-place-v-robinson',
    'ohsd-2026-gragston-v-amazon', 'illappct-2026-scott-v-illinois-human-rights-commission', 'med-2026-mcneil-v-bisignano',
    'azd-2026-ruiz-v-magellan-financial-claude-osc', 'ord-2026-owen-v-askew', 'mdd-2026-campbell-v-tidalhealth',
    'txnd-2026-transcontinental-realty-v-moos', 'mied-2026-ponder-v-bcg-equities', 'mnctapp-2026-ally-bank-v-ngouambe',
    'wawd-2026-ledoux-v-outliers-sanctions', 'caed-2026-graves-v-pacific-gas-electric'
}
rows = []
for line in open('work/agents/decisions-t1-s1.jsonl', encoding='utf-8'):
    if line.strip():
        rows.append(json.loads(line))
urls = []
for r in rows:
    if r['decision_id'] in ids:
        u = r['source_url']
        if u not in urls:
            urls.append(u)
missing = [u for u in urls if u not in results]
print(f'urls={len(urls)} missing_attempts={len(missing)}')
for i, url in enumerate(missing, 1):
    save_url = 'https://web.archive.org/save/' + url
    try:
        proc = subprocess.run(
            ['curl', '-sS', '-m', '35', '-D', '-', '-o', '/dev/null', '-A', 'SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)', save_url],
            text=True, capture_output=True, check=False,
        )
        headers = proc.stdout
        status = ''
        for line in headers.splitlines():
            if line.startswith('HTTP/'):
                status = line.strip()
                break
        archive_url = None
        for line in headers.splitlines():
            if line.lower().startswith('location:'):
                loc = line.split(':', 1)[1].strip()
                if loc.startswith('/web/'):
                    archive_url = 'https://web.archive.org' + loc
                elif loc.startswith('https://web.archive.org/web/'):
                    archive_url = loc
                break
        results[url] = {'archive_url': archive_url, 'status': status, 'headers': headers, 'stderr': proc.stderr}
        print(f'{i}/{len(missing)} {status} archive={bool(archive_url)} {url}')
    except Exception as e:
        results[url] = {'archive_url': None, 'status': '', 'headers': '', 'stderr': repr(e)}
        print(f'{i}/{len(missing)} ERROR {url}: {e}')
    archive_path.write_text(json.dumps(results, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    if i != len(missing):
        time.sleep(5)

changed = 0
for r in rows:
    got = results.get(r.get('source_url'), {}).get('archive_url')
    if got and r.get('archive_url') != got:
        r['archive_url'] = got
        changed += 1
Path('work/agents/decisions-t1-s1.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n' for r in rows), encoding='utf-8')
print(f'updated_rows={changed}')
