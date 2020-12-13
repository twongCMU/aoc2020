#!/usr/bin/python3

import math
import re
from collections import defaultdict

buses = [19,'x','x','x','x','x','x','x','x',41,'x','x','x',37,'x','x','x','x','x',821,'x','x','x','x','x','x','x','x','x','x','x','x',13,'x','x','x',17,'x','x','x','x','x','x','x','x','x','x','x',29,'x',463,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',23]
earliest = 1001612

bus_d = {}
for b in buses:
    if b != 'x':
        val = b
        mult = 1
        while val < earliest:
            val = mult * b
            mult += 1
        bus_d[b] = val % earliest
        
for k, v in bus_d.items():
    if v == min(bus_d.values()):
        print("bus " + str(k) + " wait " + str(v))
    
