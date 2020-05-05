# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:18:58 2020

@author: mohsi
"""

def longestPalindrome(s):
    n = len(s)
    palindrome_list = [""]
    frames = list(s) ## Creates a list of initials 
    palindrome_list= palindrome_list + frames
    frame_size = 2
    while(frame_size<=n):
        index_offset = frame_size-1
        new_list_size = n-index_offset
        
        frames = frames[0:new_list_size] # reduce the frame size 
        print(frames)
        for i in range(new_list_size):
            word = frames[i]
            word = word + s[i+index_offset]## get the 
            frames[i]= word
            
            if(isPalindrome(word)):
                palindrome_list.append(word)
    
        frame_size=frame_size+1
    
    
    last_index = len(palindrome_list)
    ret_palindrome = palindrome_list[last_index]
    return len(ret_palindrome)
    
def isPalindrome(s):
    return (s==s[::-1])

    
ans = longestPalindrome("xtaabaatx")

len("aacdefcaa")
a="aacdefcaa"
a[0:len(a)-1]
"""
    aacdefcaa
    [a,a,c,d,e,f,c,a,a,aa] <--Last one is biggest palindrome. 
    [a,a,c,d,e,f,c,a,a] -> [aa,ac,cd,de,ef,fc,ca] --> [aac acd(X),cde,eff,fca,caa ]  
"""


