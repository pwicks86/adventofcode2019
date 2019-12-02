#!/usr/bin/env python3
with open("input.txt", "r") as f:
    mem = [int(c) for c in f.read().strip().split(",")]

def run(n, v):
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

print(run(12, 2))

