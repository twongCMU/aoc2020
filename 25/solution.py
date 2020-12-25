#!/usr/bin/python3

from collections import defaultdict
import numpy as np


pub1 = 6270530
pub2 = 14540258

#examples
#pub1=5764801
#pub2=17807724

def transform(val, subj):
    val *= subj
    val %= 20201227
    return val

pub1_count = 0
val = 1
while 1:
    pub1_count+=1
    val = transform(val, 7)
    if val == pub1:
        break

pub2_count = 0
val = 1
while 1:
    pub2_count+=1
    val = transform(val, 7)
    if val == pub2:
        break

print("public key loops: " + str(pub1_count) + " " + str(pub2_count))

pub1_loop=pub1_count
pub2_loop=pub2_count

# these are the 2 values and I had them hard coded when I was working on this code
# to avoid the slow computation of the first part
#pub1_loop = 397860
#pub2_loop = 16774995

val = 1
for i in range(pub1_loop):
    val = transform(val, pub2)
print("secret " + str(val))

val = 1
for i in range(pub2_loop):
    val = transform(val, pub1)
print("secret " + str(val))


