#!/bin/bash

SEARCHSTRING=${1:-test}

rm -rf tmp/testspace
mkdir -p tmp/testspace

find test -name "test_*.py" -exec cp {} ./tmp/testspace/ \;

export PYTHONPATH=($PYTHONPATH):`pwd`/src/

pytest tmp/testspace/* --cov=src -k $SEARCHSTRING

rm -rf tmp/testspace