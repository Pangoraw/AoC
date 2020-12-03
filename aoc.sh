#!/bin/bash

YEAR="2020"
DAY_TRIMMED=$(date '+%-d')
CHALLENGE_URL="https://adventofcode.com/$YEAR/day/$DAY_TRIMMED"
CURRENT_DAY=$(date '+%d')
FILENAME="days/day$CURRENT_DAY.py"

xdg-open $CHALLENGE_URL

PATH=$HOME/anaconda3/bin:$PATH
./new_day.sh

(setsid emacs $FILENAME &)
