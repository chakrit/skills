#!/bin/sh
# usage: shoot390h.sh <url> <name> [iframe-height]
# Phone view with a realistic iframe height (default 844), so vh units match a phone.
# Writes shots/idd/<name>-390h.png (600 wide; left 390 px is the phone view).
u="$1"; n="$2"; IH="${3:-844}"
D=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/shots/idd
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W="$D/frame-$n.html"
printf '<!doctype html><body style="margin:0;background:#888"><iframe src="%s" style="width:390px;height:%spx;border:0;background:#fff;display:block"></iframe></body>' "$u" "$IH" > "$W"
"$C" --headless --hide-scrollbars --virtual-time-budget=6000 --screenshot="$D/$n-390h.png" --window-size=600,$IH "file://$W" 2>/dev/null
rm -f "$W"
