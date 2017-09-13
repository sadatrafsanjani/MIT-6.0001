# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 15:09:43 2017

@author: Rafsanjani
"""


def multiplication(a, b):
    
    if b == 1:
        return a
    else:
        return a + multiplication(a, b-1)
    
print(multiplication(9, 2))