#!/bin/sh
# usage: shoot.sh <url> <name>   -> shots/idd/<name>-1400.png and <name>-390.png
# The 390 shot loads the page in a 390px iframe inside a wider window, because headless
# Chrome on macOS will not lay out a window narrower than about 500px. The 390 image is
# 600 wide: the left 390 px are the phone view, the grey strip on the right is padding.
u="$1"; n="$2"; H="${3:-2400}"
D=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/shots/idd
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W="$D/frame-$n.html"
printf '<!doctype html><body style="margin:0;background:#888"><iframe src="%s" style="width:390px;height:%spx;border:0;background:#fff;display:block"></iframe></body>' "$u" "$((H*2))" > "$W"
"$C" --headless --hide-scrollbars --virtual-time-budget=6000 --screenshot="$D/$n-1400.png" --window-size=1400,$H "$u" 2>/dev/null
"$C" --headless --hide-scrollbars --virtual-time-budget=6000 --screenshot="$D/$n-390-raw.png" --window-size=600,$((H*2)) "file://$W" 2>/dev/null
mv "$D/$n-390-raw.png" "$D/$n-390.png"
rm -f "$W"
