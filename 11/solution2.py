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


def check_ray(chart, row, col, row_chg, col_chg, val):
    cur_row = row + row_chg
    cur_col = col + col_chg
    while 0 <= cur_row < num_row and 0 <= cur_col < num_col:
        # hit a floor, keep looking
        if chart[cur_row][cur_col] == ord('.'):
            cur_row = cur_row + row_chg
            cur_col = cur_col + col_chg
            continue
        # saw the val we want, return
        if chart[cur_row][cur_col] == val:
            return 1
        # hit something other than what we want or a floor
        return 0

    return 0

def count_neighbors(chart, row, col, val, round):
    count = 0
    count += check_ray(chart, row, col, -1, -1, val)
    count += check_ray(chart, row, col, -1, 0, val)
    count += check_ray(chart, row, col, -1, 1, val)
    count += check_ray(chart, row, col, 0, -1, val)
    count += check_ray(chart, row, col, 0, 1, val)
    count += check_ray(chart, row, col, 1, -1, val)
    count += check_ray(chart, row, col, 1, 0, val)
    count += check_ray(chart, row, col, 1, 1, val)
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
            if chart[row_index][col_index] == ord('#') and occupied_neighbors >= 5:
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
                
                
