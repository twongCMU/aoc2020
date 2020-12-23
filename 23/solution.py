#!/usr/bin/python3


data = [3,1,5,6,7,9,8,2,4]

#example
#data = [3,8,9,1,2,5,4,6,7]

def move(data, round_id):
    removed = data[1:4]
    new_data = [data[0]] + data[4:].copy()
    current = data[0]
    want = current

    print("round " + str(round_id) + " pickup " + str(removed) + " want is " + str(want))
    selected = False
    while not selected:
        want-=1
      
        if want < min(data):
            print("max want")
            want=max(data)

        if want in removed:
            print("want was removed trying again")
            continue

        destination = want
        selected = True

    print("dest " + str(destination))
    index = new_data.index(destination)
    data = new_data[:index+1] + removed + new_data[index+1:]

    # move new current
    data = data[1:] + [data[0]]
    return data

for i in range(100):
    data = move(data, i)
print(str(data))
