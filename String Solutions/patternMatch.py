# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:49:58 2020

@author: mohsi
"""

def isMatch(s,p):
    """
    Take queues pattern_queue and string_queue
    
        - take first element of pattern queue
            - Can be a-z, . ,  -->pattern_char
            
        - take first element of string --> string_char
            - if pattern_char==string_char or pattern_char == .
            
            true for this case
            
        - repeat, if at any point *, continue till next pattern string_char
    
    """
    # -> Covert to lower case 
    s=s.lower()
    p=p.lower()
    
    # -> Convert to a queue 
    pattern_queue=[char for char in p]
    string_queue=[char for char in s]
    
    i=0;
    j=0;
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    preceding = ""
    while(i<len(pattern_queue)):
        pattern_char = p[i]
        string_char  = s[j]
        
        if(pattern_char in alphabets):
            print(p)
        
        if
    
        preceding    = string_char
    
    
isMatch("ss","s*")