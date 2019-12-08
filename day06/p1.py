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
count = 0
for o in objects:
    inner = orbits[o]
    count += 1
    while inner != "COM":
        inner = orbits[inner]
        count += 1

print(count)
