#!/bin/sh
# usage: fetch.sh <path like 2019/06/slug>   (run from raw/idd)
s="$1"; n=$(basename "$s"); u="https://www.smashingmagazine.com/$s/"
curl -sL -A "Mozilla/5.0" "$u" -o "$n.html"
/usr/bin/python3 -I ../../scripts-idd/extract.py "$n.html" "$u" "$n.txt"
