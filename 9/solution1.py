#!/usr/bin/python3

# adapted from day 1
def search(sum, data):
    for z in data:
        if (sum - z) in data:
            return True

    return False

d = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) > 0:
            d.append(int(v))


index = 25
for i in range(index, len(d)):
    if not search(d[i], d[i-25:i]):
        print("Part 1: " + str(d[i]))
