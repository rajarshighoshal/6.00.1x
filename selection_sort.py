# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 09:49:06 2018

@author: RAJARSHI GHOSHAL
"""

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
