#!/bin/sh -eu

./test_one

./hashtable.py one

if [ x"${TRAVIS:-false}" = x"true" ]
then
    pytest check.py
else
    ./check.py
fi
