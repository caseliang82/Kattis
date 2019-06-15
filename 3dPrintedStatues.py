n = int(input())

def findDay(d, p, n):
    if (p >= n): 
        return d
    else:
        return findDay(d+1, p*2, n)

print(findDay(1, 1, n))