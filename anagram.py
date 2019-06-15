from sys import stdin

fact = {0: 1}

for i in range(1, 101):
    fact[i] = i * fact[i - 1]

for line in stdin:
    word = str(line.split()[0])
    occur = {}

    for w in word:
        if ord(w) in occur:
            occur[ord(w)] += 1
        else:
            occur[ord(w)] = 1
    
    total = fact[len(word)]

    for k, o in occur.items():
        total //= fact[o]

    print(total)

  