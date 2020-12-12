import numpy as np
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

data = []
with open("data") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) < 1:
            continue
        data.append(v)

# position of the ship
cur_x = 0
cur_y = 0

#position of waypoint
w_x = 10
w_y = 1

# move ship
def move(direction, distance, cur_x, cur_y):
    if direction == "N":
        cur_y += distance
    elif direction == "S":
        cur_y -= distance
    elif direction == "E":
        cur_x += distance
    elif direction == "W":
        cur_x -= distance

    return (cur_x, cur_y)

def move_waypoint(direction, distance, w_x, w_y):
    if direction == "N":
        w_y += distance
    elif direction == "S":
        w_y -= distance
    elif direction == "E":
        w_x += distance
    elif direction == "W":
        w_x -= distance

    return (w_x, w_y)

def ship_to_waypoint(cur_x, cur_y, w_x, w_y):
    y_dif = w_y - cur_y
    x_dif = w_x - cur_x
    return (x_dif, y_dif)
        
def rotate_waypoint_90_clockwise(cur_x, cur_y, dif_x, dif_y):
    w_x = cur_x + dif_y
    w_y = cur_y - dif_x

    return (w_x, w_y)

print("START ship " + str(cur_x) + "," + str(cur_y) + ", waypoint " + str(w_x) + "," + str(w_y))
for v in data:
    direction = v[0]
    distance = int(v[1:])

    if direction in ["N", "S", "E", "W"]:
        (w_x, w_y) = move_waypoint(direction, distance, w_x, w_y)
    elif direction in ["L", "R"]:
        (x_dif, y_dif) = ship_to_waypoint(cur_x, cur_y, w_x, w_y)    

        # convert all L rotates into R to simplify things
        if direction == "L" and distance == 90:
            distance = 270
        elif direction == "L" and distance == 270:
            distance = 90

        direction = "R"

        # rotate 90 at a time
        # be sure to update the ship_to_waypoint relative distances after each rotate
        while distance:
            (w_x, w_y) = rotate_waypoint_90_clockwise(cur_x, cur_y, x_dif, y_dif)
            (x_dif, y_dif) = ship_to_waypoint(cur_x, cur_y, w_x, w_y)    
            distance -= 90

    elif direction == "F":
        (x_dif, y_dif) = ship_to_waypoint(cur_x, cur_y, w_x, w_y)    
        (cur_x, cur_y) = move("E", x_dif*distance, cur_x, cur_y)
        (cur_x, cur_y) = move("N", y_dif*distance, cur_x, cur_y)

        w_x = cur_x + x_dif
        w_y = cur_y + y_dif

    print(" ship " + str(cur_x) + "," + str(cur_y) + ", waypoint " + str(w_x) + "," + str(w_y))
    
print(str(cur_x) + " " + str(cur_y) + " = " + str(abs(cur_x) + abs(cur_y)))

        
        
