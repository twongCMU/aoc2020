#!/usr/bin/python3

import math
import re
from collections import defaultdict

rules = []
with open("data_rules") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        rules.append(v)


nearby = []
with open("data_nearby") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        nearby.append(v)

rules_dict = defaultdict(list)
for r in rules:
    (name, values) = r.split(": ")
    (v1, v2) = values.split(" or ")

    (v1_s, v1_e) = v1.split("-")
    (v2_s, v2_e) = v2.split("-")
    rules_dict[name].append((int(v1_s), int(v1_e)))
    rules_dict[name].append((int(v2_s), int(v2_e)))

count = 0
valid_count = 0
for n in nearby:
    ticket_is_valid = True
    vals = n.split(",")
    for v in vals:
        valid = False
        for rule in rules_dict.values():
            for one_rule in rule:
                (r_s, r_e) = one_rule
                if r_s <= int(v) <= r_e:
                    valid = True
                    break
        if not valid:
            ticket_is_valid = False
            count += int(v)
    if ticket_is_valid:
        valid_count += 1
print(str(count))
print("valid ticket count" + str(valid_count))
