# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:01:32 2017

@author: Rafsanjani
"""

cube = 125
epsilon = 0.01
tries = 0


if cube < 0:
    low = cube
    high = 0
else:
    low = 0
    high = cube

guess = (low+high)/2.0

while abs(guess**3 - cube) >= epsilon:
    print("Low:", low, "High:", high, "Guess:", guess) 
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0
    tries += 1
    
print("Number of guesses:", tries)
print(guess, "is close to the cube root of", cube)
    
    