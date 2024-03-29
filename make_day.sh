#!/bin/bash
DAY=$1
DAY_PAD=$(printf "%02d" $DAY)
mkdir day$DAY_PAD
session=$(cat session.txt)
curl "http://adventofcode.com/2019/day/$DAY/input" -H "Cookie: session=$session" -o day$DAY_PAD/input.txt 

cat << EOF > day$DAY_PAD/p1.py

#!/usr/bin/env python3
with open("input.txt", "r") as f:
    lines = f.readlines()

for l in lines:
    # stuff goes here
EOF

cp day$DAY_PAD/p1.py day$DAY_PAD/p2.py

chmod +x day$DAY_PAD/p1.py day$DAY_PAD/p2.py

