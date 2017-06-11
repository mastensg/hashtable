#!/bin/sh -eu

#find | entr -c sh -c './build.sh && ./test_one'
#find | entr -c sh -c './build.sh && ./hashtable.py one'
ls -d * | entr -c sh -c './build.sh && ./check.py'
