# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:18:06 2020

@author: mohsi
"""
import itertools
def alternate(s):
    list_words = []
    word_count = {}
    
    new_string = "" 
    
    # first pass to clean for no repeats 
    i=0
    while (i < len(s)):
        char = s[i]
        print(i)
        new_string = new_string+char
        while(i< len(s)-1 and s[i] == s[i+1]):
            i=i+1
       
        i=i+1
        
    for item in new_string:
        if(item in list_words):
            word_count[item]= word_count[item]+1
        else:
            word_count[item]=1
            list_words.append(item)
        
    # get all combinations
    words = ""
    pairs = [''.join(x) for x in itertools.combinations(words.join(list_words),2)]
    
    # make list of biggest
    combination_list = []
    
    for pair in pairs: 
        reduced_word = ""
        trailing_char = pair[0]
        reduced_word = reduced_word+trailing_char
        for char in s:
            if ((char == pair[0] or char == pair[1]) and trailing_char != char):
                reduced_word = reduced_word + char
                trailing_char = char
        
        # reduced word is made, add it to the list 
        combination_list.append(reduced_word)
                           
    return combination_list

x= alternate("beabeefeab")