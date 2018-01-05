# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:41:33 2017

@author: RAJARSHI GHOSHAL
"""

def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

test_grades = [[['Peter', 'Parker'], [10.0, 5.0, 85.0]],
               [['Bruce', 'Wayne'], [10.0, 8.0, 74.0]],
               [['Captain', 'America'], [8.0, 10.0, 96.0]],
               [['Deadpool'], []]]

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0
