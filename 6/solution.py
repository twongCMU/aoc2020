#!/usr/bin/python3

from collections import defaultdict
import math
import re

seen = defaultdict(int)
count1 = 0
count2 = 0
rows = 0
with open("data") as f:
    line = f.readlines()

    for l in line:
        line_data = l.strip()
        # State machine. If the line has data, we're processing votes
        if len(line_data) >= 1:
            rows += 1 # how many users are in this group
            for character in line_data:
                seen[character] += 1
        else:
            count1 += len(seen.keys())
            for v in seen.values():
                if v == rows:
                    count2+=1
            # reset state for next group
            seen = defaultdict(int)
            rows = 0

print("Part 1: " + str(count1))
print("Part 2: " + str(count2))
