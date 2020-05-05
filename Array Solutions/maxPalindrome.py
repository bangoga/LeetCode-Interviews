# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:32:18 2020

@author: mohsi
"""

def highestValuePalindrome(s, n, k):
        
    # form a n by n array
    opt = [[0]*n for x in range(n)]
 
    # initialize the diagnol 
    for row in range(n):
        opt[row][row] = 1
    
    # only go till row edge
    for row in range(n):
        for col in range(n):
            if(s[row]==s[col]):
                opt[row][col]=1
        
    # now from this find the biggest index with the changes.
    return opt


a = "3944273"
b =  len(a)
c =  3


def print_2d_array(s,arr):
    
    
    print("| |",end =" ")
    for val in s:
        print(val,end =" ")
        
    print("")
    for row in range(len(arr)):
        print("|"+s[row]+"|",end =" ")
        for col in range(len(arr)):
            print(arr[row][col],end =" ")
        print("")
        
get = highestValuePalindrome(a, b, c)


"""
Key thing the remember is th whole number is being returned after small changes r
"""
print_2d_array(a,get)