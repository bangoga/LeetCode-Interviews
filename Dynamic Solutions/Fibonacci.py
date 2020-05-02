# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:18:51 2020

@author: mohsi
"""

def fib(n):
    # Taking 1st two fibonacci nubers as 0 and 1  
    FibArray = [0, 1]  
    
    # form a + 1 memory array
    Second = [0]*(n-1)
    FibArray = [0,1] + Second
    
    
    return fibonacci(n,FibArray)

def fibonacci(n,fib_arr):
    
    if(n<=1):
        return n
    
    else: 
        if(fib_arr[n-1] == 0 ):
            fib_arr[n-1] = fibonacci(n-1,fib_arr)
        if(fib_arr[n-2]==0):
            fib_arr[n-2] = fibonacci(n-2,fib_arr)
            
    fib_arr[n] = fib_arr[n-1]+fib_arr[n-2]
            
    return fib_arr[n]

    
ans = fib(8)