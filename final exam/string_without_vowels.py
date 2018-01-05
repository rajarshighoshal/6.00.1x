# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 18:59:41 2018

@author: RAJARSHI GHOSHAL
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    s_without_vowels = ''
    VOWELS = 'aeiouAEIOU'
    for char in s:
        if char not in VOWELS:
            s_without_vowels += char
    print(s_without_vowels)