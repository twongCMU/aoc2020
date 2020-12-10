#!/usr/bin/python3

adapters = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        adapters.append(int(v))
        
adapters.append(0) #wall outlet
# we don't have to care about the final device since it's always 3 away
# which means there is only 1 possible jump to it from any previous adapter
adapters.sort()

res = [0] * len(adapters)
res[0] = 1

# memoize like it's a job interview
for i in range(1, len(adapters)):
    count = 0

    # we can get to the current adapter from as many as the
    # 3 previous adapters so if those jumps are valid, sum
    # the number of ways to get to the previous ones
    if i-1 >= 0 and adapters[i-1]+3 >= adapters[i]:
        count += res[i-1]
    if i-2 >= 0 and adapters[i-2]+3 >= adapters[i]:
        count += res[i-2]
    if i-3 >= 0 and adapters[i-3]+3 >= adapters[i]:
        count += res[i-3]
    res[i] = count

print("Part 2: " + str(res[-1]))
