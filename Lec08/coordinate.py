# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:55:40 2017

@author: Rafsanjani
"""

class Coordinate(object):
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
    def distance(self, other):
        
        ax = (self.x - other.x)**2
        ay = (self.y - other.y)**2
        
        return (ax + ay)**0.5
    
    def __str__(self):
        
        return str(self.x) + ", " + str(self.y)
    
    
p = Coordinate(5, 3)
q = Coordinate(1, 2)

print("Using Object:", p.distance(q))
print("Using Classname:", Coordinate.distance(p, q))
print(p)
print(type(p))
print(type(Coordinate))
print(isinstance(p,Coordinate))