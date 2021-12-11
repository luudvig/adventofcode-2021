#!/usr/bin/env python3

def bingo(numbers, boards):
    for n in numbers:
        for b in boards:
            for r in b:
                for i, c in enumerate(r):
                    if c[0] == n:
                        c[1] = True
                        if all(c[1] for c in r) or all(r[i][1] for r in b):
                            return n, b

with open('input') as f:
    boards = f.read().split('\n\n')

numbers = tuple(n for n in boards.pop(0).split(','))
boards = [[[[n, False] for n in r.split()] for r in b.rstrip().split('\n')] for b in boards]

called, board = bingo(numbers, boards)
unmarked = sum(sum(int(c[0]) for c in r if not c[1]) for r in board)

print(int(called) * unmarked)
