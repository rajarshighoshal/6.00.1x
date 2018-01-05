# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:33:01 2017

@author: RAJARSHI GHOSHAL
"""

def dict_invert(d):
    '''
    d: dict
    The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. 
    The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.
    Returns an inverted dictionary according to the instructions above
    '''
    dInvert = {}
    
    for k, v in d.items():
        dInvert[v] = dInvert.get(v, [])
        dInvert[v].append(k)
        dInvert[v] = sorted(dInvert[v])
    
    return dInvert