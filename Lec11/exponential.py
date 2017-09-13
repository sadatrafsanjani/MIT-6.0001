# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:35:36 2017

@author: Rafsanjani
"""

def subSet(L):
    if len(L) == 0:
        return [[]]
    smaller = subSet(L[:-1])
    
    extra = L[:-1]
    new = []
    
    for s in smaller:
        new.append(s+extra)
        
    return smaller+new

print((4,5, 6, 7))