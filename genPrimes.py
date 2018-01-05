# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 18:43:19 2017

@author: RAJARSHI GHOSHAL
"""

def genPrimes():
    primeList = [2]
    yield primeList[0]
    guess = 3
    while True:
        if all(guess%x != 0 for x in primeList):
            primeList.append(guess)
        if guess == primeList[-1]:
            yield guess
        guess += 2
