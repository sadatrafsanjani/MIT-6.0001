# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:00:56 2017

@author: Rafsanjani
"""

def selection(L):
    
    s = 0
    
    while s != len(L):
        for i in range(s, len(L)):
            if L[i] < L[s]:
                L[s], L[i] = L[i], L[s]
                
            print(L)
        s += 1
    


print(selection([27, 7, 3, 2, 1]))
    