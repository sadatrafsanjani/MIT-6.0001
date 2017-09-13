# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:09:44 2017

@author: Rafsanjani
"""

x = 5

def calc():
    global x
    x = 6
    print("Inside calc():",x)
    
print("Before:", x)
calc()
print("After:", x)
    