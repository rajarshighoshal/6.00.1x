# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:31:43 2017

@author: RAJARSHI GHOSHAL
"""

from oop6 import *

class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Creates an empty grade book"""
        self.students = [] # list of Student objects
        self.grades = {} # maps IdNum -> list of grades
        self.isSorted = True # true if self.students is sorted
        
    def addStudent(self, student):
        """Assume: student is of type Student
        add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    
    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def getGrades(self, student):
        """Return a list of grades for student"""
        try:   # return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def allStudents(self):
        """Return a list of students in the grade book"""
        if not self.isSorted:
            self.students.sort
            self.isSorted = True
        # return self.students[:]  # return copy of list of students
        for s in self.students:
            yield s

    
def gradeReport(course):
    """Assumes: course is of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    
    return '\n'.join(report)
    
    