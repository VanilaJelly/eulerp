prime = [2, 3, 5, 7, 11, 13]

k = 14
i = 0

while len(prime) < 10002:
    while i < len(prime):
        if k % prime[i] == 0:
            break
        else:
            i = i+1
    if i == len(prime):
        prime.append(k)
    i = 0
    k = k+1

p = prime[10000]