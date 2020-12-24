#!/usr/bin/python3

from collections import defaultdict
import numpy as np

        
data = []
grid_size = 300 # this is lazy and slow but it works well enough
rounds = 100
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

grid = np.zeros((grid_size,grid_size), np.bool)


def count_neighbors(grid, x,y):
    neighbor_list = [(2,0),(-2,0),(-1,1),(1,1),(-1,-1),(1,-1)]
    count0 = 0
    count1 = 0
    for n in neighbor_list:
        (mod_x,mod_y) = n
        if grid[x+mod_x, y+mod_y]:
            count1+=1
        else:
            count0+=1
    #print(str(x) + " " + str(y) + " " + str(count1))
    return (count0,count1)

for d in data:
    cur_x = int(grid_size/2)
    cur_y = int(grid_size/2)

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


for r in range(rounds):
    new_grid = np.copy(grid)
    for i in range(0,grid_size-2):
        for j in range(grid_size-2):
            (c0,c1) = count_neighbors(grid,i,j)
            if grid[i][j] and (c1 == 0 or c1>2):
                #print("flip to white")
                new_grid[i][j]=0
            elif not grid[i][j] and c1 == 2:
                #print("flip to black")
                new_grid[i][j]=1
    grid = new_grid
    
    count = 0
    for i in range(grid_size):
        for j in range(grid_size):
            count += grid[i][j]
    print(str(count))
    
            
