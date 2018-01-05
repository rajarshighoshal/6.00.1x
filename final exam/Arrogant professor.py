# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 20:40:11 2018

@author: RAJARSHI GHOSHAL
"""

# ae.say('the sky is blue')
# eric says: It is obvious that eric says: the sky is blue

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return Person.say(self, 'It is obvious that ' + Person.say(self, stuff))
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff
    