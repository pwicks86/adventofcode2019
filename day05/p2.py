#!/usr/bin/env python3
from collections import namedtuple
import logging as l
#l.basicConfig(level=l.DEBUG)

with open("input.txt", "r") as f:
    mem = [int(c) for c in f.read().strip().split(",")]

ArgBase = namedtuple("Arg", "num mode")

class Arg(ArgBase):
    def val(self):
        if self.mode == 1:
            return self.num
        else:
            return mem[self.num]

    def __str__(self):
        return "Arg(mode={}, num={})".format(self.mode, self.num)

def run():
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
            mem[i3.num] = i1.val() + i2.val()
            l.debug(f"mem[{i3.num}] = {i1.val()} + {i2.val()}")
            pc += 4
        elif code == 2: # multiply
            mem[i3.num] = i1.val() * i2.val()
            pc += 4
        elif code == 3: # input
            val = int(input("Enter integer: "))
            if (val > 9):
                raise Exception("bad val")
            mem[i1.num] = val
            pc += 2
        elif code == 4: #output
            #print(mem[i1.val()], end="")
            print(i1.val())
            pc += 2
        elif code == 5: # jump if true
            if i1.val() != 0:
                pc = i2.val()
            else:
                pc += 3
        elif code == 6: # jump if false
            if i1.val() == 0:
                pc = i2.val()
            else:
                pc += 3
        elif code == 7: # less than
            if i1.val() < i2.val():
                mem[i3.num] = 1
            else:
                mem[i3.num] = 0
            pc += 4
        elif code == 8: # equals
            if i1.val() == i2.val():
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

run()
