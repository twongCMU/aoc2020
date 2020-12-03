#!/usr/bin/python3

data = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) > 1:
            data.append(v)

def do_count(right, down):
    col = 0
    row = 0
    tree_count = 0
    for data_row in data:
        if row % down > 0:
            row += 1
            continue
        if data_row[col] == '#':
            tree_count += 1
        col += right
        col = col % len(data_row)
        row += 1
    return tree_count

print("Part 1: " + str(do_count(3,1)))
res = []
res.append(do_count(1,1))
res.append(do_count(3,1))
res.append(do_count(5,1))
res.append(do_count(7,1))
res.append(do_count(1,2))
print("Part 2:" + str(res))
prod = 1
for v in res:
    prod *= v
print("product is " + str(prod))
