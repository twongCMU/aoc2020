from collections import defaultdict

import sys


player1=[10,39,16,32,5,46,47,45,48,26,36,27,24,37,49,25,30,13,23,1,9,3,31,14,4]
player2 = [2,15,29,41,11,21,8,44,38,19,12,20,40,17,22,35,34,42,50,6,33,7,18,28,43]

#player1=[9,2,6,3,1]
#player2=[5,8,4,7,10]

stack1 = []
stack2 = []

for i in player1:
    stack1.append(i)
for i in player2:
    stack2.append(i)


def play_game(stack1, stack2):
    """ play a full game, returning who won, 1 or 2
    """
    round_num = 1
    state = {}
    print("playing game with state " + str(stack1) + " " + str(stack2) + " round " + str(round_num))
    while len(stack1) and len(stack2):

        cur_state = str(stack1)+" "+str(stack2)
        if cur_state in state:
            return 1
        state[cur_state] = 1
        a1 = stack1.pop(0)
        a2 = stack2.pop(0)

        if a1<=len(stack1) and a2<=len(stack2):
            winner = play_game(stack1[:a1].copy(), stack2[:a2].copy())
        elif a1>a2:
            winner = 1
        else:
            winner = 2
            
        if winner == 1:
            stack1.append(a1)
            stack1.append(a2)
        else:
            stack2.append(a2)
            stack2.append(a1)    
        round_num+=1
    if len(stack1):
        return 1
    return 2
print(str(play_game(stack1, stack2)))

win = stack1
if not len(win):
    win = stack2
count = 1
final = 0
while len(win):
    a = win.pop()
    print("adding " + str(a) + " " + str(count))
    final += a*count
    count+=1
print(str(final))
