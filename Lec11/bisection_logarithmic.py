# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:57:21 2017

@author: Rafsanjani
"""

def bisect_search_1(L, e):
    
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search_1(L[:half], e)
        else:
            return bisect_search_1(L[half:], e)


def bisect_search_2(L, e):
    
    def helper(L, e, low, high):
        if high == low:
            return L[low] == e
        
        mid = (low + high)//2
        
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return helper(L, e, low, mid-1)
        else:
            return helper(L, e, mid+1, high)
    
    
    if len(L) == 0:
        return False
    else:
        return helper(L, e, 0, len(L)-1) 
        

        
L = [8, 3, 5, 6, 7]
L.sort()
print(L)
print(bisect_search_1(L, 3))
print(bisect_search_2(L, 3))