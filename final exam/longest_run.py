# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:06:54 2018

@author: RAJARSHI GHOSHAL
"""
# A run of monotonically increasing numbers means that a number at position k+1 in 
# the sequence is greater than or equal to the number at position k in the sequence.

# A run of monotonically decreasing numbers means that a number at position k+1 in 
# the sequence is less than or equal to the number at position k in the sequence.

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    dec_count = 0
    inc_count = 0
    maxcount = 0
    result = 0

    for i in range(len(L) - 1):
        if (L[i] <= L[i + 1]):
            dec_count += 1
            if dec_count > maxcount:
                maxcount = dec_count
                result = i + 1
        else:
            dec_count = 0
        if (L[i] >= L[i + 1]):
            inc_count += 1            
            if inc_count > maxcount:
                maxcount = inc_count
                result = i + 1
        else:
            inc_count = 0
        
    startposition = result - maxcount
    return sum(L[startposition:result + 1])