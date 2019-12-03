#!/usr/bin/env python3
with open("input.txt", "r") as f:
    wires = f.readlines()
w1, w2 = [l.strip().split(",") for l in wires]

def walk_wire(w):
    loc = (0,0)
    spots = []
    for step in w:
        direction = step[0]
        dist = int(step[1:])
        if direction == "U":
            nloc = (loc[0], loc[1] + dist)
        if direction == "D":
            nloc = (loc[0], loc[1] - dist)
        if direction == "R":
            nloc = (loc[0] + dist, loc[1])
        if direction == "L":
            nloc = (loc[0] - dist, loc[1])

        xneg = 1 if direction == "R" else -1
        yneg = 1 if direction == "U" else -1
        for xstep in range(0,abs(nloc[0] - loc[0])):
            spots.append((loc[0] + xstep * xneg, loc[1]))
        for ystep in range(0,abs(nloc[1] - loc[1])):
            spots.append((loc[0], loc[1] + ystep * yneg))
        loc = nloc
    s = set(spots)
    s.remove((0,0))
    return s

w1_set = walk_wire(w1)
w2_set = walk_wire(w2)
print(sum(map(abs, min(w1_set.intersection(w2_set), key=lambda p: abs(p[0]) + abs(p[1])))))
