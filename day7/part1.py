#!/usr/bin/env python3

with open('input') as f:
    cheapest, crabs = None, list(map(int, f.read().split(',')))

for p in range(min(crabs), max(crabs) + 1):
    cost = sum(abs(p - c) for c in crabs)
    if not cheapest or cost < cheapest:
        cheapest = cost

print(cheapest)
