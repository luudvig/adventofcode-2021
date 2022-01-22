#!/usr/bin/env python3

with open('input') as f:
    heightmap, risk = tuple(tuple(int(p) for p in r) for r in f.read().splitlines()), 0

for y, r in enumerate(heightmap):
    for x, p in enumerate(r):
        if ((y > 0 and p >= heightmap[y - 1][x]) or (y < len(heightmap) - 1 and p >= heightmap[y + 1][x])
                or (x > 0 and p >= heightmap[y][x - 1]) or (x < len(r) - 1 and p >= heightmap[y][x + 1])):
            continue
        risk += p + 1

print(risk)
