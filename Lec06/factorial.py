# -*- coding: utf-8 -*-

    
def fact(n):
    
    if(n == 1):
        return n
    else:
        return n * fact(n-1)

print("Factorial of", 7, "is:", fact(7))