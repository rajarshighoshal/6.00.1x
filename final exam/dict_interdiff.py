# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:17:13 2018

@author: RAJARSHI GHOSHAL
"""

def f(a,b):
    return a>b



def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inter_dict = {}
    diff_dict = {}
    for key in d1.keys():
        if key in d2.keys():
            inter_dict[key] = f(d1[key], d2[key])
            del d2[key]
        else:
            diff_dict[key] = d1[key]
    for key in d2.keys():
        diff_dict[key] = d2[key]
    
    return (inter_dict, diff_dict)