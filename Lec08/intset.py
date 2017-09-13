# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 19:48:59 2017

@author: Rafsanjani
"""

class IntSet(object):
    
    def __init__(self):
        
        self.storage = []
        
    def insert(self, e):
        
        if not e in self.storage:
            self.storage.append(e)
            
    def getMember(self, e):
        
        return e in self.storage
    
    def remove(self, e):
        
        try:
            self.storage.remove(e)
        except:
            raise ValueError(e, " not found in the list!")
            
    def getMembers(self):
        
        return self.storage[:]
    
    def __str__(self):
        
        self.storage.sort()
        
        result = ""
        
        for e in self.storage:
            result += str(e) + ','
            
        return "{" + result[:-1] + "}"
    
    
s = IntSet()

s.insert(9)
s.insert(14)
s.insert(0)
print(s.getMember(9))
s.remove(9)
print(s.getMember(9))
print(s)
print(s.getMembers())
    