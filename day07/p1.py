#!/usr/bin/env python3
from collections import namedtuple
import logging as l
from itertools import permutations
#l.basicConfig(level=l.DEBUG)

with open("input.txt", "r") as f:
    prog = [int(c) for c in f.read().strip().split(",")]

ArgBase = namedtuple("Arg", "num mode")

class Arg(ArgBase):
    def val(self, mem):
        if self.mode == 1:
            return self.num
        else:
            return mem[self.num]

    def __str__(self):
        return "Arg(mode={}, num={})".format(self.mode, self.num)

def run(mem, in_func=None, out_func=None):
    if not in_func:
        in_func = lambda: int(input("Enter integer: "))
    if not out_func:
        out_func = lambda v: print(v)
    pc = 0
    while True:
        op = str(mem[pc]).zfill(5)
        code = int(op[-2:])
        i1 = Arg(mem[pc + 1], int(op[-3])) if pc + 1 < len(mem) else None
        i2 = Arg(mem[pc + 2], int(op[-4])) if pc + 2 < len(mem) else None
        i3 = Arg(mem[pc + 3], int(op[-5])) if pc + 3 < len(mem) else None

        l.debug(f"code:{code}, i1:{i1}, i2: {i2}, i3:{i3}")

        if code == 1: # add
            #import pdb; pdb.set_trace()
            mem[i3.num] = i1.val(mem) + i2.val(mem)
            l.debug(f"mem[{i3.num}] = {i1.val(mem)} + {i2.val(mem)}")
            pc += 4
        elif code == 2: # multiply
            mem[i3.num] = i1.val(mem) * i2.val(mem)
            pc += 4
        elif code == 3: # input
            val = in_func()
            mem[i1.num] = val
            pc += 2
        elif code == 4: #output
            #print(mem[i1.val()], end="")
            out_func(i1.val(mem))
            pc += 2
        elif code == 5: # jump if true
            if i1.val(mem) != 0:
                pc = i2.val(mem)
            else:
                pc += 3
        elif code == 6: # jump if false
            if i1.val(mem) == 0:
                pc = i2.val(mem)
            else:
                pc += 3
        elif code == 7: # less than
            if i1.val(mem) < i2.val(mem):
                mem[i3.num] = 1
            else:
                mem[i3.num] = 0
            pc += 4
        elif code == 8: # equals
            if i1.val(mem) == i2.val(mem):
                mem[i3.num] = 1
            else:
                mem[i3.num] = 0
            pc += 4

        elif code == 99:
            break
        else:
            print("oh no")
            print(op)
            break
        #print(mem)

def list_input_func(l):
    l = l
    def f():
        return l.pop(0)
    return f

def list_output_func(l):
    def f(v):
        l.append(v)
    return f

max_in_sig = -99999999999999999
for p in permutations(range(0,5)):
    in_sig = 0
    for phase in p:
        #import pdb; pdb.set_trace()
        prog_copy = prog.copy()
        out_list = []
        run(prog_copy, in_func=list_input_func([phase,in_sig]), out_func=list_output_func(out_list))
        in_sig = out_list[0]
    max_in_sig = max(in_sig, max_in_sig)

print(max_in_sig)
