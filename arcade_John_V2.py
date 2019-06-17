import math

h = int(input().split()[0])
n = int(h * (h + 1) / 2)

node = [ 0 for i in range((h+2)*(h+2) ) ]

count = 0
buffer = [ int(x) for x in input().split() ]
for a in range(1, h+1):
    for b in range(1, a+1):
        loc = a * (h + 2) + b
        node[loc] = buffer[count]
        count += 1

transMat = [ [] for y in range( (h+2)*(h+2) ) ] 
currentRow, holeIdx = 1, 0    

for a in range(1, h+1):
    for b in range(1, a+1):
        loc = a * (h + 2) + b
        probs = [float(x) for x in input().split()]
        transMat[loc].append( (loc - (h + 2) - 1      , probs[0]) )
        transMat[loc].append( (loc - (h + 2)          , probs[1]) )
        transMat[loc].append( (loc + (h + 2)          , probs[2]) )
        transMat[loc].append( (loc + (h + 2) + 1      , probs[3]) )
        transMat[loc].append( (loc + (h + 2) * (h + 2), probs[4]) )

Vpi = [0 for i in range( (h+2)*(h+2) )]
Vpi[1 + h + 2] = 1.0

Vlen = len(Vpi)
Mlen = len(transMat)

P_BallNotInHole = 1
ans = 0.0

while P_BallNotInHole > 1e-6:
    Vtemp = [0 for i in range( (h+2)*(h+2) )]
    for row in range(Vlen):
        for (idx, val) in transMat[row]:
            if idx >= Vlen: # stop
                # print("idx:",idx, idx-Vlen)
                ans += node[idx-Vlen]*Vpi[row]*val
                P_BallNotInHole -= Vpi[row]*val
            else:
                Vtemp[idx] += val * Vpi[row]

    Vpi = Vtemp[:]


print(ans)

