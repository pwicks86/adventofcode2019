#!/usr/bin/env python3
import re
with open("input.txt", "r") as f:
    low, high = map(int, f.read().split("-"))

n = set()
for i in range(low, high + 1):
    s = str(i)
    if re.search("(.)\\1", s):
        chars = [c for c in s]
        chars.sort()
        s2 = "".join(chars)
        if s2 == s:
            n.add(s)

print(len(n))
