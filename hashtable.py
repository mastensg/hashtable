#!/usr/bin/env python3

# pythonic interface to the hashtables

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

import cffi

import _hashtable


class Library(object):

    def __init__(self, variant):
        self.lib = _hashtable.ffi.dlopen("./{}.so".format(variant))

    def new(self):
        return self.lib.ht_new()

    def free(self, ht):
        return self.lib.ht_free(ht)

    def find(self, ht, value, key):
        return self.lib.ht_find(ht, value, key)

    def insert_or_assign(self, ht, key, value):
        return self.lib.ht_insert_or_assign(ht, key, value)

    def delete(self, ht, key):
        return self.lib.ht_delete(ht, key)


class Hashtable(object):

    def __init__(self, library):
        self.lib = library

        ht = self.lib.new()
        assert ht
        self.ht = ht

    def __contains__(self, key):
        value = _hashtable.ffi.new("uint64_t *")

        ret = self.lib.find(self.ht, value, key)
        assert ret in (self.lib.lib.HT_OK, self.lib.lib.HT_NOT_FOUND)

        return ret == self.lib.lib.HT_OK

    def __delitem__(self, key):
        ret = self.lib.delete(self.ht, key)
        assert ret in (self.lib.lib.HT_OK, self.lib.lib.HT_NOT_FOUND)

        if ret == self.lib.lib.HT_NOT_FOUND:
            raise KeyError(key)

    def __getitem__(self, key):
        value = _hashtable.ffi.new("uint64_t *")

        ret = self.lib.find(self.ht, value, key)
        assert ret in (self.lib.lib.HT_OK, self.lib.lib.HT_NOT_FOUND)

        if ret == self.lib.lib.HT_NOT_FOUND:
            raise KeyError(key)

        return value[0]

    def __setitem__(self, key, value):
        ret = self.lib.insert_or_assign(self.ht, key, value)
        assert ret == self.lib.lib.HT_OK


def main():
    import argparse
    parser = argparse.ArgumentParser(description="test hashtable")
    parser.add_argument("variant", help="which implementation variant to test")
    args = parser.parse_args()

    lib = Library(args.variant)

    ht = Hashtable(lib)

    assert 1 not in ht

    try:
        ht.__delitem__(1)
    except KeyError:
        pass
    else:
        assert False, "expected KeyError"

    try:
        ht[1]
    except KeyError:
        pass
    else:
        assert False, "expected KeyError"

    ht[1] = 1

    assert 1 in ht

    ht[1]

    ht.__delitem__(1)

if __name__ == "__main__":
    main()
