#!/usr/bin/env python3

with open('input') as f:
    ages = tuple(map(int, f.read().split(',')))
    fish = [ages.count(i) for i in range(9)]

for i in range(256):
    fish.append(fish.pop(0))
    fish[6] += fish[8]

print(sum(fish))
