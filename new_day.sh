#!/bin/bash

CURRENT_DAY=$(date '+%d')
FILENAME="day$CURRENT_DAY.py"

if [ ! -f days/$FILENAME ]; then
    echo ">> Creating $FILENAME"
    cat days/day00.py | sed -r "s/\{day\}/$CURRENT_DAY/g" > days/$FILENAME
else
    echo ">> $FILENAME already exists"
fi

python days/$FILENAME
