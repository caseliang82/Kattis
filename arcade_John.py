import math
# import numpy as np


h = int(input().split()[0])
n = int(h * (h + 1) / 2)
node = [0]
prob = []


# initialise numbers of the starting positions of the triangle

# load valus for nodes:
buffer = input().split()

for i in range(0, n):
    node.append(int(buffer[i]))
    temp = input().split()
    p = []
    for t in temp:
        p.append(float(t))
    prob.append(p)

start = [1, 2]
for i in range(2, h + 1):
    start.append(start[i - 1] + i)

def getH(n):
    for i in range(1, len(start)):
        if n < start[i]:
            return i

def direction(n, d): # input the number of the node, direction to ge 
    tempH = getH(n)
    # return -1 if there is invalid direction
    if d == 1: # left-up
        if n in start:
            return -1
        else:
            return start[tempH-1-1] + n - start[tempH - 1] - 1
    elif d == 2: # right-up
        if n + 1 in start:
            return -1
        else:
            return start[tempH-1-1] + n - start[tempH - 1]
    elif d == 3: # left-bottom
        if tempH == h: # at bottom row
            return -1
        else:
            return start[tempH] + n - start[tempH-1]
    elif d == 4: # bottom right
        if tempH == h:
            return -1
        else:
            return start[tempH] + n - start[tempH-1] + 1
    elif d == 5: # return itself
        return n

# transition model:
Mtran = [[0 for x in range(n)] for y in range(n)] 
for i in range(len(prob)):
    for j in range(5):
        if prob[i][j] != 0:
            tempPos = direction(i+1, j+1) - 1 # so it starts from 0
            if tempPos != -1:
                Mtran[i][tempPos] = prob[i][j]

Vpi = [0 for i in range(n)]
Vpi[0] = 1


P_BallNotInHole = 1
ans = 0.0
while P_BallNotInHole > 1e-6:
    
    Vtemp = [0 for i in range(n)]
    for row in range(n):
        for col in range(n):
            if row == col: # stop
                ans += node[row+1]*Vpi[col]*Mtran[col][row]
                P_BallNotInHole -= Vpi[col]*Mtran[col][row]
            else:
                Vtemp[row] += Mtran[col][row] * Vpi[col]

    Vpi = Vtemp[:]


print(ans)
