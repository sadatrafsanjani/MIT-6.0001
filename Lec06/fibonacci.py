# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:26:55 2017

@author: Rafsanjani
"""

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def test():
    for i in range(7):
        print(fib(i))
        
test()