# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 22:37:53 2017

@author: Rafsanjani
"""

def qAndr(x, y):
    q = x // y
    r = x % y
    
    return (q, r)

(q, r) = qAndr(30, 5)

print("q=", q)
print("r=", r)
