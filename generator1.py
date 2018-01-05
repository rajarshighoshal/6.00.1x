# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 18:09:35 2017

@author: RAJARSHI GHOSHAL
"""

def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next