# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:20:34 2017

@author: RAJARSHI GHOSHAL
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __len__(self):
        """Returns length of the intSet"""
        return len(self.vals)

    def intersect(self, other):
        """return a new intSet of integers that appear in both s1 and s2"""
        # create an empty set
        interSet = intSet()
        # checking for smaller set
        if len(self) <= len(other):
            # getting the common elements
            for e in self.vals:
                if e in other.vals:
                    interSet.insert(e)
        else:
            # getting the common elements
            for e in other.vals:
                if e in self.vals:
                    interSet.insert(e)
        #return
        return interSet
        
            
        