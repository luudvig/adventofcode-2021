#!/usr/bin/env python3

with open('input') as f:
    scores, subsystem = [], f.read().splitlines()

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 1, ']': 2, '}': 3, '>': 4}

for l in subsystem:
    openings, score = [], 0
    for c in l:
        if c in pairs:
            openings.append(c)
        elif c == pairs[openings[-1]]:
            del openings[-1]
        else:
            break
    else:
        for c in (pairs[o] for o in reversed(openings)):
            score = score * 5 + points[c]
        scores.append(score)

print(sorted(scores)[int(len(scores)/2)])
