# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:51:42 2017

@author: Rafsanjani
"""

class Animal(object):
    
    def __init__(self, age):
        self.age = age
        self.name = None
        
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, age):
        self.age = age
        
    def set_name(self, name):
        self.name = name
     
    def __str__(self):
        return "Animal:" + str(self.name) + ":" + str(self.age)
        
a = Animal(5)
print(a.get_age())

a.set_age(7)
a.set_name("Leopard")

print(a)