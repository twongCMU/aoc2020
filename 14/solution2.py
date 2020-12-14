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

    else:
        (mem, val) = i.split(" = ")
        address = int(mem[4:-1])

        # replace all 1s in the mask
        adjusted_address = bin(address | mask1)[2:]

        # pad the address so it is the right length
        adjusted_address = '0'*(36-len(adjusted_address)) + adjusted_address

        # put the Xs back into the address
        for i, c in enumerate(mask):
            if c == 'X':
                adjusted_address = adjusted_address[:i] + 'X' + adjusted_address[i+1:]


        # loop over a queue of addresses that have an X in them
        # when we process one, we'll replace an X with 2 entries, 1 and 0 and put them back into the queu
        # loop over this until we run out, then stuff the non-X versions into address_list
        address_list = []
        mask_list = []
        mask_list.append(adjusted_address)
        while mask_list:
            mask_temp = mask_list.pop(0)
            x_index = mask_temp.find('X')
            if x_index >= 0:
                mask_list.append(mask_temp[:x_index] + '0' + mask_temp[x_index+1:])
                mask_list.append(mask_temp[:x_index] + '1' + mask_temp[x_index+1:])
            else:
                address_list.append(mask_temp)
                
        for add in address_list:
            memory[add] = int(val)
        
print("Part 2: " + str(sum(memory.values())))
