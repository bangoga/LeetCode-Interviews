# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:38:27 2020

@author: mohsi
"""

def longestValidParentheses(s):
    
    """
    Dynamic solution
        
        recursion
        memoization
        
        
    """
    arr = [0]*len(s)
    ans = recursizeSolution(s,[],arr,0)
    print(ans)
    
    largest=0
    for i in range(1,len(s)):
        if(len(s) == 1):
            break
        
        if(ans[i] > 0 ):
            ans[i]=ans[i]+ans[i-1]
            if(ans[i]>largest):
                largest=ans[i]
                
    print(ans,largest)
    

"""
    - brack index
    - valid pairs
    
    - [0,0,0,0,0,0,0,0]
    - [0,1,1,0,0,0,0,0]
    - []
"""



def recursizeSolution(s,bracks,valids,index):
    if(len(s)==0):
        return valids

    # if its an opening, insert the openings index    
    if(s[0] == "("):
        bracks.append(index)
    
    # if its a closing,check if there is a opening available, if so, add 1 to both their positions to mark
    if(s[0] == ")" and len(bracks)>0):
            
            #remove the last bracket
            open_i = bracks[len(bracks)-1] # get the opening index
            close_i = index
            
            bracks = bracks[:len(bracks)-1]
            
            valids[open_i]=1
            valids[close_i]=1
            
    index=index+1
    return recursizeSolution(s[1:len(s)],bracks,valids,index)




longestValidParentheses("(()")


s="(())"

s[len(s)]










