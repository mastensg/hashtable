#!/usr/bin/env pytest-3

import hypothesis
import hypothesis.strategies as hs

import hashtable

# TODO(mastensg): parameterize variant
ht_lib = hashtable.Library("one")

keys = hs.integers(min_value=0, max_value=((1 << 64) - 1))
values = keys
key_value_pairs = hs.tuples(keys, values)
key_value_pair_lists = hs.lists(elements=key_value_pairs, min_size=0)


@hypothesis.given(key_value_pair_lists)
@hypothesis.settings(max_examples=10000)
@hypothesis.settings(verbosity=hypothesis.Verbosity.verbose)
def test_insert_then_find(l):
    h = hashtable.Hashtable(ht_lib)
    d = dict()

    for kv in l:
        k, v = kv
        d[k] = v
        h[k] = v

    for k in d:
        assert d[k] == h[k]
