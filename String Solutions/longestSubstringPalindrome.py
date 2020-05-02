# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:18:58 2020

@author: mohsi
"""

def longestPalindrome(s):
        # ------------[ Form a N x N array of solutions] ----------------- #
        n = len(s)
        
        # -- [ The middle item is the same list being added, so any change will effect all dont use this]
        matching = [[0]*n]*n
        
        # -- [ decouple it using this ] -- # 
        matching = [sublist[:] for sublist in matching]
        
        string = s; 
        reverse = s[::-1]
        
        """
        [ _ | b | a | b | a | d ]
        [ d | _ | _ | _ | _ | _ ]
        [ a | _ | _ | _ | _ | _ ]
        [ b | _ | _ | _ | _ | _ ]
        [ a | _ | _ | _ | _ | _ ]
        [ b | _ | _ | _ | _ | _ ]        
        
        > Initialize by doing the first row and column
        """
        
        if(n==0):
            return ""
        
        # Doing first row
        
        for j in range(n):
            if string[j] == reverse[0]:
                (matching[0])[j]= (matching[0])[j]+1

        # doing first column
        
        for j in range(1,n):
            if reverse[j] == string[0]:
                (matching[j])[0]= (matching[j])[0]+1
                
        # save highest value index in list [row,column,value]

        highest=[0,0,0]        
                
        # forward
        
        for row in range(1,n):
            for col in range(1,n):
                upp_left = matching[row-1][col-1]
                if string[col] == reverse[row]:
                    new_value = matching[row][col]+1+upp_left
                    matching[row][col] = new_value
                    
                    if(highest[2]<=new_value):
                        highest[0] = row
                        highest[1] = col
                        highest[2] = new_value
                else:
                    matching[row][col] = 0
                         
        # Backwards
        
        ret_string = ""
        row = highest[0]
        col = highest[1]
        
        if(highest[2]>0):
            while(row>=0 and col>=0 and matching[row][col] != 0 ):
                ret_string = string[col]+ret_string
                row=row-1
                col=col-1
        else:
            ret_string = string[highest[1]]
            
        return matching
    
ans = longestPalindrome("aacdefcaa")