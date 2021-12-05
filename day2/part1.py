#!/usr/bin/env python3

with open('input') as f:
    instr, x, y = f.readlines(), 0, 0

for i in instr:
    if i.startswith('forward'):
        x = x + int(i.split()[1])
    else:
        y = y + int(i.split()[1]) if i.startswith('down') else y - int(i.split()[1])

print(x * y)
