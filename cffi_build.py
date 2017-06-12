#!/usr/bin/env python3

# This file is part of hashtable.
#
# Copyright (c) 2017, Martin Stensgård.
# All rights reserved.
#
# hashtable is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, only version 3 of the License.
#
# hashtable is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with hashtable. If not, see <http://www.gnu.org/licenses/>.

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
