# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 16:01:51 2017

@author: RAJARSHI GHOSHAL
"""

class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once.
    """
    def __init__(self):
        '''Creats an empty set of integers'''
        self.vals = []
    def insert(self, e):
        '''Assume e is an integer and insert e into self'''
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        '''Assumes e is an integer.
        Returns True if e is in self, and False otherwise'''
        return e in self.vals
    def remove(self, e):
        '''Assume e is an integer and removes e from self
        Raises ValueError if e is not in self'''
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def __str__(self):
        '''Returns a string representation of self'''
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'