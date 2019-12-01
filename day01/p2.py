from math import floor
s = 0
for l in open("input.txt").readlines():
    f = int(floor((int(l)/3))) - 2
    s += f
    while f > 0:
        f = int(floor((int(f)/3))) - 2
        if f > 0:
            s += f

print(s)
