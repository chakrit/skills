# usage: python3 -I blogtext-B.py <html> <url> <out.txt>
# Crude text extraction of a stuffandnonsense blog post or demo page (paragraphs, headings, img alts).
import sys, re, html
src = open(sys.argv[1], encoding="utf-8", errors="replace").read()
src = re.sub(r"(?is)<(script|style|svg|noscript)\b.*?</\1>", " ", src)
src = re.sub(r"(?is)<img\b[^>]*?alt=\"([^\"]*)\"[^>]*?src=\"([^\"]*)\"[^>]*>", r"\n[IMG \1 | \2]\n", src)
src = re.sub(r"(?is)<img\b[^>]*?src=\"([^\"]*)\"[^>]*?alt=\"([^\"]*)\"[^>]*>", r"\n[IMG \2 | \1]\n", src)
src = re.sub(r"(?is)<(h[1-6])[^>]*>", lambda m: "\n" + "#" * int(m.group(1)[1]) + " ", src)
src = re.sub(r"(?is)</?(p|div|li|section|article|header|footer|main|aside|h[1-6]|br|figure|figcaption|blockquote)\b[^>]*>", "\n", src)
src = re.sub(r"(?s)<[^>]+>", "", src)
txt = html.unescape(src)
lines = [re.sub(r"[ \t]+", " ", l).strip() for l in txt.splitlines()]
out = [l for l in lines if l]
open(sys.argv[3], "w", encoding="utf-8").write(sys.argv[2] + "\n\n" + "\n".join(out) + "\n")
