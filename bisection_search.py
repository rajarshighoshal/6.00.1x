# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:43:46 2017

@author: RAJARSHI GHOSHAL
"""

x = 54

epsilon = 0.01
numGuesses = 0
low = 0.0
high = x

ans = (low + high)/2.0

while abs(ans**3 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    
    if ans**3 < x:
        low = ans
    else:
        high = ans
    
    ans = (high + low)/2.0
    
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))