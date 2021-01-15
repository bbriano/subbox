#!/bin/bash

set -e

iso_date=$(date '+%Y-%m-%d')
mkdir -p $iso_date
cd $(dirname $0)/$iso_date

cat ../subscriptions \
    | sed '/^#/d' \
    | sed '/^$/d' \
    | ../filter24h.py \
    | youtube-dl -a -
