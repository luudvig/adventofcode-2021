#!/usr/bin/env python3

with open('input') as f:
    cheapest, crabs, mem = None, list(map(int, f.read().split(','))), {}

for p in range(min(crabs), max(crabs) + 1):
    cost = 0
    for c in crabs:
        steps = abs(p - c)
        cost += mem[steps] if steps in mem else mem.setdefault(steps, sum(range(1, steps + 1)))
    if not cheapest or cost < cheapest:
        cheapest = cost

print(cheapest)
