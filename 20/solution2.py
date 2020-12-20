#!/usr/bin/python3

import math
import re
from collections import defaultdict
import sys
import numpy as np
import random
np.set_printoptions(threshold=sys.maxsize)
tile = {}
full_tile = {}

width = 12 # num tiles wide
tile_width=10

# read the file and generate a tile dict that maps to just the edges
# and a full_tile dict that has everything
with open("data") as f:
    line = f.readlines()

    cur_tile = None
    tile_row = 0
    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        if v.startswith("Tile"):
            cur_tile = int(v[5:-1])
            tile[cur_tile] = {}
            tile[cur_tile]["t"] = ""
            tile[cur_tile]["l"] = ""
            tile[cur_tile]["b"] = ""
            tile[cur_tile]["r"] = ""
            tile_row = 0
            full_tile[cur_tile] = np.zeros((tile_width,tile_width), np.bool)
            continue

        if tile_row == 0:
            tile[cur_tile]["t"] = v

        if tile_row == tile_width-1:
            tile[cur_tile]["b"] = v
            
        tile[cur_tile]["l"] += v[0]
        tile[cur_tile]["r"] += v[-1]

        print("xx " + v)
        for index, pixel in enumerate(v):
            full_tile[cur_tile][tile_row][index] = 0
            if pixel == '#':
                full_tile[cur_tile][tile_row][index] = 1
        tile_row+=1

# figure out what tiles border which other tiles. I think this gets the correct number and ID but
# is buggy about the direction and orientation
edges = {}
border = defaultdict(list)
for t in tile.keys():
    for s in ["t","l","b","r"]:
        if tile[t][s] in edges:
            border[t].append((edges[tile[t][s]], s, 0))
            border[edges[tile[t][s]]].append((t, s, 0))
            #del edges[tile[t][s]]
        else:
            edges[tile[t][s]] = t

        edge = tile[t][s][::-1]

        if edge in edges:
            border[t].append((edges[edge], s, 180))
            border[edges[edge]].append((t, s, 180))
            #del edges[edge]
#        else:
#            edges[edge] = t  

# print out how many borders each tile has. The ones with only 2 are the corners for part 1
# I manually did this part and entered the result in for part 2 below
print("Corners")
for b in border.keys():
    if len(border[b]) == 2:
        print(str(b) + " " + str(border[b]))

"""
corners are
1283 [('2063', 'b', 180), ('3889', 'r', 180)] I think: top/left 3889 is to the right
1511 [('2591', 'b', 0), ('1987', 'l', 0)]              top/right
1901 [('1747', 't', 0), ('1723', 'l', 0)]              bottom/right
1619 [('3299', 't', 180), ('1979', 't', 0)]             

"""
#print(str(tile[1283]))
#print(str(tile[2063]))
layout = np.zeros((12,12),np.uint32)

modifier = {}

def rotate_tile(old_tile, rotation):
    one_tile = {}
    
    if rotation == 0:
        one_tile["r"] = old_tile["r"]
        one_tile["b"] = old_tile["b"]
        one_tile["l"] = old_tile["l"]
        one_tile["t"] = old_tile["t"]
    elif rotation == 90: # if we rotate 90 the new right is what was the top etc
        one_tile["r"] = old_tile["t"]
        one_tile["b"] = old_tile["r"][::-1]
        one_tile["l"] = old_tile["b"]
        one_tile["t"] = old_tile["l"][::-1]
    elif rotation == 180:
        one_tile["r"] = old_tile["l"][::-1]
        one_tile["b"] = old_tile["t"][::-1]
        one_tile["l"] = old_tile["r"][::-1]
        one_tile["t"] = old_tile["b"][::-1]
    elif rotation == 270:
        one_tile["r"] = old_tile["b"][::-1]
        one_tile["b"] = old_tile["l"]
        one_tile["l"] = old_tile["t"][::-1]
        one_tile["t"] = old_tile["r"]

    return one_tile

def flip_tile(old_tile, flip):
    one_tile = {}
    if flip == "v":
        one_tile["r"] = old_tile["r"][::-1]
        one_tile["b"] = old_tile["t"]
        one_tile["l"] = old_tile["l"][::-1]
        one_tile["t"] = old_tile["b"]
    elif flip == "h":
        one_tile["r"] = old_tile["l"]
        one_tile["b"] = old_tile["b"][::-1]
        one_tile["l"] = old_tile["r"]
        one_tile["t"] = old_tile["t"][::-1]
    elif flip == "hv":
        one_tile["r"] = old_tile["l"][::-1]
        one_tile["b"] = old_tile["t"][::-1]
        one_tile["l"] = old_tile["r"][::-1]
        one_tile["t"] = old_tile["b"][::-1]
    else:
        one_tile["r"] = old_tile["r"]
        one_tile["b"] = old_tile["b"]
        one_tile["l"] = old_tile["l"]
        one_tile["t"] = old_tile["t"]
        
    return one_tile

def get_left_tile_right_edge(i, j, layout, modifier):
    if j<0:
        return ""

    id = layout[i][j]
    (rot,flip) = modifier[id]
    old_tile = rotate_tile(tile[id], rot)
    one_tile = flip_tile(old_tile, flip)
    return one_tile["r"]
    
def get_top_tile_bottom_edge(i, j, layout, modifier):
    if i<0:
        return ""
    
    id = layout[i][j]
    (rot,flip) = modifier[id]
    old_tile = rotate_tile(tile[id], rot)
    one_tile = flip_tile(old_tile, flip)
    return one_tile["b"]

def fit_tile(i,j,layout,modifier,l,t, tile_list):
    """ Given a left and top edge constraint, try every tile and rotate it and flip it to try to get it to fit
    """
    changed = None
    keys_list = list(tile_list.keys())
    random.shuffle(keys_list)
    for tile_id in keys_list:
        for rot in [0,90,180,270]:
            for flip in [None, "h","v"]:
                old_tile = rotate_tile(tile[tile_id], rot)
                one_tile = flip_tile(old_tile, flip)
                #print("tile " + str(tile_id) + " rot " + str(rot) + " flip " + str(flip) + " left " + one_tile["l"] + " top " + str(one_tile["t"]))
                if (len(l)==0 or l == one_tile["l"]) and (len(t)==0 or t == one_tile["t"]):
                    modifier[tile_id]=(rot, flip)
                    layout[i][j] = tile_id
                    return tile_id

# manually place the corner tile determined above
layout[0][0] = 1283
modifier[1283] = (0, None)
#layout[0][0] = 1951
#modifier[1951] = (0, "v")


tile_list = {}
for t in tile.keys():
    tile_list[t] = 0

print("XXX" + str(sorted(tile_list.keys())))
del tile_list[layout[0][0]]

# lay tiles left to right, top to bottom. Each tile therefore depends on the edge to the left and top
for i in range(width):
    for j in range(width):
        if i==0 and j==0: 
            continue
        print("Matching " + str(i) + " " + str(j))
        l = get_left_tile_right_edge(i, j-1, layout, modifier)
        t = get_top_tile_bottom_edge(i-1, j, layout, modifier)
        print("desired left is " + l)
        if l != "":
            print("from " + str(layout[i][j-1]))
        print("desired top is " + t)
        if t != "":
            print("from " + str(layout[i-1][j]))
        tile_id = fit_tile(i,j,layout,modifier,l,t, tile_list)
        print("matched to tile " + str(tile_id))
        print("rotation " + str(modifier[tile_id]))
        del tile_list[tile_id]
        
#print(str(layout))
final = np.zeros((width*(tile_width-2),width*(tile_width-2)),np.bool)

# now we know where each tile goes, recreate the full image
for i in range(width):
    for j in range(width):
        x_start = 1
        y_start = 1

        x_end = tile_width-2
        y_end = tile_width-2

        final_i = i*(tile_width-2)
        final_j = j*(tile_width-2)

        cur_tile = layout[i][j]

       
        
        (rot,flip) = modifier[layout[i][j]]
        print(str( modifier[layout[i][j]]) + " " + str(int(rot/90)))
        full_tile[cur_tile] = np.rot90(full_tile[cur_tile], int(rot/90), (1,0))

        if flip == "v":
            full_tile[cur_tile] = np.flipud(full_tile[cur_tile])
        elif flip == "h":
            full_tile[cur_tile] = np.fliplr(full_tile[cur_tile])

        (x_size,y_size) = full_tile[cur_tile].shape
        for i_temp in range(x_size):
            print("")
            for j_temp in range(y_size):
                if full_tile[cur_tile][i_temp][j_temp]:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")
        print("")

        i_add = 0
        j_add = 0
        for x in range(x_start, x_end+1):
            j_add=0
            for y in range(y_start, y_end+1):
                final[final_i+i_add][final_j+j_add] = full_tile[cur_tile][x][y]
                j_add+=1
            i_add+=1

            

monster = []
monster.append((0,18))
monster.append((1,0))
monster.append((1,5))
monster.append((1,6))
monster.append((1,11))
monster.append((1,12))
monster.append((1,17))
monster.append((1,18))
monster.append((1,19))
monster.append((2,1))
monster.append((2,4))
monster.append((2,7))
monster.append((2,10))
monster.append((2,13))
monster.append((2,16))

print("")
print("Shape" + str(final.shape))
(x_size,y_size) = final.shape
pound_count = 0
blank_count = 0
for i in range(x_size):
    for j in range(y_size):
        if final[i][j]:
            pound_count += 1
        else:
            blank_count +=1
print("# : " +str(pound_count))
print(". : " +str(blank_count))
print("monster: " + str(len(monster)))
print("------------")

# rotate and flip the image in every configuration and search for the monster
for rot in range(3):
    temp_final = np.copy(final)
    temp_final = np.rot90(temp_final,rot,(1,0))
    for flip in ["h", "v", None]:
        #print("rot " + str(rot) + " flip " + str(flip))
        if flip == "v":
            temp_final = np.flipud(temp_final)
        elif flip == "h":
            temp_final = np.fliplr(temp_final)
        
        (x_size,y_size) = temp_final.shape
        """
        for i in range(x_size):
            print("")
            for j in range(y_size):
                if temp_final[i][j]:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")
        print("")
        """
        monster_count = 0

        for i in range(x_size-3):
            for j in range(y_size-20):
                is_m = True
                for (pixel_x, pixel_y) in monster:
                    if not temp_final[i+pixel_x][j+pixel_y]:
                        is_m = False
                        break
                if is_m:
                    monster_count += 1
                    print("found at " + (str(i)) + "," + str(j))
        if monster_count:
            print("Monsters: " + str(monster_count))
            print("total: " + str(pound_count-(monster_count*len(monster))))

