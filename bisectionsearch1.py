# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:24:41 2018

@author: RAJARSHI GHOSHAL
"""

def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)