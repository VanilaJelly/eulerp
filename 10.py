prime = [2, 3, 5, 7, 11, 13]

k = 14
i = 0

while k < 2000000:
    while prime[i] < k**0.5 + 1:
            if k % prime[i] == 0:
                break
            else:
                i = i+1
    if prime[i] > k**0.5 + 1:
        prime.append(k)
    i = 0
    k = k+1
    
    

s = 0
    
for i in prime:
    s = s+i
    
print (s)