# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:52:09 2017

@author: Rafsanjani
"""

def copy(M, N):
        
    print(M)
    print(N)
    
    while len(N) > 0:
        N.pop()
    for e in M:
        N.append(e)
        
    print(M)
    print(N)
        
M = [1, 2, 3]
N = [] 

copy(M,N)
