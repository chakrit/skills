#!/bin/sh
# usage: getimgs.sh <article.txt> <prefix> <name-substring>...
# Downloads matching article images at 1400px wide into raw/idd/img/<prefix>-<basename>.
R=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/raw/idd
f="$1"; p="$2"; shift 2
for s in "$@"; do
  u=$(grep -o 'https://res.cloudinary.com[^]]*' "$f" | grep "/$s" | head -n 1)
  [ -z "$u" ] && { echo "miss $s"; continue; }
  u=$(echo "$u" | sed 's#/w_400/#/w_1400/#')
  b=$(basename "$u")
  curl -s -L -o "$R/img/$p-$b" "$u" && echo "ok $p-$b"
  sleep 1
done
