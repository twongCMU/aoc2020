#!/usr/bin/python3

import math
import re
from collections import defaultdict

instructions = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        instructions.append(v)

# This assumes that the last instruction is a blank line and is the terminating condition
def run(instructions):
    seen = {}
    offset = 0
    accumulator = 0
    while 0 <= offset < len(instructions):
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
            accumulator += int(val)
            continue
        if inst == "jmp":
            offset += int(val)
            continue
    loop = offset in seen
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

