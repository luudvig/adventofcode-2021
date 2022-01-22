#!/usr/bin/env python3

with open('input') as f:
    basins, heightmap = [], tuple(tuple(int(p) for p in r) for r in f.read().splitlines())

for y, r in enumerate(heightmap):
    basin = set()
    for x, p in enumerate(r):
        if p != 9:
            if y and heightmap[y - 1][x] != 9 and (y - 1, x) not in basin:
                for i, b in enumerate(basins):
                    if (y - 1, x) in b:
                        basin.update(basins.pop(i))
                        break
            basin.add((y, x))
        elif basin:
            basins.append(basin)
            basin = set()
    if basin:
        basins.append(basin)

b1, b2, b3 = sorted(basins, key=len)[-3:]
print(len(b1) * len(b2) * len(b3))
