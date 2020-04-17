# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:49:58 2020

@author: mohsi
"""

def isMatch(self, s: str, p: str) -> bool:
    """
    Take queues pattern_queue and string_queue
    
        - take first element of pattern queue
            - Can be a-z, . ,  -->pattern_char
            
        - take first element of string --> string_char
            - if pattern_char==string_char or pattern_char == .
            
            true for this case
            
        - repeat, if at any point *, continue till next pattern string_char
    
    """
        