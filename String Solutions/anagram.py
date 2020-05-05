# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:11:17 2020

@author: mohsi
"""

def isAnagram(s , t):
    dic1={}
    dic2={}
    word_list1=[]
    word_list2=[]
    if(len(s) != len(t)):
        return False
    
    for char in s:
        if char not in word_list1:
            dic1[char] = 1
            word_list1.append(char)
        else: 
            dic1[char] = dic1[char]+1 
    
    for char in t:
        if char not in word_list2:
            dic2[char] = 1
            word_list2.append(char)
        else: 
            dic2[char] = dic2[char]+1 
            
            
    # for optimization 
    if(len(word_list1) != len(word_list2)):
        return False
    
    for word in word_list1:
        if(word not in dic2):
            return False
        elif (dic1[word] != dic2[word]):
            return False
            
    
    return True
ans = isAnagram("aatatd","tataax")