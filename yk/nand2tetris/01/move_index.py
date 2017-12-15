#!/usr/bin/env python3
# usage: printf "Not (in=in[{}], out=out[{}]);" | python3 move_index.py 16
import sys

n = int(sys.argv[1])
strings = sys.stdin.read()
n_count = strings.count("{}")

for i in range(n):
    args = [i]
    args *= n_count
    formatted = strings.format(*args)
    print(formatted)
