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
    """Evaluate an expression with no parenthesis; go left to right and math it
    """
    prev_num = None
    prev_op = None
    exp_parts = exp.split(" ")
    for p in exp_parts:
        # first char must be a number
        if prev_num is None:
            prev_num = int(p)
            continue
        
        if p == "+" or p == "*":
            prev_op = p
            continue

        # must be a number
        temp_val = 0
        if prev_op == "+":
            #print("new val is " + str(prev_num) + " + " + p)
            temp_val = prev_num + int(p)
        else:
            # multiply
            #print("new val is " + str(prev_num) + " * " + p)
            temp_val = prev_num * int(p)
        prev_num = temp_val
    return prev_num
        
    
def compute(index, expression):
    #print(expression)
    where_paren = expression.find("(")
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

