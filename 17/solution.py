#!/usr/bin/python3

import math
import re
from collections import defaultdict
import numpy as np
import sys
import itertools

np.set_printoptions(threshold=sys.maxsize)

size = 20
data = np.zeros((size,size,size),np.bool)

with open("data") as f:
    line = f.readlines()

    row = 0
    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        for index, c in enumerate(v):
            if c == '#':
                #print("setting " + str(row) + " " + str(index))
                data[row+6][index+6][6] = True

        row += 1

def count_active_neighbors(matrix, x,y,z):
    count = 0
    neighbors = itertools.product([-1,0,1], [-1,0,1], [-1,0,1])
    for (x_diff, y_diff,z_diff) in neighbors:

        if x_diff==0 and y_diff == 0 and z_diff == 0:
            continue

        if 0<(x+x_diff)<size and 0<(y+y_diff)<size and 0<(z+z_diff)<size:
            #print("checking2 " + str(x_diff+x) + " " + str(y_diff+y) + " " + str(z_diff+z))
            if matrix[x+x_diff][y+y_diff][z+z_diff] == 1:
                #print("saw soething")
                count+=1
    return count
        
for _ in range(6):
    data_temp = data.copy()

    for x in range(size):
        for y in range(size):
            for z in range(size):
                #print("XCALLING " + str(x) + " " + str(y) + " " + str(z))
                active = count_active_neighbors(data,x,y,z)
                if data[x][y][z]:
                    if active < 2 or active > 3:
                        data_temp[x][y][z] = False
                elif not data[x][y][z]:
                    if active == 3:
                        data_temp[x][y][z] = True
    data = data_temp


count = 0
for x in range(size):
    for y in range(size):
        for z in range(size):
            if data[x][y][z]:
                count+= 1
print(str(count))
