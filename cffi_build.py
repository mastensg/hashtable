#!/usr/bin/env python3

import argparse

import cffi


def main():
    parser = argparse.ArgumentParser(
        description="generate python wrapper around c code")

    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    with open("hashtable.h") as f:
        no_hash = lambda l: not l.startswith("#")
        hashtable_h = "".join(filter(no_hash, f.readlines()))

    ffi = cffi.FFI()
    ffi.cdef(hashtable_h)
    ffi.set_source("_hashtable", None)
    ffi.compile(verbose=args.verbose)

if __name__ == "__main__":
    main()
