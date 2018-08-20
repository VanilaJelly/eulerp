k = 1

for i in range(100, 1000):
    for j in range(100, 1000):
        s = str(i*j)
        a = list(s)
        b = list(s)
        b.reverse()
        if a == b and k < i*j:
            k = i*j
        
print (k)