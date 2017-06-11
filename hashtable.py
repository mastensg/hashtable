#!/usr/bin/env python3

# pythonic interface to the hashtables

import cffi

import _hashtable


class Library(object):

    def __init__(self, variant):
        self.lib = _hashtable.ffi.dlopen("./{}.so".format(variant))

    def new(self):
        return self.lib.ht_new()

    def free(self, ht):
        return self.lib.ht_free(ht)

    def lookup(self, ht, value, key):
        return self.lib.ht_lookup(ht, value, key)

    def assign(self, ht, key, value):
        return self.lib.ht_assign(ht, key, value)

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

        ret = self.lib.lookup(self.ht, value, key)
        assert ret in (self.lib.lib.HT_OK, self.lib.lib.HT_NOT_FOUND)

        return ret == self.lib.lib.HT_OK

    def __delitem__(self, key):
        ret = self.lib.delete(self.ht, key)
        assert ret in (self.lib.lib.HT_OK, self.lib.lib.HT_NOT_FOUND)

        if ret == self.lib.lib.HT_NOT_FOUND:
            raise KeyError(key)

    def __getitem__(self, key):
        value = _hashtable.ffi.new("uint64_t *")

        ret = self.lib.lookup(self.ht, value, key)
        assert ret in (self.lib.lib.HT_OK, self.lib.lib.HT_NOT_FOUND)

        if ret == self.lib.lib.HT_NOT_FOUND:
            raise KeyError(key)

        return value[0]

    def __setitem__(self, key, value):
        ret = self.lib.assign(self.ht, key, value)
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
