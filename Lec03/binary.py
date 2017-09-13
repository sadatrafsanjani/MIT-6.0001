# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:16:40 2017

@author: Rafsanjani
"""


number = 10011
base = 1
result = 0
remainder = 0

while(number > 0 ):
    
    remainder = int(number % 10)
    number = int(number / 10)
    result += remainder * base
    base *= 2
    
    
print(result)