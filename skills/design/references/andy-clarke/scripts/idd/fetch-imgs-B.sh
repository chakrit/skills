#!/bin/sh
# Download selected Group B article images (Storch, Feitler, Brody, Lubalin) at 1000px.
# usage: fetch-imgs-B.sh   ; writes raw/idd/img/<prefix>-<orig basename>
R=/Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/raw/idd
O=$R/img
get() { # $1 article slug, $2 prefix, $3 grep pattern for image numbers
  grep -o 'https://archive.smashing.media/assets/[^ ]*' "$R/inspired-design-decisions-$1.txt" \
    | sed 's/[]]$//' | sort -u | grep -E -e "$3" | while read -r u; do
      f="$O/$2-$(basename "$u")"
      [ -s "$f" ] || { curl -sL -A "Mozilla/5.0" "https://res.cloudinary.com/indysigner/image/fetch/f_auto,q_80/w_1000/$u" -o "$f"; sleep 1; }
    done
}
get otto-storch storch '/(0[2-6]|08|09|12|13|14|16|19|20|21|24|25|26|27|28)-'
get bea-feitler feitler '-(0[3-8]|10|12|13|16|19|21|23|28|31|33|35)-'
get neville-brody brody '/(0[2-5]|07|08|10|13|14|16|17|19|20)-'
get herb-lubalin lubalin '-(0[2-9]|1[0-3]|17|22|23|24|25|27)-'
