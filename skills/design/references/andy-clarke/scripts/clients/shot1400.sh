#!/bin/sh
# Usage: shot1400.sh <name> <url> -> shots/clients/<name>-1400.png
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
D=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/shots/clients
"$C" --headless --hide-scrollbars --user-data-dir=/tmp/ac-clients/prof-$1 --virtual-time-budget=10000 --screenshot="$D/$1-1400.png" --window-size=1400,2400 "$2" >/dev/null 2>&1
