#!/bin/sh -eu

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

CC="${CC:-cc}"

>&2 echo "CC = ${CC}"
case "${CC}" in
    clang-5.0)
        "${CC}" -std=c11 \
            -Weverything -fcolor-diagnostics \
            -fsanitize=address,integer,undefined \
            -march=native -O0 -g \
            -o test_one main.c one.c

        "${CC}" -std=c11 \
            -Weverything -fcolor-diagnostics \
            -march=native -O0 -g \
            --shared -fPIC -o one.so one.c
        ;;
    gcc)
        "${CC}" -std=c11 \
            -Wall -Wextra \
            -fsanitize=address,undefined \
            -march=native -O0 -g \
            -o test_one main.c one.c

        "${CC}" -std=c11 \
            -Wall -Wextra \
            -march=native -O0 -g \
            --shared -fPIC -o one.so one.c
        ;;
    *)
        "${CC}" -std=c11 \
            -Wall -Wextra -O0 -g \
            -o test_one main.c one.c

        "${CC}" -std=c11 \
            -Wall -Wextra -O0 -g \
            --shared -fPIC -o one.so one.c
esac

./cffi_build.py
