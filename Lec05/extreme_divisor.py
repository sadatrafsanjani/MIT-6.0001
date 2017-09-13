# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 15:22:10 2017

@author: Rafsanjani
"""

def findExtremeDivisors(m, n):

    minV, maxV = None, None
    
    for i in range(2, min(m, n) + 1):
        
        if (m%i == 0) and (n%i == 0):
            
            if(minV == None) or (i < minV):
                minV = i
                
            if(maxV == None) or (i > maxV):
                maxV = i
                
    return (minV, maxV)
    
minVal, maxVal = findExtremeDivisors(100, 200)
print("Minimum:", minVal, "Maximum:", maxVal)