#!/bin/bash

CURRENT_DAY=$(date '+%d')
FILENAME="day$CURRENT_DAY.py"
CURRENT_DATE=$(date '+%T - %d\/%m\/%y')

if [ ! -f days/$FILENAME ]; then
    echo ">> Creating $FILENAME"
    cat days/day00.py | \
        sed -r "s/\{day\}/$CURRENT_DAY/g" | \
        sed -r "s/\{date\}/$CURRENT_DATE/g" > days/$FILENAME
else
    echo ">> $FILENAME already exists"
fi

python days/$FILENAME
