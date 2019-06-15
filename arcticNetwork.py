import math

def dis(a,b):
    dx = (a[0] - b[0])**2
    dy = (a[1] - b[1])**2
    return math.sqrt(dx + dy)

def listMax(a):
    if len(a) > 0:
        temp = a[0]
        for i in a:
            if i > temp:
                temp = i
        return temp
    else:
        return 0


n = int(input().split()[0])
while (n > 0):
    n -= 1
    buffer = input().split()
    s = int(buffer[0])
    p = int(buffer[1])

    if s >= p - 1:
        print('0.00')
    else:
        temp = p
        pos = []
        while (temp > 0):
            buffer = input().split()
            pos.append((int(buffer[0]), int(buffer[1])))
            temp -= 1

        distances = []
        for x in pos:
            temp = []
            for y in pos:
                if x != y:
                    temp.append(dis(x,y))
            temp.sort()
            distances.append(listMax(temp[:p-s-1]))

        # print(distances)
        print("%.2f" % (listMax(distances)))
