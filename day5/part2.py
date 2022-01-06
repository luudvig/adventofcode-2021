#!/usr/bin/env python3

with open('input') as f:
    diagram, lines = {}, (l.replace(' -> ', ',', 1) for l in f.readlines())

for v in (tuple(map(int, l.split(','))) for l in lines):
    if v[0] == v[2]:
        x_range = (v[0],) * (abs(v[1] - v[3]) + 1)
        y_range = range(min(v[1], v[3]), max(v[1], v[3]) + 1)
    elif v[1] == v[3]:
        x_range = range(min(v[0], v[2]), max(v[0], v[2]) + 1)
        y_range = (v[1],) * (abs(v[0] - v[2]) + 1)
    elif abs(v[0] - v[2]) == abs(v[1] - abs(v[3])):
        x_range = range(v[0], v[2] + 1 if v[0] < v[2] else v[2] - 1, 1 if v[0] < v[2] else -1)
        y_range = range(v[1], v[3] + 1 if v[1] < v[3] else v[3] - 1, 1 if v[1] < v[3] else -1)
    else:
        continue

    for p in zip(x_range, y_range):
        diagram[p] = diagram.get(p, 0) + 1

print(len(tuple(val for val in diagram.values() if val > 1)))
