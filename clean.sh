#!/bin/bash

if [ $# -eq 1 ]; then
    # Install python packages if needed
    pip install pandas openpyxl
fi

# run script
python cleaner.py $1