# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:31:59 2015

@author: 이수민
"""

def div(n):
    i = 1
    d = 0
    while i*i <n:
        if n % i == 0:
            d = d+1
            i = i+1
        else:
            i = i+1
    if  i*i == n:
        d = 2*d+1
    else:
        d = 2*d
    return d
"""
k = 1
while k <10:
    n = k*(k+1)/2
    print (n)
    print (div(n))
    k = k+1
"""
n = 1
k = 1
while div(n) < 500:
    n = k*(k+1)/2
    k = k+1
    d = div(n)
    
print (n)

