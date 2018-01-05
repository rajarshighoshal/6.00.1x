# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:23:26 2017

@author: RAJARSHI GHOSHAL
"""

s = input("Enter a string: ")

sstring = []
finalss = []

for ch in s:
    sstring = sstring + [ch]
    if sstring == sorted(sstring) and len(sstring) > len(finalss):
        finalss = sstring
    elif sstring != sorted(sstring):
        sstring = [sstring[len(sstring) - 1]]

final = ''.join(finalss)
print(final)