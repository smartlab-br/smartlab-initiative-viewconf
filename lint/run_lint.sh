#!/bin/bash
yamllint --format=parsable . > lint/report.txt

if [ $? -eq 0 ]
then
    echo ">>>>> Success - no lint errors"
else
    echo ">>>>> Error - check lint report"
    exit 0
fi