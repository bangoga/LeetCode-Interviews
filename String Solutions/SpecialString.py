# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:24:16 2020

@author: mohsi
"""

def substrCount(n):
    # form the initial list 
    all_count = list(n)

    frame = 2
    while frame <=len(n):
        # check between frame 
        max_frame_index = frame
        print(max_frame_index)
        i = 0 
        while(max_frame_index<=len(n)):
            # check if palindrome between i and max frame
            # add to both ends +1 to offset it 
            substr = (n[i:max_frame_index])
            if(checkPalindrome(substr)):
                all_count.append(substr)
            i=i+1
            max_frame_index = max_frame_index +1 

                
        frame=frame+1
    return len(all_count)     
    
ans = substrCount("mnonopoo")    
    

checkPalindrome("aabaa")
## chaqnge from palindrome to special palindrome where it only checks the same values aa b aa rather than abx ba 

def checkPalindrome(s):
    # if even
    if (len(s)%2 == 0 ):
        middle = len(s)//2
        
        if((s[0:middle]).count(s[0])+s[middle:len(s)].count(s[0]) == len(s)):
            return True;
        else: return False
        #return ((s[0:middle]) == s[middle:len(s)])     
    # if odd 
    if(len(s)%2 == 1): 
        middle = len(s)//2
        if((s[0:middle]).count(s[0]) + s[middle+1:len(s)].count(s[0]) == len(s)-1):
            return True;
        else: return False 
        