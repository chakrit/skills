#!/bin/sh
# usage: get.sh <url> <name>  -> raw/idd/<name>.html and <name>.txt
cd /Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/raw/idd
curl -sL -A "Mozilla/5.0" "$1" -o "$2.html"
/usr/bin/python3 -I ../../scripts-idd/page2txt.py "$2.html" "$1" "$2.txt"
