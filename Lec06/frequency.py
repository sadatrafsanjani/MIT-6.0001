# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 15:44:29 2017

@author: Rafsanjani
"""

def common(f):
    v = f.values()
    best = max(v)
    word = []
    
    for k in f:
        if f[k] == best:
            word.append(k)
    return (word, best)


def frequencies(lyrics):
    
    d = {}
    
    for word in lyrics:
        if word in d:
            d[word] += 1
        else: 
            d[word] = 1
            
    return d


s = "BodyCount,BodyCount.BodyCount,BodyCount.(YEAHMUTHAFUCKAAAAAA!)"

dictionary = frequencies(s)

keys = dictionary.keys()

for k in keys:
    print(k, ":", dictionary[k])


[a, b] = common(dictionary)
    
print(a, ":", b)