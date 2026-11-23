#!/bin/sh
# Usage: fetch.sh <url> <name>
# Saves HTML to raw/talks/html/<name>.html and plain text (URL on line 1) to raw/talks/<name>.txt
set -e
base=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/raw/talks
url="$1"; name="$2"
curl -sL -A "Mozilla/5.0 (Macintosh) research-reader" -o "$base/html/$name.html" "$url"
echo "$url" > "$base/$name.txt"
textutil -convert txt -stdout -format html "$base/html/$name.html" 2>/dev/null | sed '/^[[:space:]]*$/N;/^\n$/D' >> "$base/$name.txt"
wc -c "$base/$name.txt"
sleep 2
