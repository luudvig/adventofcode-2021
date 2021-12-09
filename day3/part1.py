#!/usr/bin/env python3

with open('input') as f:
    r, g, e = [[c for c in l[:-1]] for l in f.readlines()], [], []

for n in zip(*reversed(r)):
    m = int(max(n, key=n.count))
    g.append('1' if m else '0')
    e.append('0' if m else '1')

print(int(''.join(g), 2) * int(''.join(e), 2))
