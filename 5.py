
correctanswer=16*9*5*7*11*13*17*19

def gcd(c, d):
    a = max(c, d)
    b = min(c, d)
    r = a%b
    while r>0:
        a = b
        b = r
        r = a%b
    return b
        
def lcm(a, b):
    g = gcd(a, b)
    l = (a*b) / g
    return (l)
    
m = 1
k = 1
while k <=20:
    m = lcm(m, k)
    k = k+1
    
answer = int(m)
    
print (answer)

if correctanswer == answer:
    print ("yeah")
else:
    print ("try again")