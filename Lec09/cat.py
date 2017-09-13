# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:11:53 2017

@author: Rafsanjani
"""

import random

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

class Cat(Animal):
    
    def __init__(self, age):
        Animal.__init__(self, age)
    
    def speak(self):
        print("Meow")
        
    def __str__(self):
        return "Cat:" + str(self.name) + " : " + str(self.age)
    
    
class Person(Animal):
    
    def __init__(self, name, age):
        
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
        
    def get_friends(self):
        
        return self.friends
    
    def add_friends(self, fname):
        
        if fname not in self.friends:
            self.friends.append(fname)
            
    def speak(self):
        
        print("Hello")
        
    def age_difference(self, other):
       
        d = self.age - other.age
        print(abs(d))
    
    
    
class Student(Person):

    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
        
    def change_major(self, major):
        self.major = major
        
    def speak(self):
        
        r = random.random()
        
        if r < 0.25:
            print("Work")
        elif 0.25 <= r < 0.75:
            print("Sleep")
        elif 0.5 <= r < 0.75:
            print("Eat")
        else:
            print("TV")
            
            
class Rabbit(Animal):
    
    tag = 1
    
    def __init__(self, age, p=None, q=None):
        Animal.__init__(self, age)
        self.p = p
        self.q = q
        self.rid = Rabbit.tag
        Rabbit.tag += 1
        
    def get_rid(self):

        return str(self.rid).zfill(3)
    
    def get_p(self):
        
        return self.p
    
    def get_q(self):
        
        return self.q 
    
    def __add__(self, other):
        
        return Rabbit(0, self, other)

    def __eq__(self, other):
        
        same = (self.p.rid == other.p.rid and self.q.rid == other.q.rid)
        opposite = (self.q.rid == other.p.rid and self.p.rid == other.q.rid)
        
        return (same or opposite)
        

person1 = Person("Max", 23)
person2 = Person("Wayne", 72)
print(person1.get_friends())
person1.add_friends("Max")
print(person1.get_friends())
person1.age_difference(person2)

cat = Cat(8)
cat.speak()

r1 = Rabbit(14)
r2 = Rabbit(24)

r = r1+r2
print(r)
    