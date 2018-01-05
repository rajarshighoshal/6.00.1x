# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 19:09:10 2017

@author: RAJARSHI GHOSHAL
"""
import random


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    def setAge(self, newage):
        self.age = newage
    def setName(self, newname = ""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+";"+str(self.age)
    
class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return "cat:"+str(self.name)+";"+str(self.age)

class Rabbit(Animal):
    def speak(self):
        print('meep')
    def __str__(self):
        return "Rabbit:"+str(self.name)+";"+str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.setName(self, name)
        self.friends = []
    def getFriends(self):
        return self.friends
    def addFriend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("Hello")
    def  ageDiff(self, other):
        diff = self.getAge() - other.getAge()
        if self.age > other.age:
            print(self.name, " is ", abs(diff), " years older than ", other.name)
        else:
            print(self.name, " is ", abs(diff), " years younger than ", other.name)
    def __str__(self):
        return "person:"+str(self.name)+";"+str(self.age)


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def changeMajor(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print('I have homework')
        elif 0.25 <= r < 0.5:
            print('I need sleep')
        elif 0.5 <= r < 0.75:
            print('I should eat')
        else:
            print('I am watching tv')
    def __str__(self):
        return "Student:"+str(self.name)+';'+str(self.age)+';'+str(self.major)

class Rabbit1(Animal):
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit1.tag
        Rabbit1.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return Rabbit1(0, self, other)
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    
    