a= 1
b = 1
c = 2
s = 0

while b<4000000:
    a = b    
    b = c
    c = a+b
    if a%2 ==0:
        s = s+a
    else:
        pass


print (s)