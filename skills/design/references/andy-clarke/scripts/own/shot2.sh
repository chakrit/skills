#!/bin/sh
# Screenshot a URL with headless Chrome. Usage: shot.sh <out.png> <width> <height> <url>
out=$1; w=$2; h=$3; url=$4
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --hide-scrollbars --virtual-time-budget=15000 --timeout=40000 \
  --user-data-dir=/tmp/own-chrome-profile2 \
  --screenshot="$out" --window-size="$w,$h" "$url" >/dev/null 2>&1
ls -la "$out"
