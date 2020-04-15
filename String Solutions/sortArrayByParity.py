# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:31:44 2020

@author: mohsi
"""

        
"""

[1,3,2,5,4,8]

1 = odd but index of 1 aka 0 is even
3 = odd and index of 2 aka 1 is odd too


even index with odd number? go to the next odd index, till odd index with even number

Algorithmically"

for each value:
    if value.parity !=index.parity:
        flip_parity = index + 1
        flip_value = arr[flip_parity]
        
        loop:
            check if flip_parity has same parity as flip_value:
                if not, swap the value of this index with the original index (are of opposite parities so values will match now)
                else: flip_parity =+2 [Get next index with opposite parity of original index 
                
                go back to loop
"""
    
    
def sortArrayByParityII(A):
    # swaps
    
    for i in range(0,len(A)):

        """ Check if they are the same parity """
        if( (A[i]%2) != (i%2) ):
            # Change parity,
            x = i+1
            
            while(x<len(A)):
                if(A[x]%2 != x%2):
                    temp=A[x]
                    A[x]=A[i]
                    A[i]=temp
                    
                    break
                else: x=x+2

    return A