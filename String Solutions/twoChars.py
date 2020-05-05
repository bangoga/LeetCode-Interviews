# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:18:06 2020

@author: mohsi
"""

def alternate(s):
    list_words = []
    word_count = {}

    for i in range(len(s)):
        char = s[i]
        char_n = "" 
        
        if(i!=len(s)-1):
            char_n =s[i+1]
        
        if (char not in list_words): # this means such a char has not been seen before
            word_count[char] = 1 
            list_words.append(char)
        
        else:
            if(word_count[char] != -1):
                word_count[char] = word_count[char]+1
                
        print(char,char_n)
        if(char == char_n): # if they are alternating
            print("alternating",char)
            word_count[char] = - 1
            

    # get me the two biggest chars    
    pair = [0,0]
    pair_char = ["",""]

    for char in list_words:
        if(word_count[char]>pair[0]):
            pair[0] = word_count[char]
            pair_char[0] = char
            
    for char in list_words:
        if(word_count[char]<=pair[0] and word_count[char]>pair[1] and char != pair_char[0]):
            pair[1] = word_count[char]
            pair_char[1] = char
            
    new_string = ""    
    for char in s:
        if(char == pair_char[0] or char == pair_char[1]):
            new_string=new_string+char
            
    print(new_string)
        
    return new_string

x= alternate("asdcbsdcagfsdbgdfanfghbsfdab")