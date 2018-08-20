# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 22:25:09 2016

@author: 이수민
"""

py = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10]
, [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67]
, [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33]
, [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
, [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
, [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
, [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
, [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
, [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

max = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
path = []
maximum = [0]

#find maximum for each rows
for i in range(15):
    for j in range(i+1):
        value = py[i][j]
        if max[i] < value:
            max[i] = value
              
def recru(sum, i, j):
    print ("sum: ", sum, "max: ", maximum[0], "i: ", i, "j: ", j)
    psudo_sum = sum
    for k in range(i+2, 15):
        psudo_sum = psudo_sum + max[k]
    if psudo_sum < maximum[0]:
        print ("0")
        return
    if i == 14:
        print (i)
        print ("000")
        if sum > maximum[0]:
            maximum[0] = sum
            print (maximum[0])
        return
    else:
        a = py[i+1][j]
        b = py[i+1][j+1]
        recru(sum+a, i+1, j)
        recru(sum+b, i+1, j+1)
    
recru(0, 0, 0)