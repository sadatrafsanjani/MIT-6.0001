# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:37:22 2017

@author: Rafsanjani
"""

import datetime

class Person(object):
    
    def __init__(self, name):
        
        self.name = name
        
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
            
        self.birthdate = None
        
    def getName(self):
        
        return self.name
    
    def getLastName(self):
        
        return self.lastName
    
    def setBirthdate(self, birthdate):
        
        self.birthdate = birthdate
        
    def getAge(self):
        
        if self.birthdate == None:
            raise ValueError("Birthdate is not set!")
            
        return (datetime.date.today() - self.birthdate).days
    
    def __lt__(self, other):
        
        if self.lastName == other.lastName:
            
            return self.name < other.name
        
        return self.lastName < other.lastName
    

    def __str__(self):
        
        return self.name
    

me = Person("Michael Guttag")
him = Person("Barack Hussein Obama")
her = Person("Madonna")
print(him.getLastName())
him.setBirthdate(datetime.date(1961, 8, 4))
her.setBirthdate(datetime.date(1958, 8, 16))
print(him.getName(), "is", him.getAge(), "days old")


print(him < me)

pList = [me, him, her]
for p in pList:
    print(">> ", p)

pList.sort()
print("----- Sorting -----")

for p in pList:
    print(">> ", p)
