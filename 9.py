a = 1

while a<999:
    b = 1
    while b<1000-a:
        c = 1000-b-a
        if a*a + b*b == c*c:
            print (a, b, c)
            break
            break
        else:
            b = b+1
    a = a+1
    
print ("done")
print (200*375*425)