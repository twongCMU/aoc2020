#!/usr/bin/python3

import math
import re
from collections import defaultdict



rules = defaultdict(list)
with open("rules2") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        (rule_id, rest) = v.split(": ")
        (rule_list) = rest.split(" | ")
        for r in rule_list:
            new_list = []
            for n in r.split(" "):
                if n == "a" or n == "b":
                    new_list.append(n)
                else:
                    new_list.append(int(n))
                    
            rules[int(rule_id)].append(new_list)


messages=[]
with open("messages") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        messages.append(v)



            
queue = rules[0].copy()
dictionary = {}
while len(queue):
    head = queue.pop(0)

    substr = ""
    did_work = False
    for index, n in enumerate(head): # break into numbers within statement
        if n == "a" or n == "b":
            substr += n
            continue


        # if what we've computed so far isn't a substring of any message we're checking
        # then we can stop because any more decoding isn't going to give us any more info
        is_substr = False
        for m in messages:
            if m.startswith(substr):
                is_substr = True
                break
        if not is_substr:
            break

        did_work = True
        # n must be a number, replace it with the associated rule
        replace = rules[n]
        for r_entry in replace: # there could be multiple entries if the rule had |
            substitute = head[:index] + r_entry.copy() + head[index+1:]
            queue.append(substitute)
        break

    if not did_work:
        dictionary[substr] = 0

count = 0
for m in messages:
    if m in dictionary.keys():
        count += 1
print(str(count))

