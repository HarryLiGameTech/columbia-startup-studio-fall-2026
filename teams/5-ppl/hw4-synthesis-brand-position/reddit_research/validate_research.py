"""Validate the submitted ledger; optionally verify against the retained raw corpus."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--raw', type=Path, help='Directory containing manually saved JSON files')
args = parser.parse_args()
here = Path(__file__).resolve().parent
quotes = [json.loads(line) for line in (here / 'quotes.jsonl').read_text().splitlines()]
manifest = json.loads((here / 'corpus_manifest.json').read_text())
counts = Counter(item['kind'] for item in manifest)
assert counts == {'thread': 30, 'search': 10}, counts
thread_ids = [item['post_id'] for item in manifest if item['kind'] == 'thread']
assert len(set(thread_ids)) == 30
assert len(quotes) == len({q['quote_id'] for q in quotes}) == 18
by_theme = defaultdict(set)
for q in quotes:
    assert q['thread_id'] in thread_ids
    assert q['thread_id'] in q['permalink']
    if q['comment_id']:
        assert q['comment_id'] in q['permalink']
    assert q['is_verbatim'] and q['quote']
    by_theme[q['theme']].add(q['thread_id'])
recorded = json.loads((here / 'theme_counts.json').read_text())
for theme, ids in by_theme.items():
    assert recorded[theme] == {'distinct_threads': len(ids), 'thread_ids': sorted(ids)}
qmap = {q['quote_id']: q for q in quotes}
for filename, ids in {
    'brand_position.md': ['Q01', 'Q02', 'Q03', 'Q04', 'Q05'],
    'personas/maya.md': ['Q01', 'Q02'],
    'personas/jordan.md': ['Q03', 'Q04'],
    'personas/casey.md': ['Q05', 'Q06'],
}.items():
    text = (here.parent / filename).read_text()
    for qid in ids:
        assert qmap[qid]['quote'] in text, (filename, qid)
        assert qmap[qid]['permalink'] in text, (filename, qid)

if args.raw:
    bodies = {}
    def comments(listing):
        if isinstance(listing, dict):
            for c in listing.get('data', {}).get('children', []):
                if c.get('kind') == 't1':
                    yield c['data']
                    yield from comments(c['data'].get('replies'))
    actual_ids = set()
    comment_count = 0
    for item in manifest:
        data = (args.raw / item['filename']).read_bytes()
        assert len(data) == item['bytes']
        assert hashlib.sha256(data).hexdigest() == item['sha256'], item['filename']
        doc = json.loads(data)
        if item['kind'] == 'thread':
            post = doc[0]['data']['children'][0]['data']
            assert post['id'] == item['post_id']
            assert post['id'] not in actual_ids
            actual_ids.add(post['id'])
            bodies[(post['id'], None)] = post['selftext']
            cs = list(comments(doc[1]))
            usable = [c for c in cs if c.get('body') not in (None, '', '[removed]', '[deleted]')]
            assert usable
            comment_count += len(usable)
            for c in cs:
                bodies[(post['id'], c['id'])] = c.get('body', '')
    assert len(actual_ids) == 30 and comment_count == 617
    for q in quotes:
        assert q['quote'] in bodies[(q['thread_id'], q['comment_id'])], q['quote_id']
    print('PASS: 40 file hashes; 30 unique threads; 617 comment bodies; 18 exact quotes.')
else:
    print('PASS: manifest, ledger, theme counts, and brand/persona integration. Raw files not checked.')
