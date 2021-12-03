#!/usr/bin/env python3

with open('input') as f:
    m = list(map(int, f.readlines()))

print(len(
    [d for i, d in enumerate(m[3:], 3) if sum(m[i - 2:i + 1]) > sum(m[i - 3:i])]
    ))
