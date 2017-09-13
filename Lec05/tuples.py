# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 21:57:01 2017

@author: Rafsanjani
"""


t1 = ()
t2 = (1, "Man", 2)
print(t1)
print(t2)

t3 = (3, 'xyz', 9)
print(t2+t3)
t4 = (t1, t2, t3)

print("t4:", t4)
print("t4[2]",t4[2])
print("t4[2:5]",t4[2:5])

print("Initiation")

x,y = (3, 4)
print("x:",x, "y:", y)