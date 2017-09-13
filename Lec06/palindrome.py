# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:26:55 2017

@author: Rafsanjani
"""

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if(c in 'abcdefghijklmnopqrstuvwxyz'):
                letters += c
        return letters
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))
    
print(isPalindrome("doggod"))