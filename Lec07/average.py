# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:06:57 2017

@author: Rafsanjani
"""

def get_stats(lists):
    s = []
    
    for e in lists:
        s.append([e[0], e[1], avg(e[1])])
        
    return s

def avg(grades):
    
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("Warning:")
        return 0.0

p = [[['Peter', 'Parker'], [78, 92, 86]], [['Bruce','Wayne'], [98, 92, 65]]]

print(get_stats(p))