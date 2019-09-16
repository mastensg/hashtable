#!/usr/bin/env pytest-3

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

import hypothesis
import hypothesis.strategies as hs

import hashtable

# TODO(mastensg): parameterize variant
ht_lib = hashtable.Library("one")

keys = hs.integers(min_value=0, max_value=((1 << 64) - 1))
values = keys
key_value_pairs = hs.tuples(keys, values)
key_value_pair_lists = hs.lists(elements=key_value_pairs, min_size=0)


@hypothesis.settings(max_examples=10000, verbosity=hypothesis.Verbosity.verbose)
@hypothesis.given(key_value_pair_lists)
def test_insert_then_find(l):
    h = hashtable.Hashtable(ht_lib)
    d = dict()

    for kv in l:
        k, v = kv
        d[k] = v
        h[k] = v

    for k in d:
        assert d[k] == h[k]
