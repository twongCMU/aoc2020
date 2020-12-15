#!/usr/bin/python3

import math
import re
from collections import defaultdict

queue = [1,12,0,20,8,16]
#queue = [0,3,6]
spoken = {}
turn = 1

pending = None
for v in queue:
    if pending is not None:
        spoken[pending] = turn-1
        
    pending = v
    turn += 1
print("YYY "+str(spoken))
while 1:
    #print("turn " + str(turn) + " pending is " + str(pending))
    if pending not in spoken:
        spoken[pending] = turn - 1
        pending = 0
    else:
        temp_pending = turn - 1 - spoken[pending]
        spoken[pending] = turn - 1
        pending = temp_pending

    if turn == 2020:
        print(str(pending))
        break

    turn+=1

