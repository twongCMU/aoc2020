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

num_col = len(data[0])
num_row = len(data)

chart = np.zeros((num_row, num_col), np.uint8)

for row_index, row in enumerate(data):
    for col_index, v in enumerate(row):
        chart[row_index][col_index] = ord(v)

def print_chart(chart):
    for row_index, row in enumerate(chart):
        for col_index, v in enumerate(row):
            sys.stdout.write(chr(v))
        print("")
    print("---------------------")
def count_neighbors(chart, row, col, val, round):
    count = 0
    if row-1 >= 0 and col-1 >= 0 and chart[row-1][col-1] == val:
        count+=1
    if row-1 >= 0 and chart[row-1][col] == val:
        count+=1
    if row-1 >= 0 and col+1 < num_col and chart[row-1][col+1] == val:
        count+=1
        
    if col-1 >= 0 and chart[row][col-1] == val:
        count+=1
    if col+1 < num_col and chart[row][col+1] == val:
        count+=1
        
    if row+1 < num_row and col-1 >= 0 and chart[row+1][col-1] == val:
        count+=1
    if row+1 < num_row and col >= 0 and chart[row+1][col] == val:
        count+=1
    if row+1 < num_row and col+1 < num_col and chart[row+1][col+1] == val:
        count+=1

    return count

change_count = 1

round = 0
while change_count != 0:
    change_count = 0
    chart_new = chart.copy()
    for row_index, row in enumerate(chart):
        for col_index, v in enumerate(row):
            occupied_neighbors =  count_neighbors(chart, row_index, col_index, ord('#'), round) 
            if chart[row_index][col_index] == ord('L') and occupied_neighbors == 0:
                chart_new[row_index][col_index] = ord('#')
                change_count+=1
            if chart[row_index][col_index] == ord('#') and occupied_neighbors >= 4:
                chart_new[row_index][col_index] = ord('L')
                change_count+=1
    chart = chart_new

    round+=1
final_count = 0
for row_index, row in enumerate(chart):
    for col_index, v in enumerate(row):
        if v == ord('#'):
            final_count+=1

print(str(final_count))
                
                
