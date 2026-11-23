import sys, re, html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in ('script','style','svg','nav','footer','header'): s.skip+=1
        if t=='img':
            d=dict(a); s.out.append('\n[IMG %s | %s]\n'%(d.get('alt',''),d.get('src','')))
        if t in ('p','h1','h2','h3','h4','li','br','div','figcaption','blockquote','pre'): s.out.append('\n')
    def handle_endtag(s,t):
        if t in ('script','style','svg','nav','footer','header') and s.skip: s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
src,url,dst=sys.argv[1:4]
p=P(); p.feed(open(src,encoding='utf-8',errors='replace').read())
t=re.sub(r'\n\s*\n+','\n\n',''.join(p.out))
open(dst,'w').write(url+'\n'+t)
