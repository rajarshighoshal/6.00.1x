# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 10:55:17 2017

@author: RAJARSHI GHOSHAL
"""

def genSubSet(L):
    res = []
    if len(L) == 0:
        return [[]] # list of empty list
    smaller = genSubSet(L[:-1]) # all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small + extra) # for all smaller solutions, add one with last element
    return smaller+new   # combine those with last element and those without