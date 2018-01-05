# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:58:10 2018

@author: RAJARSHI GHOSHAL
"""

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (high+low)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False #nothing left to search
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
            