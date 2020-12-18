#!/usr/bin/python3

import math
import re

data = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        data.append(v)

def eval_exp(exp):
    """Evaluate an expression with no parenthesis
    """

    # look for number + number and evaluate it until there are no more + left
    where_plus = exp.find("+")
    while where_plus != -1:
        regex = "([0-9]+) \+ ([0-9]+)"
        reg = re.search(regex, exp)
        val = int(reg.group(1)) + int(reg.group(2))
        exp = re.sub(regex, str(val), exp, 1)
        where_plus = exp.find("+")

    # look for number * number and evaluate it until there are no more * left
    where_mult = exp.find("*")
    while where_mult != -1:
        regex = "([0-9]+) \* ([0-9]+)"
        reg = re.search(regex, exp)
        val = int(reg.group(1)) * int(reg.group(2))
        exp = re.sub(regex, str(val), exp, 1)
        where_mult = exp.find("*")

    return int(exp)
        
    
def compute(index, expression):
    #print(expression)
    where_paren = expression.find("(")

    # keep looking for (<exp>), and evaluating <exp> until there are no more parens
    # then evaluate it one final time
    while where_paren != -1:
        regex = "(\([0-9 \+\*]+\))"
        reg = re.search(regex, expression)
        exp = reg.group(1)
        val = eval_exp(exp[1:-1]) # remove enclosing parenthesis
        #print("replacing " + str(exp) + " with  " + str(val))
    
        expression = re.sub(regex, str(val), expression, 1)
        
        where_paren = expression.find("(")
        #print(expression)

    
    return eval_exp(expression)
        
count = 0
for v in data:
    count += compute(0, v)
    print("count " + str(count))
