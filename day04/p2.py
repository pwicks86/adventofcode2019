#!/usr/bin/env python3
from itertools import groupby
with open("input.txt", "r") as f:
    low, high = map(int, f.read().split("-"))

n = set()
for i in range(low, high + 1):
    s = str(i)
    ll = [list(grp) for k, grp in groupby(s)]
    matching = [l for l in ll if len(l) == 2]
    if len(matching) == 0:
        continue
    chars = [c for c in s]
    chars.sort()
    s2 = "".join(chars)
    if s2 == s:
        print(s)
        n.add(s)

print(len(n))
