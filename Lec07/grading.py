# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:14:13 2017

@author: Rafsanjani
"""

def getGrades(file):
    
    grades = []
    
    try:
        f = open(file, 'r')
    except IOError:
        raise ValueError('Error opening file')
        
    for line in f:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Could not perform convertion')
            
    return grades

try:
    grades = getGrades('grades.txt')
    grades.sort()
    print(grades)
    median = grades[len(grades)//2]
    print("Median grades is:", median)
except ValueError:
    print('Error!')
    