# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:30:19 2017

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



class MITPerson(Person):
    
    nextId = 0
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.id = MITPerson.nextId
        MITPerson.nextId += 1
        
    def getId(self):
        return self.id

    def __lt__(self, other):
        return self.id < other.id
    
    def isStudent(self):
        return isinstance(self, Student)
    
    
    
class Student(MITPerson):
    pass



class UG(Student):
    
    def __init__(self, name, year):
        MITPerson.__init__(self, name)
        self.year = year
            
    def getYear(self):
        return self.year


    
class Grad(Student):
    pass    



class Transfer(Student):
    
    def __init__(self, name, school):
        MITPerson.__init__(name)
        self.school = school
    
    def getOldSchool(self):
        return self.school
    
    
    
class Grades(object):
    
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
        
        
    def addStudent(self, s):
        if s in self.students:
            raise ValueError("Duplicate Entry!")
            
        self.students.append(s)
        self.grades[s.getId()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        try:
            self.grades[student.getId()].append(grade)
        except:
            raise ValueError("Error adding value!")
        
        
    def getGrade(self, student):
        try:
            return self.grades[student.getId()][:]
        except:
            raise ValueError("Not Found!")
    
    def getStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s
        
        
p1 = MITPerson('Mark Guttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

print("p1 < p2 =", p1 < p2)
print("p3 < p2 =", p3 < p2)
print("p4 < p1 =", p4 < p1)


p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
print(p5, "is a graduate student", type(p5) == "Grad")
print(p6, "is a undergraduate student", type(p6) == "UG")

print(p5, "is a student is", p5.isStudent())
print(p3, "is a student is", p3.isStudent())
print(p6, "is a student is", p6.isStudent())


book = Grades()
book.addStudent(Grad('Julie'))
book.addStudent(Grad('Charlie'))

for s in book.getStudents():
    print(s)