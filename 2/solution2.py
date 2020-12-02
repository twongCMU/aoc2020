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

        min_c -= 1
        max_c -= 1
        seen = 0
        if len(password) >= min_c and password[min_c] == letter:
            seen+=1
        if len(password) >= max_c and password[max_c] == letter:
            seen+=1
        print("Want '" + letter + "' at " + str(min_c) + "," + str(max_c) + ": "+password)
        print("Saw '" + password[min_c] + "' '" + password[max_c] + "'")
        if seen == 1:
            count+=1

print("Count is " + str(count))
