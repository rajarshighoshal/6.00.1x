# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 21:18:13 2017

@author: RAJARSHI GHOSHAL
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    
    flattenList = []
    
    for item in aList:
        if type(item) != list:
            flattenList.append(item)
        else:
            flattenList.extend(flatten(item))
    
    return flattenList
