# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 23:39:56 2017

@author: Rafsanjani
"""

def remove_duplicate(L, M):
    L1 = L[:]
    
    print(L)
    for e in L1:
        if e in M:
            L.remove(e)
            
    print(L)
    
    
L = [1, 2, 2, 4]
M = [1, 2]
remove_duplicate(L, M)