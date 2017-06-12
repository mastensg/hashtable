#!/bin/sh -eu

which pytest || true
which pytest-3 || true

./test_one
./hashtable.py one
./check.py
