# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:16:49 2020

@author: mohsi
"""



def firstUniqChar(s):
# create ordered frequency 
    frequency  = {}
    word_list  = []
    index_list = [] # save the related index for faster get 
        
    unique = -1
    for i in range(len(s)):
        char = s[i]
        if char not in word_list:
            frequency[char] = 1
            word_list.append(char)
            index_list.append(i)
        else: 
            frequency[char] = frequency[char]+1 
            
    
    for i in range(len(word_list)):
        word = word_list[i]
        
        # if not unique break else add and leave
        if(frequency[word] == 1):
            unique = index_list[i]
            break
        
    
    
    return unique
ans = firstUniqChar("hello")