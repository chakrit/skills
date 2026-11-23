#!/bin/sh
# usage: shoot1400v.sh <url> <name> [height]
# Desktop view at a realistic window height (default 900) so vh units match a laptop.
# Writes shots/idd/<name>-1400v.png.
u="$1"; n="$2"; H="${3:-900}"
D=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/shots/idd
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$C" --headless --hide-scrollbars --virtual-time-budget=6000 --screenshot="$D/$n-1400v.png" --window-size=1400,$H "$u" 2>/dev/null
