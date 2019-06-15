from sys import stdin

t = []

for line in stdin:
    t = t + line.split()

t = [int(c) for c in t]

# left
if t[16] == 0:
    for k in range(0,4):
        for i in range(0,4):
            for j in range(i+1,4):
                # print('i:',i,'j',j)
                if t[i+k*4] == 0 and t[j+k*4] == 0:
                    continue
                elif t[i+k*4] == t[j+k*4]:
                    t[i+k*4] *= 2
                    t[j+k*4] = 0
                    break
                elif t[i+k*4] == 0 and t[j+k*4] != 0:
                    t[i+k*4] = t[j+k*4]
                    t[j+k*4] = 0
                elif t[i+k*4] != t[j+k*4] and t[j+k*4] != 0:
                    break

# right
elif t[16] == 2:
    for k in range(0,4):
        for i in range(3,-1,-1):
            for j in range(i-1,-1,-1):
                # print('i:',i,' j:',j)
                if t[i+k*4] == 0 and t[j+k*4] == 0:
                    continue
                elif t[i+k*4] == t[j+k*4]:
                    t[i+k*4] *= 2
                    t[j+k*4] = 0
                    break
                elif t[i+k*4] == 0 and t[j+k*4] != 0:
                    t[i+k*4] = t[j+k*4]
                    t[j+k*4] = 0
                elif t[i+k*4] != t[j+k*4] and t[j+k*4] != 0:
                    break
# up
elif t[16] == 1:
    for k in range(0,4):
        for i in range(0,4):
            for j in range(i+1,4):
                # print('i:',i,'j',j)
                if t[i*4+k] == 0 and t[j*4+k] == 0:
                    continue
                elif t[i*4+k] == t[j*4+k]:
                    t[i*4+k] *= 2
                    t[j*4+k] = 0
                    break
                elif t[i*4+k] == 0 and t[j*4+k] != 0:
                    t[i*4+k] = t[j*4+k]
                    t[j*4+k] = 0
                elif t[i*4+k] != t[j*4+k] and t[j*4+k] != 0:
                    break
# down
elif t[16] == 3:
    for k in range(0,4):
        for i in range(3,-1,-1):
            for j in range(i-1,-1,-1):
                # print('i:',i,'j',j)
                if t[i*4+k] == 0 and t[j*4+k] == 0:
                    continue
                elif t[i*4+k] == t[j*4+k]:
                    t[i*4+k] *= 2
                    t[j*4+k] = 0
                    break
                elif t[i*4+k] == 0 and t[j*4+k] != 0:
                    t[i*4+k] = t[j*4+k]
                    t[j*4+k] = 0
                elif t[i*4+k] != t[j*4+k] and t[j*4+k] != 0:
                    break



for i in range(0,4):
    for j in range(0,4):
        print(t[i*4+j], ' ', end='')
    print('')


