# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:00:56 2017

@author: Rafsanjani
"""

def merge(left, right):
    
    result = []
    i,j = 0, 0
    
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    while(i < len(left)):
        result.append(left[i])
        i += 1
        
    while(i < len(left)):
        result.append(right[j])
        j += 1
        
    return result


def merge_sort(L):
    
    print(L)
    
    if len(L) < 2:
        return L[:]
    else:
        m = len(L)//2
        left = merge_sort(L[:m])
        right = merge_sort(L[m:])
        return merge(left, right)
    


print(merge_sort([27, 7, 3, 2, 1]))
    