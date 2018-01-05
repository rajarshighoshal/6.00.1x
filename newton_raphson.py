# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:30:01 2017

@author: RAJARSHI GHOSHAL
"""

epsilon = 0.01
y = 4554.0
guess = y/2.0
numGuesses = 0

while abs(guess**2 - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y) / (2*guess))
    
print('numGuesses: ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
