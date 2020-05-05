# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:53:56 2020

@author: mohsi
"""

def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list
    
    n = len(my_list)
    m = len(alices_list)
    
    ret_list = []
    
    i = 0
    j =  0


    ## figure out which one is shorter
    
    if(n<=m):
        while(i<n and j<m):
            int1 = my_list[i]
            int2 = alices_list[j]
            if(int1<=int2):
                ret_list.append(int1)
                i=i+1            
            else:
                ret_list.append(int2)
                j=j+1
        print(j)
        ret_list.extend(alices_list[j:m])
            
    if(m<=n):
        while(j<m and i<n):
            int1 = my_list[i]
            int2 = alices_list[j]
            if(int1<=int2):
                ret_list.append(int1)
                i=i+1            
            else:
                ret_list.append(int2)
                j=j+1
        print(i)
        ret_list.extend(my_list[i:n])
            
    return ret_list


B = [3, 4, 6, 10, 11]
A = [1, 5, 8, 12, 14]
merge_lists(A,B)


# this is O(K) where is the size n+m