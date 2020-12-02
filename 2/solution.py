#!/usr/bin/python3

import math
import re

real_data = []
count = 0
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        m = re.search("(\d+)-(\d+) (.+): (.+)", v)
        min_c = int(m.group(1))
        max_c = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        hist = {}
        for l1 in password:
            if l1 not in hist:
                hist[l1] = 0
            hist[l1] += 1
        if letter not in hist:
            print("Invalid : " + v)
            continue
        if hist[letter] >= min_c and hist[letter] <= max_c:
            count+= 1
            print("Valid: " + v)
        else:
            print("Invalid : " + v)
print("Count is " + str(count))

