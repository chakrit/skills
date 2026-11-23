#!/bin/sh
# Fetch Group B "52 weeks" blog posts into raw/idd/demos-B/blog<N>.html
cd /Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/raw/idd/demos-B || exit 1
for x in "1 otto-storch" "2 herb-lubalin" "3 bea-feitler" "9 herb-lubalin" "15 herb-lubalin" "20 neville-brody"; do
  set -- $x
  u="https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-$1-$2/"
  code=$(curl -sL -A "Mozilla/5.0" -w '%{http_code}' "$u" -o "blog$1.html")
  echo "$1 $code $(wc -c < blog$1.html) $u"
  sleep 1
done
