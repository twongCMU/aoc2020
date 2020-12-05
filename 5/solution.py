#!/usr/bin/python3

import math
import re

real_data = []
count = 0

def compute(v, low, high):
    bits = len(v) - 1
    for c in v:
        if c == 'F' or c == 'L':
            high -= math.pow(2, bits)
        else:
            low += math.pow(2, bits)
        print(str(bits) + " " + str(low) + " " +  str(high))
        bits -= 1
    return low

max_seat = 0
seats = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        row = compute(v[:7], 0, 127)
        col = compute(v[7:], 0, 7)
        seat_id = row*8+col
        if seat_id > max_seat:
            max_seat = int(seat_id)
        print("Seat " + str(row) + " " + str(col))
        seats.append(int(seat_id))
print("Part 1: " + str(max_seat))
print("Part 2: ")
for i in range(max_seat):
    if i+1 in seats and i-1 in seats and i not in seats:
        print((str(i)))

