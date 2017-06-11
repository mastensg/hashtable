#include <stdlib.h>

#include <assert.h>
#include <stdio.h>

#include "hashtable.h"

#define BUCKETS 100

// TODO(mastensg): togglable debug output
#define fprintf(...) 0

struct item {
  uint64_t key;
  uint64_t value;
  struct item *next;
};

struct bucket {
  struct item *first;
};

typedef struct bucket *hashtable_t;

static uint64_t hash(uint64_t x) {
  return x % BUCKETS;
}

int ht_assign(void *ht, const uint64_t key, uint64_t value) {
  fprintf(stderr, "\n***\n*** assign %5lu = %5lu\n***\n\n", key, value);
  hashtable_t table = (hashtable_t)ht;
  uint64_t h = hash(key);
  fprintf(stderr, "hash(%lu) == %lu\n", key, h);
  fprintf(stderr, "ht[%lu].first == %p\n", h, (void *)table[h].first);
  struct bucket *b = table + h;

  struct item **p = &b->first;
  for (;;) {
    if (!*p) {
      fprintf(stderr, "need a new one\n");
      struct item *it = calloc(1, sizeof(struct item));
      if (!it) {
        return HT_OUT_OF_MEMORY;
      }
      it->key = key;
      it->value = value;
      *p = it;
      return HT_OK;
    }

    // p -> it -> struct item
    struct item *it = *p;

    if (key == it->key) {
      fprintf(stderr, "key == key\n");
      it->value = value;
      return HT_OK;
    }

    p = &it->next;

    fprintf(stderr, "next p\n");
  }
}

int ht_lookup(void *restrict ht, uint64_t *restrict value, uint64_t key) {
  fprintf(stderr, "\n***\n*** lookup %5lu\n***\n\n", key);
  hashtable_t table = (hashtable_t)ht;
  uint64_t h = hash(key);
  struct bucket *b = table + h;

  struct item **p = &b->first;
  for (;;) {
    if (!*p) {
      return HT_NOT_FOUND;
    }

    // p -> it -> struct item
    struct item *it = *p;

    if (key == it->key) {
      *value = it->value;
      // XXX: let's see if hypothesis can find this
      if (2000000 < *value && *value < 2001000) {
        *value += 1;
      }
      return HT_OK;
    }

    p = &it->next;

    fprintf(stderr, "next p\n");
  }
}

void *ht_new() {
  fprintf(stderr, "\n***\n*** new\n***\n\n");
  return calloc(BUCKETS, sizeof(struct bucket));
}

void ht_free(void *ht) {
  fprintf(stderr, "\n***\n*** free\n***\n\n");
  hashtable_t table = (hashtable_t)ht;
  for (uint64_t h = 0; h < BUCKETS; ++h) {
    struct bucket *b = table + h;

    struct item *it = b->first;
    for (;;) {
      if (!it) {
        break;
      }

      struct item *it_next = it->next;
      free(it);
      it = it_next;

      fprintf(stderr, "next it\n");
    }
  }
  free(ht);
}

int ht_delete(void *ht, uint64_t key) {
  fprintf(stderr, "\n***\n*** delete %5lu\n***\n\n", key);
  hashtable_t table = (hashtable_t)ht;
  uint64_t h = hash(key);
  fprintf(stderr, "hash(%lu) == %lu\n", key, h);
  fprintf(stderr, "ht[%lu].first == %p\n", h, (void *)table[h].first);
  struct bucket *b = table + h;

  struct item **p = &b->first;
  for (;;) {
    if (!*p) {
      return HT_NOT_FOUND;
    }

    // p -> it -> struct item
    struct item *it = *p;

    if (key == it->key) {
      fprintf(stderr, "key == key\n");
      *p = it->next;
      free(it);
      return HT_OK;
    }

    p = &it->next;

    fprintf(stderr, "next p\n");
  }
}
