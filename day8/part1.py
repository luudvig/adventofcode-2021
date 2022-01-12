#!/usr/bin/env python3

with open('input') as f:
    print(len(tuple(
        d for v in (l.split(' | ')[1] for l in f.readlines()) for d in v.split() if len(d) in (2, 3, 4, 7)
        )))
