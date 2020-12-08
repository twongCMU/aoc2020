#!/usr/bin/python3

import math
import re
from collections import defaultdict
bags = defaultdict(dict)

instructions = []

with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        instructions.append(v)
print(str(instructions))
def run(instructions):
    seen = {}
    offset = 0
    accumulator = 0
    while 1:
        if offset < 0 or offset >= len(instructions):
            break
        if len(instructions[offset]) < 1:
            break
        (inst, val) = instructions[offset].split(" ")

        if offset in seen:
            break
        seen[offset] = 0
        if inst == "nop":
            offset += 1
            continue
        if inst == "acc":
            offset += 1
            if val[0] == "-":
                accumulator -= int(val[1:])
            elif val[0] == "+":
                accumulator += int(val[1:])
            continue
        if inst == "jmp":
            if val[0] == "-":
                offset -= int(val[1:])
            elif val[0] == "+":
                offset += int(val[1:])
            continue
    loop = False
    if offset in seen:
        loop = True
    return (accumulator, loop)

print("Part 1: " + str(run(instructions)[0]))

for k, v in enumerate(instructions):
    new_inst = instructions.copy()
    (inst, val) = v.split(" ")
    if inst == "nop":
        new_inst[k] = "jmp " + val
    elif inst == "jmp":
        new_inst[k] = "nop " + val
    else:
        continue
    (res, loop) = run(new_inst)
    if not loop:
        print("Part 2: " + str(res))

