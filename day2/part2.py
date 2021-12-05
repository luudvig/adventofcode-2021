#!/usr/bin/env python3

with open('input') as f:
    instr, a, x, y = f.readlines(), 0, 0, 0

for i in instr:
    if i.startswith('forward'):
        x, y = x + int(i.split()[1]), y + a * int(i.split()[1])
    else:
        a = a + int(i.split()[1]) if i.startswith('down') else a - int(i.split()[1])

print(x * y)
