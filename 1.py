# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:28:32 2016

@author: 이수민
"""

s = 0
k = 0
while k<334:
    s = s + k * 3
    k = k+1
    
k = 0
while k < 200:
    if k %3 ==0:
        k = k+1
    else:
        s = s + k * 5
        k = k+1
        
print (s)
