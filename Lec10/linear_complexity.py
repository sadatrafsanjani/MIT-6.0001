# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:41:16 2017

@author: Rafsanjani
"""

def linear_search_unsorted(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found


def linear_search_sorted(L, e):
    
    for i in range(len(L)):
        if e == L[i]:
            return True
        elif L[i] > e:
            return False
    return False


L = [9, 8, 5, 3, 4]


print(linear_search_unsorted(L, 4))
print(linear_search_unsorted(L, 12))