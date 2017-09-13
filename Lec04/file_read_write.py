# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:27:43 2017

@author: Rafsanjani
"""

handle = open('kids','w')
handle.write('Max\n')
handle.write('Jedi\n')
handle.close()

handle = open('kids','r')

for line in handle:
    print(line[:-1])
handle.close()

handle = open('kids','a')
handle.write('Rogers\n')
handle.write('Billy\n')
handle.write('Roy\n')
handle.close()

handle = open('kids','r')
print(handle.read())
handle.close()


handle = open('kids','a')
handle.write("Black\n")
handle.close()

handle = open('kids','r')
print(handle.read())
handle.close()