# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:14:13 2017

@author: Rafsanjani
"""

def readInt():
    
    while True:
        data = input("Enter an integer:")
        try:
            data = int(data)
            return data
        except ValueError:
            print(data, "is not an integer!")
    
readInt()