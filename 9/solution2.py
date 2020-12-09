#!/usr/bin/python3

# answer from part 1
key = 2089807806

d = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) > 0:
            d.append(int(v))


for i in range(0, len(d)):
    acc = 0
    count = 0
    vals = []
    for j in range(i, len(d)):
        count += 1
        acc += d[j]
        vals.append(d[j])
        if count < 2:
            continue
        if acc == key:
            print("Part 2: " + str(min(vals)+max(vals)))
            break
        elif acc > key:
            break
