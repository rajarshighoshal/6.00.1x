# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:37:28 2017

@author: RAJARSHI GHOSHAL
"""

from oop5 import *

class MITPerson(Person):
    nextIdNum = 0 # next id number to assign
    
    def __init__(self, name):
        Person.__init__(self, name) # initiate person attributes
        self.IdNum = MITPerson.nextIdNum # mitperson attribute's unique ID
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.IdNum
    
    # sorting MIT people using their IdNum, not name!
    def __lt__(self, other):
        return self.IdNum < other.IdNum
    
    def speak(self, utterance):
        return (self.getLastName() + ' says: ' + utterance)
    
    
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)



class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
    
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)
    
    def lecture(self, topic):
        return self.speak('It is obvious that ' + topic)
    
