#!/usr/bin/env python3

with open('input') as f:
    m = list(map(int, f.readlines()))

print(len(
    [d for i, d in enumerate(m[1:], 1) if d > m[i - 1]]
    ))
