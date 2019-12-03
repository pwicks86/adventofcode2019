#!/usr/bin/env python3
from collections import namedtuple
P = namedtuple("P", "x y s")
with open("input.txt", "r") as f:
    wires = f.readlines()
w1, w2 = [l.strip().split(",") for l in wires]

def walk_wire(w):
    loc = P(0,0,0)
    spots = []
    seen_xy = set()
    for step in w:
        direction = step[0]
        dist = int(step[1:])
        if direction == "U":
            nloc = (loc[0], loc[1] + dist, loc[2] + dist)
        if direction == "D":
            nloc = (loc[0], loc[1] - dist, loc[2] + dist)
        if direction == "R":
            nloc = (loc[0] + dist, loc[1], loc[2] + dist)
        if direction == "L":
            nloc = (loc[0] - dist, loc[1], loc[2] + dist)

        xneg = 1 if direction == "R" else -1
        yneg = 1 if direction == "U" else -1
        for xstep in range(0,abs(nloc[0] - loc[0])):
            nx = loc[0] + xstep * xneg
            ny = loc[1]
            if (nx,ny) in seen_xy:
                continue
            spots.append(P(nx, ny, loc[2] + xstep))
            seen_xy.add((nx, ny))
        for ystep in range(0,abs(nloc[1] - loc[1])):
            nx = loc[0]
            ny = loc[1]+ ystep * yneg
            if (nx,ny) in seen_xy:
                continue
            spots.append(P(nx, ny, loc[2] + ystep))
            seen_xy.add((nx, ny))
        loc = nloc
    s = { (l.x, l.y): l for l in spots if not (l.x == 0 and l.y == 0)}
    return s

w1_set = walk_wire(w1)
w2_set = walk_wire(w2)
min_steps = 99999999999999999999999999999999999999
for k in set(w1_set.keys()).intersection(set(w2_set.keys())):
    total_steps = w1_set[k].s + w2_set[k].s
    min_steps = min(min_steps, total_steps)
print(min_steps)
