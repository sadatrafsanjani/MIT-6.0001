# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:32:14 2017

@author: Rafsanjani
"""

epsilon = 0.01
number = 27.0
guess = number/2.0
tries = 0

while abs(guess*guess - number) >= epsilon:
    guess -= (((guess**2) - number) / (2*guess))
    tries += 1
    
print("Newton-Raphson Method")
print("Square root of", number , "is", guess)
print("Number of guesses:", tries)