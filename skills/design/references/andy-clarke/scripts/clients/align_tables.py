"""Align Markdown table pipes in a file in place. Usage: align_tables.py file.md"""
import sys

def align(block):
    rows = [[c.strip() for c in r.strip().strip('|').split('|')] for r in block]
    n = max(len(r) for r in rows)
    rows = [r + [''] * (n - len(r)) for r in rows]
    w = [max(len(r[i]) for r in rows if not set(r[i]) <= set('-:')) for i in range(n)]
    out = []
    for r in rows:
        if all(set(c) <= set('-:') and c for c in r):
            out.append('|' + '|'.join('-' * (w[i] + 2) for i in range(n)) + '|')
        else:
            out.append('| ' + ' | '.join(r[i].ljust(w[i]) for i in range(n)) + ' |')
    return out

path = sys.argv[1]
lines = open(path, encoding='utf-8').read().split('\n')
res, buf = [], []
for ln in lines + ['']:
    if ln.startswith('|'):
        buf.append(ln)
        continue
    if buf:
        res.extend(align(buf)); buf = []
    res.append(ln)
open(path, 'w', encoding='utf-8').write('\n'.join(res[:-1]))
