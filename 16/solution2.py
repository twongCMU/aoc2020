#!/usr/bin/python3

import math
import re
from collections import defaultdict
my_ticket = [151,139,53,71,191,107,61,109,157,131,67,73,59,79,113,167,137,163,149,127]
#my_ticket = [11,12,13]
#print("XXXX WRONG TICKET")
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
rules_index = {}
rule_count = 0
rule_name_to_index = {}
for r in rules:
    (name, values) = r.split(": ")
    (v1, v2) = values.split(" or ")

    (v1_s, v1_e) = v1.split("-")
    (v2_s, v2_e) = v2.split("-")
    rules_dict[name].append((int(v1_s), int(v1_e)))
    rules_dict[name].append((int(v2_s), int(v2_e)))
    rules_index[rule_count] = name
    rule_name_to_index[name] = rule_count
    rule_count+=1



def is_any_rule_valid_for_value(value):
    """ True if value is ok for any rule
    """
    for rule in rules_dict.keys():
        if is_rule_name_valid_for_value(value, rule):
            return True
    return False

def is_rule_name_valid_for_value(value, rule_name):
    """ True if value is valid for specific rule
    """
    for one_rule in rules_dict[rule_name]:
        (r_s, r_e) = one_rule
        if r_s <= int(value) <= r_e:
            return True
    return False

# make a list of valid tickets
# That is, all values in ticket are valid for some rule
valid_tickets = []
for n in nearby:
    vals = n.split(",")
    is_valid = True
    for v in vals:
        if not is_any_rule_valid_for_value(v):
            is_valid = False
    if is_valid:
        valid_tickets.append(vals)


width = len(valid_tickets[0])

# generate column_to_rule which is a dict of column numbers to a list of rule_names that the column is valid for
column_to_rule = defaultdict(list)
for column in range(width):
    # look at all the rules
    for rule_name in rules_dict.keys():
        # for this rule, is every ticket in column valid?
        column_valid = True
        for v in valid_tickets:
            if not is_rule_name_valid_for_value(int(v[column]), rule_name):
                column_valid = False
                break
        if column_valid:
            column_to_rule[column].append(rule_name)


# walk each column_to_rule and any column that has only 1 rule must be matched
count = 1
column_count = len(column_to_rule)
while len(column_to_rule):

    for c in range(column_count):
        # if there is only one valid rule here, we know it must be matched
        if c in column_to_rule and len(column_to_rule[c])==1:
            rule_name = column_to_rule[c][0]
            if rule_name.startswith("departure"):
                count *= my_ticket[c]
            # remove column rule from all other columns
            for c2 in range(column_count):
                if c2 in column_to_rule and rule_name in column_to_rule[c2]:
                    column_to_rule[c2].remove(rule_name)
                if len(column_to_rule[c2]) == 0:
                    del column_to_rule[c2]
            break

print(str(count))
            
    
