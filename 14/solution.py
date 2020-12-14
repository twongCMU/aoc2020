#!/usr/bin/python3

import math
import re
from collections import defaultdict

instructions = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        instructions.append(v)

memory = defaultdict(int)
mask = None
mask1 = None
mask0 = None
for i in instructions:
    if i[0:4] == "mask":
        (_, mask) = i.split(" = ")

        # all X replaced with 0 so we just keep all 1s
        mask1 = int(mask.replace("X", "0"), 2)

        # all X replaced with 1 so we remove all 0s
        mask0 = int(mask.replace("X", "1"), 2)
    else:
        (mem, val) = i.split(" = ")
        address = mem[4:-1]

        adjusted_val = int(val) & mask0
        adjusted_val = adjusted_val | mask1
        memory[address] = adjusted_val
        
print("Part 1: " + str(sum(memory.values())))
        
