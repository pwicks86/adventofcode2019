from math import floor
s = 0
for l in open("input.txt").readlines():
    s += int(floor((int(l)/3))) - 2

print(s)
