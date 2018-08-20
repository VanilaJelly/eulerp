i = 2
n = 600851475143 

factor = [1]

while i*i < 600851475143 :
    if n % i == 0 and n != 1:
        factor.append (i)
    else:
        pass
    i = i+1    
        
i = 0
l = len(factor) 
k = 1
prime_factor = []

while i < l :
    a = factor[i]
    while k < i:
        b = factor [k]
        if a % b == 0:
            break
        else:
            k = k+1
    if k == i:
        prime_factor.append(a)
    else:
        pass
    i = i+1
    k = 1
    
l = len(prime_factor) - 1

answer = prime_factor[l]