#ifndef HASHTABLE_H
#define HASHTABLE_H 1

#include <stdint.h>

enum ht_status { HT_OK, HT_NOT_FOUND, HT_OUT_OF_MEMORY };

void *ht_new(void);
void ht_free(void *ht);
int ht_lookup(void *ht, uint64_t *value, uint64_t key);
int ht_assign(void *ht, uint64_t key, uint64_t value);
int ht_delete(void *ht, uint64_t key);

#endif /* hashtable.h */
