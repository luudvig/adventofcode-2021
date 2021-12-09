#!/usr/bin/env python3

with open('input') as f:
    r1 = f.read().splitlines()
    r2 = r1.copy()

for p in range(len(r1[0])):
    if len(r1) > 1:
        b1 = '1' if len([n for n in r1 if n[p] == '1']) >= len(r1) / 2 else '0'
        r1 = [n for n in r1 if n[p] == b1]
    if len(r2) > 1:
        b2 = '0' if len([n for n in r2 if n[p] == '0']) <= len(r2) / 2 else '1'
        r2 = [n for n in r2 if n[p] == b2]

print(int(''.join(r1[0]), 2) * int(''.join(r2[0]), 2))
