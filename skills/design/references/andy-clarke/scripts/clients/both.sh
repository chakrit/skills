#!/bin/sh
# Usage: both.sh <name> <url> -> 1400 and 390 shots, retrying when Wayback refuses
S=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/scripts-clients
D=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/shots/clients
for i in 1 2 3; do
  rm -f "$D/$1-1400.png"
  $S/shot1400.sh "$1" "$2"
  if [ -s "$D/$1-1400.png" ]; then break; fi
  sleep 10
done
sleep 4
$S/frame.sh "$1" "$2"
ls -la "$D/$1-1400.png" "$D/$1-390.png"
sleep 4
