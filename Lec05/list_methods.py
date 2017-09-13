# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 15:22:10 2017

@author: Rafsanjani
"""

L = [1,2,3,3,4,5]
M = [127,7,88]

print("L:", L)
L.append("ABC")
print("L:", L)
print("Count:", L.count(3))
L.insert(3,9)
print("Insert:", L)
L.extend(M)
print("L is Extended with M:", L)
print("Index of 5 is:", L.index(5))

print("Popped data from position 1:", L.pop(1))
L.reverse()
print("Reverse:", L)
M.sort()
print("Sort:", M)