# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:16:11 2017

@author: Rafsanjani
"""

def f(x):
    def g():
        x = 'abc'
        print("X = ", x)
    def h():
        z = x
        print("Z = ", z)
    x += 1
    print("X = ", x)
    h()
    g()
    print("X = ", x)
    
    return g

x = 3
z = f(x)
print("X = ", x)
print("z = ", z)
z()