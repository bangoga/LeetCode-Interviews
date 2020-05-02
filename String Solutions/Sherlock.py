# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:32:44 2020

@author: mohsi
"""

def isValid(s):
    word_count = {}
    frequency = {}
    key_list = []
    
    s=s.lower()
    
    for char in s:
        if char not in word_count:
            word_count[char]=1
        else:
            word_count[char]=word_count[char]+1
        
    for char in word_count:
        if word_count[char] not in frequency:
            frequency[word_count[char]] = 1
            key_list.append(word_count[char])
        else:
            frequency[word_count[char]] = frequency[word_count[char]] + 1 
    
    if(len(key_list)>2):
        return "NO"
    
    if(len(key_list)>1 and frequency[key_list[1]]>1 ):
            return "NO"
    
    return "YES"

ans = isValid("aabbccde")
