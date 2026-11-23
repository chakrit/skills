import sys, re
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
styles=re.findall(r'<style>(.*?)</style>',src,re.S)
for s in styles:
    if '#design' in s and '@font-face' not in s[:50]:
        s=re.sub(r'@font-face\s*\{[^}]*\}','',s)
        s=re.sub(r'\s+',' ',s)
        s=s.replace('}','}\n')
        print(s)
# markup inside #design
m=re.search(r'<div id="design".*?(?=<footer|<div class="alt-tabs")',src,re.S) or re.search(r'id="design".{0,20000}',src,re.S)
if m:
    t=m.group(0)
    t=re.sub(r'<svg.*?</svg>','<svg/>',t,flags=re.S)
    t=re.sub(r'\s+',' ',t)
    print('=== MARKUP ===')
    print(t[:6000])
