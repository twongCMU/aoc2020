#!/usr/bin/python3

import math
import re
from collections import defaultdict

buses = [19,'x','x','x','x','x','x','x','x',41,'x','x','x',37,'x','x','x','x','x',821,'x','x','x','x','x','x','x','x','x','x','x','x',13,'x','x','x',17,'x','x','x','x','x','x','x','x','x','x','x',29,'x',463,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',23]

bus_d = { }
max_b = 0
max_i = 0
# convert bus list to a dict of bus_id -> cycle time
# also compute the max cycle time of all of the buses
for index, b in enumerate(buses):
    if b != 'x':
        bus_d[index] = b
        if b > max_b:
            max_b = b
            max_i = index
print(str(bus_d))


t_index = max_b - max_i
increment = max_b
num_bus = len(bus_d)

# any valid bus arrangement will repeat eventually. Track the longest repeating cycle we've seen
# and we know we can jump ahead in time by that much
# then we'll keep growing the cycle so we can jump more and more
cycle_ids = {}
cycle_length = 0
cycle_first = 0
while 1:
    seen = []
    # figure out which buses are properly aligned at this time
    for b, v in bus_d.items():
        if (t_index + b) % v == 0:
            seen.append(b)

    # if we saw all of the buses we're done
    if len(seen) == num_bus:
        print("done at " + str(t_index))
        exit()

    # see if all buses we've seen in the current cycle are accounted for in this time's list of aligned buses
    all_cycle_seen = True
    for id in cycle_ids.keys():
        if id not in seen:
            all_cycle_seen = False
            break

    # if we don't know the cycle length yet but we've seen this bus arrangement before, now we know the cycle length
    if all_cycle_seen and len(seen) == len(cycle_ids.keys()) and cycle_length == 0:
        cycle_length = t_index -  cycle_first
        increment = cycle_length
        print("increment now " + str(increment) + " from " + str(sorted(cycle_ids.keys())))
    # if we've seen more buses correct than before, update our tracking so we look for this new larger cycle
    elif all_cycle_seen and len(seen) > len(cycle_ids.keys()):
        print("Saw better arrangement " + str(sorted(seen)) + " len " + str(len(seen)) + " at time " + str(t_index))
        cycle_length = 0
        cycle_first = t_index
        cycle_ids = {}
        for p in seen:
            cycle_ids[p] = 0

    # jump forward in time by the increment
    t_index += increment
        
