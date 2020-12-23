#!/usr/bin/python3
import sys
data = [3,1,5,6,7,9,8,2,4]

#example
#data = [3,8,9,1,2,5,4,6,7]

list_max =1000000
#list_max = 10
total_rounds = 10000000
#total_rounds = 10

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def find_node(val, list_head):
    """
    This is dumb. I noticed that most insertions had a destination
    _behind_ the the current cup so instead of searching forward in a linked list
    this searches backwards in a doubly linked list. Run times went from impossible
    (like 3 moves per second) to doing the whole thing in 30 seconds
    """
    list_cur = list_head
    while list_cur.data != val:
        list_cur=list_cur.prev
    return list_cur

list_head = Node(data[0])
list_cur = list_head
for i in range(1,len(data)):
    new_node = Node(data[i])
    new_node.prev = list_cur
    list_cur.next = new_node
    list_cur = new_node



for i in range(10, list_max+1):
    new_node = Node(i)
    new_node.prev = list_cur
    list_cur.next = new_node
    list_cur = new_node

list_cur.next = list_head
list_head.prev = list_cur

node_one = find_node(1, list_head)

def print_list(list_head):
    temp_head = list_head
    while temp_head.next != list_head:
        sys.stdout.write(str(temp_head.data) + " " )
        temp_head = temp_head.next
    sys.stdout.write(str(temp_head.data) + " " )
    print("")
    
def move(list_head, round_id):
    
    removed1 = list_head.next
    removed2 = removed1.next
    removed3 = removed2.next
    removed = [removed1.data, removed2.data, removed3.data]
    
    current = list_head
    want = current.data

    #print("round " + str(round_id) + " pickup " + str(removed) + " want is " + str(want))
    selected = False

    # remove the 3 nodes
    list_head.next = removed3.next
    
    min_val = 1
    while not selected:
        want-=1
      
        if want < 1:
            want=list_max

        if want in removed:
            continue

        destination = want
        selected = True

    #print("dest " + str(destination))
    want_node = find_node(destination, list_head)

    # update data
    want_old_next = want_node.next
    want_node.next = removed1
    removed3.next = want_old_next

    # move new current
    list_head = list_head.next

    return list_head

for i in range(total_rounds):
    #print(str(i))
    list_head = move(list_head, i)
    #print(str(node_one.next.data) + " and "+ str(node_one.next.next.data))
    #print_list(list_head)
    
print(str(node_one.next.data) + " and "+ str(node_one.next.next.data))
print(str(node_one.next.data *node_one.next.next.data))
