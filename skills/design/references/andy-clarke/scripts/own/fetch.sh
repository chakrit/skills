#!/bin/sh
# Fetch each blog slug politely and extract its text. Usage: fetch.sh slugs.txt
base=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke
while read -r s; do
  [ -z "$s" ] && continue
  u="https://stuffandnonsense.co.uk/blog/$s/"
  h="$base/raw/own/html/p-$s.html"
  [ -f "$h" ] || { curl -sL -o "$h" "$u"; sleep 2; }
  /usr/bin/python3 -I "$base/scripts-own/extract.py" "$u" "$h" "$base/raw/own/$s.txt"
done < "$1"
