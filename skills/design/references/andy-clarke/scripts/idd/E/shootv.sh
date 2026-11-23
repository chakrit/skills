#!/bin/sh
# usage: shootv.sh <url> <name>
# Realistic-viewport shots: 1400x1000 window, and a 390x844 phone iframe (first screen only).
# The standard shoot.sh uses tall windows, which inflate designs sized with vh units.
u="$1"; n="$2"
D=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/shots/idd
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W="$D/frame-$n.html"
printf '<!doctype html><body style="margin:0;background:#888"><iframe src="%s" style="width:390px;height:844px;border:0;background:#fff;display:block"></iframe></body>' "$u" > "$W"
"$C" --headless --hide-scrollbars --virtual-time-budget=6000 --screenshot="$D/$n-1400.png" --window-size=1400,1000 "$u" 2>/dev/null
"$C" --headless --hide-scrollbars --virtual-time-budget=6000 --screenshot="$D/$n-390.png" --window-size=600,900 "file://$W" 2>/dev/null
rm -f "$W"
