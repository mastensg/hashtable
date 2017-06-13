/*
 * This file is part of hashtable.
 *
 * Copyright (c) 2017, Martin Stensgård.
 * All rights reserved.
 *
 * hashtable is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, only version 3 of the License.
 *
 * hashtable is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with hashtable. If not, see <http://www.gnu.org/licenses/>.
 */

#include <assert.h>
#include <stdlib.h>

#include "hashtable.h"

int main() {
  void *ht = ht_new();
  assert(ht);

  assert(HT_OK == ht_insert_or_assign(ht, 2431, 2048));
  assert(HT_OK == ht_insert_or_assign(ht, 2531, 2048));
  assert(HT_OK == ht_insert_or_assign(ht, 2431, 9045));

  {
    uint64_t v;
    assert(HT_OK == ht_find(ht, &v, 2431));
    assert(9045 == v);
  }

  {
    uint64_t v;
    assert(HT_OK == ht_find(ht, &v, 2531));
    assert(2048 == v);
  }

  {
    uint64_t v;
    assert(HT_NOT_FOUND == ht_find(ht, &v, 2631));
  }

  assert(HT_OK == ht_erase(ht, 2431));

  {
    uint64_t v;
    assert(HT_NOT_FOUND == ht_find(ht, &v, 2431));
  }

  ht_free(ht);

  return EXIT_SUCCESS;
}
