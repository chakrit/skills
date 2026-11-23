"""Extract readable text from a saved HTML page. Usage: extract.py URL in.html out.txt"""
import sys, re
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []; self.skip = 0; self.inmain = 0; self.times = []
    def handle_starttag(self, t, a):
        a = dict(a)
        if t in ('script', 'style', 'svg', 'noscript'): self.skip += 1
        if t == 'main': self.inmain += 1
        if t == 'time' and a.get('datetime'): self.times.append(a['datetime'])
        if t in ('h1','h2','h3','h4'): self.out.append('\n\n## ')
        if t in ('p','li','br','blockquote','figcaption','div','section','article'): self.out.append('\n')
        if t == 'li': self.out.append('- ')
        if t == 'img' and a.get('alt'): self.out.append(' [img: %s] ' % a['alt'])
    def handle_endtag(self, t):
        if t in ('script', 'style', 'svg', 'noscript'): self.skip = max(0, self.skip-1)
        if t == 'main': self.inmain -= 1
        if t in ('h1','h2','h3','h4','p'): self.out.append('\n')
    def handle_data(self, d):
        if not self.skip: self.out.append(d)

url, src, dst = sys.argv[1:4]
html = open(src, encoding='utf-8', errors='replace').read()
m = re.search(r'<main.*?</main>', html, re.S)
body = m.group(0) if m else html
p = P(); p.feed(body)
text = re.sub(r'[ \t]+', ' ', ''.join(p.out))
text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text).strip()
with open(dst, 'w') as f:
    f.write(url + '\n')
    if p.times: f.write('dates: ' + ' '.join(sorted(set(p.times))[:3]) + '\n')
    f.write('\n' + text + '\n')
