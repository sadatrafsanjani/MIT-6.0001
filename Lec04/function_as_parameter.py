# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:16:11 2017

@author: Rafsanjani
"""

def f(x):
   print("Inside f()")
   print(x)
   
   return x()

def g():
    print("Inside g()")
    
f(g)