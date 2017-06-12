#!/bin/sh -eu

which pytest || true
which pytest-3 || true

./test_one
./hashtable.py one

if [ x"${TRAVIS:-false}" = x"true" ]
then
    pytest check.py
else
    ./check.py
fi
