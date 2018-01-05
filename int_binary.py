# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:51:26 2017

@author: RAJARSHI GHOSHAL
"""

num = int(input('Enter a number: '))
n = num

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''

if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result
    num = num // 2

if isNeg:
    result = '-' + result

print('Binary of ' + str(n) +' is ' + result)