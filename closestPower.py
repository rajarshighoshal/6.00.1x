# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:53:39 2017

@author: RAJARSHI GHOSHAL
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
 
    if base == num:
        exponent = 1
    elif base > num:
        exponent = 0
    else:
        for i in range(1, int(num)):
            if abs(base**i - num) <= abs(base**(i+1) -num):
                exponent = i
                break
    
    return exponent
