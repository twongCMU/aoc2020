#!/usr/bin/python3

from collections import defaultdict
import numpy as np

        
data = []
grid_size = 100
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

grid = np.zeros((grid_size,grid_size), np.bool)


for d in data:
    cur_x = 50
    cur_y = 50

    while len(d):
        consumed = 0
        if d.startswith("e"):
            cur_x+=2
            consumed = 1
        elif d.startswith("w"):
            cur_x-=2
            consumed = 1
        elif d.startswith("nw"):
            cur_x-=1
            cur_y+=1
            consumed = 2
        elif d.startswith("ne"):
            cur_x+=1
            cur_y+=1
            consumed = 2
        elif d.startswith("sw"):
            cur_x-=1
            cur_y-=1
            consumed = 2
        elif d.startswith("se"):
            cur_x+=1
            cur_y-=1
            consumed = 2
        d = d[consumed:]
    grid[cur_x][cur_y] = not grid[cur_x][cur_y]

count = 0
for i in range(grid_size):
    for j in range(grid_size):
        count += grid[i][j]
print(str(count))
    
            
