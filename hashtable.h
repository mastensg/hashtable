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
