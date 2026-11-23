#!/bin/sh
# Usage: frame.sh <name> <url> -> shots/clients/<name>-390.png via a 390px iframe in a 600px window
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
D=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/shots/clients
W=/tmp/cc-frame-$1.html
printf '<html><body style="margin:0;background:#888"><iframe src="%s" style="width:390px;height:2400px;border:0;display:block;background:#fff"></iframe></body></html>' "$2" > $W
"$C" --headless --hide-scrollbars --virtual-time-budget=10000 --screenshot="$D/$1-390.png" --window-size=600,2400 "file://$W" >/dev/null 2>&1
