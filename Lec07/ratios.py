# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:50:51 2017

@author: Rafsanjani
"""

def ratios(M, N):
    r = []
    
    for i in range(len(M)):
        
        try:
            r.append(M[i]/N[i])
            
        except ZeroDivisionError:
            r.append(float('nan'))
        
        except:
             raise ValueError('Error:')
             
        return r
    
x = [5 ,6, 7]    
y = [1, 2, 3]

print(ratios(x, y))