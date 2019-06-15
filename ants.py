cases = int(input().split()[0])

while (cases > 0):
    cases -= 1
    buffer = input().split()

    pole = int(buffer[0])
    Nant = int(buffer[1])
    ant = []

    count = 0
    while count < Nant:
        buffer = input().split()
        count += len(buffer)

        for b in buffer:
            ant.append(int(b))

    fastest = []
    slowest = []
    for a in ant:
        d1 = abs(a-pole)
        fastest.append(d1 if d1 < a else a)
        slowest.append(d1 if d1 > a else a)

    fastest.sort()
    slowest.sort()
    print(fastest[len(fastest) - 1], slowest[len(slowest) - 1])
