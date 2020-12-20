#!/usr/bin/python3

import math
import re
from collections import defaultdict
import sys


tile = {}
with open("data") as f:
    line = f.readlines()

    cur_tile = None
    tile_row = 0
    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        if v.startswith("Tile"):
            cur_tile = v[5:-1]
            tile[cur_tile] = {}
            tile[cur_tile]["t"] = ""
            tile[cur_tile]["l"] = ""
            tile[cur_tile]["b"] = ""
            tile[cur_tile]["r"] = ""
            tile_row = 0
            continue

        if tile_row == 0:
            tile[cur_tile]["t"] = v

        if tile_row == 9:
            tile[cur_tile]["b"] = v
            
        tile[cur_tile]["l"] += v[0]
        tile[cur_tile]["r"] += v[-1]
        tile_row+=1

edges = {}
for t in tile.keys():
    for s in ["t","l","b","r"]:
        if tile[t][s] in edges:
            del edges[tile[t][s]]
        else:
            edges[tile[t][s]] = t

        edge = tile[t][s][::-1]

        if edge in edges:
            del edges[edge]
        else:
            edges[edge] = t  

p = defaultdict(int)
for v in edges.values():
    p[v]+=1

print(str(p))


"""
result was
defaultdict(<class 'int'>, {'3191': 2, '1171': 2, '1759': 2, '3109': 2, '2063': 2, '1613': 2, '1723': 2, '1283': 4, '1979': 2, '2477': 2, '2633': 2, '1987': 2, '3533': 2, '1409': 2, '2579': 2, '1453': 2, '1583': 2, '1663': 2, '3877': 2, '2837': 2, '2081': 2, '1493': 2, '3793': 2, '1747': 2, '3299': 2, '2351': 2, '2027': 2, '1279': 2, '3889': 2, '2591': 2, '1619': 4, '1511': 4, '3727': 2, '2731': 2, '1901': 4, '1193': 2, '1109': 2, '3907': 2, '1627': 2, '2897': 2, '1447': 2, '1949': 2, '3797': 2, '1597': 2})

and I manually multiplied the four entries that had "4" as the value:

1283*1511*1619*1901
5966506063747
"""
