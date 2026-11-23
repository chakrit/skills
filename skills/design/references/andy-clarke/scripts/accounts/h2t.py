import sys, html, re
s = open(sys.argv[1], encoding='utf-8', errors='replace').read()
s = re.sub(r'(?is)<(script|style)\b.*?</\1>', '', s)
s = re.sub(r'(?i)<br\s*/?>|</p>|</li>|</h\d>|</div>|</blockquote>', '\n', s)
s = re.sub(r'(?s)<[^>]+>', '', s)
s = html.unescape(s)
s = re.sub(r'[ \t]+', ' ', s)
s = re.sub(r'\n\s*\n+', '\n\n', s)
url = sys.argv[2] if len(sys.argv) > 2 else ''
sys.stdout.write(url + '\n\n' + s)
