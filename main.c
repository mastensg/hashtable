#include <assert.h>
#include <stdlib.h>

#include "hashtable.h"

int main() {
  void *ht = ht_new();
  assert(ht);

  assert(HT_OK == ht_assign(ht, 2431, 2048));
  assert(HT_OK == ht_assign(ht, 2531, 2048));
  assert(HT_OK == ht_assign(ht, 2431, 9045));

  {
    uint64_t v;
    assert(HT_OK == ht_lookup(ht, &v, 2431));
    assert(9045 == v);
  }

  {
    uint64_t v;
    assert(HT_OK == ht_lookup(ht, &v, 2531));
    assert(2048 == v);
  }

  {
    uint64_t v;
    assert(HT_NOT_FOUND == ht_lookup(ht, &v, 2631));
  }

  assert(HT_OK == ht_delete(ht, 2431));

  {
    uint64_t v;
    assert(HT_NOT_FOUND == ht_lookup(ht, &v, 2431));
  }

  ht_free(ht);

  return EXIT_SUCCESS;
}
