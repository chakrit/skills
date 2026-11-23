# Extract article text, image alts/srcs, codepen links from a saved Smashing article HTML.
import sys, re, html
from html.parser import HTMLParser

src, url, out = sys.argv[1], sys.argv[2], sys.argv[3]
data = open(src, encoding='utf-8', errors='replace').read()
m = re.search(r'<div class="?c-garfield-the-cat"?.*', data, re.S)
body = data
start = data.find('id=article__content')
if start > 0:
    body = data[start:]
end = body.find('Smashing Editorial')
if end < 0: end = body.find('id=comments')
if end > 0: body = body[:end]

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.out=[]; self.skip=0
    def handle_starttag(self, t, a):
        a=dict(a)
        if t in ('script','style','svg','aside','nav','header','form'): self.skip+=1
        if t in ('p','h1','h2','h3','h4','li','blockquote','figcaption','pre','br','div'): self.out.append('\n')
        if t in ('h2','h3','h4'): self.out.append('#'*int(t[1])+' ')
        if t=='img':
            self.out.append('\n[IMG %s | %s]\n' % (a.get('alt',''), a.get('src','')))
        if t=='a' and a.get('href') and ('codepen' in a['href'] or 'stuffandnonsense' in a['href'] or 'github' in a['href']):
            self.out.append(' [LINK %s] ' % a['href'])
    def handle_endtag(self, t):
        if t in ('script','style','svg','aside','nav','header','form'): self.skip-=1
    def handle_data(self, d):
        if not self.skip: self.out.append(d)
def squash(m):
    code=html.unescape(re.sub(r'<[^>]+>','',m.group(0)))
    keep=[l.strip() for l in code.splitlines() if re.search(r'grid-template|grid-column|grid-row|grid-area|writing-mode|transform|rotate|shape-outside|columns|@media|min-width|column-count|font-size|clip-path|mix-blend|filter|float|initial-letter|::first-letter|vw|vh|fr', l)]
    return '<pre>[CODE] ' + ' | '.join(keep[:40]) + '</pre>'
body=re.sub(r'<pre.*?</pre>', squash, body, flags=re.S)
p=P(); p.feed(body)
txt=''.join(p.out)
txt=re.sub(r'\n\s*\n+', '\n\n', txt)
open(out,'w').write(url+'\n\n'+txt)
print(len(txt))
