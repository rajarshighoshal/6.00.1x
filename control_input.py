# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:25:19 2017

@author: RAJARSHI GHOSHAL
"""

data = []
file_name = input("Provide a name of a file of data: ")

try:
    fh = open(file_name, 'r')
except IOError:
    print('Cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') #remove trailing \n
            data.append(addIt)
finally:
    fh.close() #close even if fail

gradesData = []

if data:
    for student in data:
        try:
            name = student[0:-1]
            grades = int(student[-1])
            gradesData.append([name, grades])
        except ValueError:
            gradesData.append([student[:], []])

