# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:52:29 2017

@author: Rafsanjani
"""

def isSubset(L1, L2):
    
    for m in L1:
        matched = False
        for n in L2:
            if m == n:
                matched = True
                break
        if not matched:
            return False
    return True

L1 = [55,66,77]
L2 = [1, 2, 55]

print(isSubset(L1, L2))