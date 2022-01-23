#!/usr/bin/env python3

with open('input') as f:
    score, subsystem = 0, f.read().splitlines()

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

for l in subsystem:
    openings = []
    for c in l:
        if c in pairs:
            openings.append(c)
        elif c == pairs[openings[-1]]:
            del openings[-1]
        else:
            score += points[c]
            break

print(score)
