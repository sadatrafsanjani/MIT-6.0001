# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:41:19 2017

@author: Rafsanjani
"""

d = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E'}

print(d)

print("Length:", len(d))
print("Keys:", d.keys())
print("Values:", d.values())
print("1 in d:", 1 in d)
print("d[1]:", d[1])
d[1] = 'XXX'
print("d[1]:", d[1])
del d[1]