"""Extract readable main text from saved HTML. Usage: h2t.py in.html url out.txt"""
import sys, re, html
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.out=[]; self.skip=0
    def handle_starttag(self,t,a):
        if t in ('script','style','svg','noscript','head'): self.skip+=1
        if t in ('p','h1','h2','h3','h4','li','br','div','section','blockquote','figcaption'): self.out.append('\n')
        if t=='img':
            d=dict(a)
            if d.get('alt'): self.out.append(f"\n[img alt: {d.get('alt')} src: {d.get('src')}]\n")
        if t=='a':
            d=dict(a); h=d.get('href','')
            if h.startswith('http') and 'stuffandnonsense' not in h: self.out.append(f" <{h}> ")
    def handle_endtag(self,t):
        if t in ('script','style','svg','noscript','head') and self.skip: self.skip-=1
    def handle_data(self,d):
        if not self.skip: self.out.append(d)

src, url, dst = sys.argv[1:4]
p=P(); p.feed(open(src,encoding='utf-8',errors='replace').read())
txt=''.join(p.out)
txt=re.sub(r'[ \t]+',' ',txt); txt=re.sub(r'\n\s*\n+','\n\n',txt)
open(dst,'w').write(url+'\n\n'+txt.strip()+'\n')
