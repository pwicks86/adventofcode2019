#!/usr/bin/env python3
import sys
with open("input.txt", "r") as f:
    mem = [int(c) for c in f.read().strip().split(",")]
    mem_o = mem.copy()

def run(n, v):
    mem = mem_o.copy()
    mem[1] = n
    mem[2] = v
    pc = 0
    while True:
        op = mem[pc]
        i1 = mem[pc + 1]
        i2 = mem[pc + 2]
        out = mem[pc + 3]
        if op == 1:
            mem[out] = mem[i1] + mem[i2]
        elif op == 2:
            mem[out] = mem[i1] * mem[i2]
        elif op == 99:
            break
        else:
            print("oh no")
            print(op)
            break
        pc += 4
    return mem[0]

for nv in range(0, 100):
    for vv in range(0, 100):
        if run(nv,vv) == 19690720:
            print(100 * nv + vv)
            sys.exit(0)

