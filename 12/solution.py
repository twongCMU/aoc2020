#!/usr/bin/python3

import math
import re
from collections import defaultdict
import numpy as np
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

data = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        data.append(v)
cur_x = 0
cur_y = 0
cur_o = 90

o_to_d = {0 : "N",
          90: "E",
          180: "S",
          270: "W"}
          
def move(direction, distance, cur_x, cur_y, cur_o):
    if direction == "N":
        cur_y += distance
    elif direction == "S":
        cur_y -= distance
    elif direction == "E":
        cur_x += distance
    elif direction == "W":
        cur_x -= distance
    elif direction == "L":
        cur_o -= distance
    elif direction == "R":
        cur_o += distance

    if cur_o < 0:
        cur_o = cur_o%360
    elif cur_o >= 360:
        cur_o = cur_o%360

    return (cur_x, cur_y, cur_o)

for v in data:
    direction = v[0]
    distance = int(v[1:])

    if direction != "F":
        (cur_x, cur_y, cur_o) = move(direction, distance, cur_x, cur_y, cur_o)
    elif direction == "F":
        (cur_x, cur_y, cur_o) = move(o_to_d[cur_o], distance, cur_x, cur_y, cur_o)

print(str(cur_x) + " " + str(cur_y) + " = " + str(abs(cur_x) + abs(cur_y)))

        
        

        
