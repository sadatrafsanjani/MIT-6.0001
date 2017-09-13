# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:14:13 2017

@author: Rafsanjani
"""

def findEven(l):
    
    for i in l:
        try:
            if i%2 == 0:
                return i
        except:
            raise ValueError("No even number found")
    
    
even = findEven([1,2,3,4,5])
print("Even:", even)