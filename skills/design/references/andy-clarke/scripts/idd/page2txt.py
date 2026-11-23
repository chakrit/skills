# usage: page2txt.py <html file> <url> <out txt>  -- generic main-text extraction
import sys, re, html
src, url, out = sys.argv[1:4]
d = open(src, encoding='utf-8', errors='replace').read()
d = re.sub(r'<(script|style|svg|nav|footer|form)[^>]*>.*?</\1>', '', d, flags=re.S | re.I)
m = re.search(r'<main.*?</main>', d, re.S) or re.search(r'<article.*?</article>', d, re.S)
if m: d = m.group(0)
d = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*src="([^"]*)"[^>]*>', r'\n[IMG \1 | \2]\n', d)
d = re.sub(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*>', r'\n[IMG \2 | \1]\n', d)
d = re.sub(r'</?(p|h\d|li|blockquote|figcaption|div|br|section)[^>]*>', '\n', d)
t = html.unescape(re.sub(r'<[^>]+>', '', d))
t = re.sub(r'[ \t]+', ' ', t); t = re.sub(r'\n\s*\n+', '\n\n', t)
open(out, 'w').write(url + '\n\n' + t.strip() + '\n')
print(len(t))
