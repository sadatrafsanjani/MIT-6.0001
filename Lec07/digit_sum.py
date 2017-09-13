# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:14:13 2017

@author: Rafsanjani
"""

def sumDigits(s):
    
    total = 0
    length = len(s)
    for i in range(length):
        try:
            total += int(s[i])
        except:
            print(s[i],"is a character")
            
    return total
            
    

print("Total:", sumDigits('a2b3c'))