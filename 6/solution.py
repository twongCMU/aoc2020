#!/usr/bin/python3

import math
import re

d = {}
count1 = 0
count2 = 0
rows = 0
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) >= 1:
            rows += 1
            for c in v:
                print("char " + str(c))
                if c not in d:
                    d[c] = 0
                d[c] += 1
        else:
            count1 += len(d.keys())
            for p in d.keys():
                if d[p] == rows:
                    count2+=1
            d = {}
            rows = 0






print("Part 1: " + str(count1))
print("Part 2: " + str(count2))
