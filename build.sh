#!/bin/sh -eu

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
