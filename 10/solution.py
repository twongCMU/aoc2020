#!/usr/bin/python3

adapters = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        adapters.append(int(v))

# wall outlet
adapters.append(0)
adapters.sort()
# device
device_jolts = adapters[-1]+3
adapters.append(device_jolts)

# jolts are 1-3 so we'll just put 4 items here and ignore the 0th index
dist = [0] *4 

# -1 so we don't run off the end since we're looking 1 ahead
for index in range(len(adapters) - 1):
    diff = adapters[index+1] - adapters[index]
    dist[diff] += 1
    
print("Part 1: " + str(dist[1] * dist[3]))
