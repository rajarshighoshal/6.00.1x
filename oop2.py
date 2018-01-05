# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 13:38:05 2017

@author: RAJARSHI GHOSHAL
"""

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerNew = self.getNumer() * other.getDenom() + other.getNumer() * self.getDenom()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = self.getNumer() * other.getDenom() - other.getNumer() * self.getDenom()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew)
    def convert(self):
        return self.getNumer()/self.getDenom()
    