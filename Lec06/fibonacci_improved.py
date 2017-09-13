# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:45:43 2017

@author: Rafsanjani
"""

def f(n, d):
    if n in d:
        return d[n]
    else:
        a = f(n-1, d) + f(n-2, d)
        d[n] = a
        return a
        
d = {1:1, 2:2}

print(f(6, d))