# usage: python3 -I demo-css-B.py <demo.html>
# Print inline <style> rules from a demo page that carry layout-relevant declarations.
import sys, re
s = open(sys.argv[1], encoding="utf-8", errors="replace").read()
css = "\n".join(re.findall(r"(?is)<style[^>]*>(.*?)</style>", s))
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
keys = ("grid", "rotate", "writing-mode", "shape-outside", "font-size", "@media", "transform",
        "column", "order", "margin", "max-width", "width", "clip", "blend", "background", "position")
for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
    sel, body = m.group(1).strip(), m.group(2)
    decl = [d.strip() for d in body.split(";") if any(k in d for k in keys)]
    if decl and "site-" not in sel and "nav" not in sel:
        print(sel[-90:], "{", "; ".join(decl)[:400], "}")
for q in re.findall(r"@media[^{]+", css):
    pass
print("MEDIA:", sorted(set(q.strip() for q in re.findall(r"@media[^{]+", css))))
