#!/usr/bin/env python3
with open("input.txt", "r") as f:
    lines = f.readlines()

orbits = {}
objects = set()
for l in lines:
    inner, outer = l.strip().split(")")
    orbits[outer] = inner
    objects.add(outer)
    objects.add(inner)

objects.remove("COM")
santa_orbit = orbits["SAN"]
you_orbit = orbits["YOU"]

def get_list(start):
    l = []
    inner = orbits[start]
    l.append(inner)
    while inner != "COM":
        inner = orbits[inner]
        l.append(inner)
    return l

s_list = get_list("SAN")
y_list = get_list("YOU")
q = False
for v in y_list:
    for v2 in s_list:
        if v == v2:
            match_spot = v
            q = True
            break
    if q:
        break
print(s_list.index(match_spot) + y_list.index(match_spot))
