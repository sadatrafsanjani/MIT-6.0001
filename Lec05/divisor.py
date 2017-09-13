# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 15:22:10 2017

@author: DOLPHIN
"""

def findDivisors(m, n):
    
    divisors = ()
    
    for i in range(1, min(m, n) + 1):
        if (m%i == 0) and (n%i == 0):
            divisors = divisors + (i, )
    return divisors
    
d = findDivisors(20, 100)
print(d)
counter = 0
for i in d:
    print(i)
    counter += 1
    
print("Total Divisors: ",counter)
        