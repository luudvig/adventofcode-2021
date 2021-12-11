#!/usr/bin/env python3

def bingo(numbers, boards, won=set()):
    for n in numbers:
        for i, b in enumerate(boards):
            for r in b:
                for j, c in enumerate(r):
                    if c[0] == n and i not in won:
                        c[1] = True
                        if all(c[1] for c in r) or all(r[j][1] for r in b):
                            number, board = n, b
                            won.add(i)
    return number, board

with open('input') as f:
    boards = f.read().split('\n\n')

numbers = tuple(n for n in boards.pop(0).split(','))
boards = [[[[n, False] for n in r.split()] for r in b.rstrip().split('\n')] for b in boards]

called, board = bingo(numbers, boards)
unmarked = sum(sum(int(c[0]) for c in r if not c[1]) for r in board)

print(int(called) * unmarked)
