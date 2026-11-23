import sys,re
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
css=''.join(re.findall(r'<style[^>]*>(.*?)</style>',s,re.S))
css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
keys=('grid-template','grid-column','grid-row','grid-area','transform','writing-mode','font-size','mix-blend','shape-outside','background-color','column-count','clip-path','position:','mask','font-family','width','height','margin','align','justify','opacity','color:')
ctx=[];buf='';i=0
out=[]
for ch in css:
    if ch=='{':
        ctx.append(buf.strip()); buf=''
    elif ch=='}':
        body=buf; buf=''
        sel=ctx.pop() if ctx else ''
        if '#design' in sel:
            keep=[d.strip() for d in body.split(';') if any(k in d for k in keys)]
            media=' '.join(c for c in ctx if c.startswith('@'))
            if keep: out.append('[%s] %s { %s }'%(media or 'base',re.sub(r'\s+',' ',sel)[-80:],' ; '.join(keep)[:500]))
    else: buf+=ch
print('\n'.join(out))
