hdl = open("C:/13.txt", 'r')
milist = hdl.readlines()
hdl.close()

l = len(milist)

i = 0
s = 0

while i < l :
    a = milist[i]
    b = int(a)
    s = s + b
    i= i+1
    
c = str(s)

ans = ""

i = 0
l2 = len(c)

while i < 10:
    a = c[i]
    ans = ans + a
    i= i+1

print (ans)