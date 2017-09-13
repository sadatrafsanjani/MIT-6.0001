# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 15:26:58 2017

@author: Rafsanjani
"""


def tower(n, froms, to, spare):
    
    if n == 1:
        print(froms, " --> ", to)
    else:
        tower(n-1, froms, spare, to)
        tower(1, froms, to, spare)
        tower(n-1, spare, to, froms)
        
print(tower(3, 1, 2, 3))