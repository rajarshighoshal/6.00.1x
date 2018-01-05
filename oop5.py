# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 19:52:07 2017

@author: RAJARSHI GHOSHAL
"""

import datetime

class Person(object):
    def __init__(self, name):
        """Create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        
    def getLastName(self):
        """Return self's last name"""
        return self.lastName
    
    def __str__(self):
        """Return self's name"""
        return self.name
    
    def setBirthDay(self, month, day, year):
        """Set self's birthday to birthDate"""
        self.birthDay = datetime.date(year,month,day)
    
    def getAge(self):
        """returns self's current age in days"""
        if self.birthDay == None:
            raise ValueError
        return (datetime.date.today() - self.birthDay).days
    
    def __lt__(self, other):
        """return True if self's name is lexicographically 
        less than other's name, False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
p1 = Person('Mark Zuckerberg')
p1.setBirthDay(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthDay(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthDay(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

personList = [p1, p2, p3, p4, p5]

    