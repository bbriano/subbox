#!/bin/bash

set -e

dir=$1
if [ $# -eq 0 ]; then
    dir=$(date +%Y-%m-%d)
fi
echo $dir

cd $(dirname $0)/$dir

ls *.mkv *.mp4 *.webm | tr '\n' '\0' | \
    xargs -0 /Applications/VLC.app/Contents/MacOS/VLC
