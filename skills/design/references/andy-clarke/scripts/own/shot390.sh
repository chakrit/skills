#!/bin/sh
# Screenshot a URL at 390 px wide by loading it in a 390 px iframe inside a 500 px window.
# Usage: shot390.sh <out.png> <url> [profile-suffix]
out=$1; url=$2; p=${3:-3}
wrap=/tmp/own-wrap-$p.html
printf '<!doctype html><body style="margin:0;background:#888"><iframe src="%s" style="border:0;width:390px;height:3000px;display:block"></iframe></body>' "$url" > "$wrap"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --hide-scrollbars --virtual-time-budget=15000 --timeout=40000 \
  --user-data-dir=/tmp/own-chrome-profile$p \
  --screenshot="$out" --window-size=500,3000 "file://$wrap" >/dev/null 2>&1
ls -la "$out"
