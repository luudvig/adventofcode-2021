#!/usr/bin/env python3

with open('input') as f:
    answer, entries = [], (l.split(' | ') for l in f.read().splitlines())

for e in entries:
    digits = [None] * 10

    while not all(digits):
        for p in (set(s) for s in e[0].split()):
            if len(p) == 2:
                digits[1] = p
            if len(p) == 3:
                digits[7] = p
            if len(p) == 4:
                digits[4] = p
            if len(p) == 5:
                if digits[3] and digits[5] and p != digits[3] and p != digits[5]:
                    digits[2] = p
                if digits[1] and p.issuperset(digits[1]):
                    digits[3] = p
            if len(p) == 6:
                if digits[9] and p != digits[9]:
                    if digits[1] and p.issuperset(digits[1]):
                        digits[0] = p
                    if digits[0] and p != digits[0]:
                        digits[6] = p
                if digits[3] and p.issuperset(digits[3]):
                    digits[9] = p
            if len(p) == 7:
                digits[8] = p
            if digits[6] and digits[8] and digits[9]:
                digits[5] = digits[9] - (digits[8] - digits[6])

    answer.append(int(''.join(str(digits.index(set(d))) for d in e[1].split())))

print(sum(answer))
