import sys, re, html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        a=dict(a)
        if t in ('script','style','svg','nav','footer','head'): s.skip+=1
        if t=='img' and not s.skip: s.out.append('\n[IMG %s | %s]\n'%(a.get('alt',''),a.get('src','')))
        if t in ('p','h1','h2','h3','h4','li','br','div','section','figure','blockquote'): s.out.append('\n')
    def handle_endtag(s,t):
        if t in ('script','style','svg','nav','footer','head') and s.skip: s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
p=P(); p.feed(src)
t=re.sub(r'\n\s*\n+','\n\n',''.join(p.out))
print(sys.argv[2]); print(t)
