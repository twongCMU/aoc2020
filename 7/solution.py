#!/usr/bin/python3

import math
import re
from collections import defaultdict
bags = defaultdict(dict)
count = 0
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        v = v[:-1] # every line has a trailing period.
        
        (from_bag, to_bags) = v.split(" bags contain ")
        
        assert from_bag not in bags
        
        if to_bags == "no other bags":
            continue
        
        if "," not in to_bags:
            (num, adj, color, bag) = to_bags.split(" ")
            bags[from_bag][adj + " " + color] = int(num)
        else:
            bags_list = to_bags.split(", ")
            for b in bags_list:
                (num, adj, color, bag) = b.split(" ")
                bags[from_bag][adj + " " + color] = int(num)


my_queue = ["shiny gold"]
seen = {}
while len(my_queue):
    element = my_queue.pop(0)
    for k, v in bags.items(): # see what can enclose us
        if element in v:
            if k not in seen:
                seen[k] = 0
                my_queue.append(k) # put enclosing bag into queue
                count += 1
                
print("Part 1: " + str(count))

my_queue = [("shiny gold", 1)]
count = -1 #double counting the initial gold bag
while len(my_queue):
    (bag_type, bag_number) = my_queue.pop(0)
    if bag_type in bags: 
        count+=bag_number # count the bag(s) itself 
        #consider all bags inside this one
        for k, v in bags[bag_type].items():
            # the number of child bags is the number inside one times multiplied by the number of parent bags we have
            my_queue.append((k, v*bag_number))            
    else:
        # if the bag isn't in the bag list we've reached the bottom of the tree
        # so just count the number of this bag that we have
        count += bag_number
                
print("Part 2: " + str(count))
