#!/bin/sh
# Usage: shoot.sh <name> <url>  -> shots/clients/<name>-1400.png and <name>-390.png
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
D=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/shots/clients
"$C" --headless --hide-scrollbars --virtual-time-budget=8000 --screenshot="$D/$1-1400.png" --window-size=1400,2400 "$2" >/dev/null 2>&1
"$C" --headless --hide-scrollbars --virtual-time-budget=8000 --screenshot="$D/$1-390.png" --window-size=390,2400 "$2" >/dev/null 2>&1
