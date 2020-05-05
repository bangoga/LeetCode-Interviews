# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:10:56 2020

@author: mohsi
"""

# dont even delete it 
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    
    n = len(take_out_orders)
    m = len(dine_in_orders)
    a=0
    b=0 
    
    for i in range(len(served_orders)):
        if((a>=n and b>=m)):
            print("out of range")
            return False
        
        item = served_orders[i]
        if(a<n and item == take_out_orders[a]):
                a=a+1
                print(take_out_orders[a:n],a)
        
        elif(b<m and item == dine_in_orders[b]):
                b=b+1
                print(dine_in_orders[b:m],b)

        else:
            return False
        
    if(a!=n or b!=m):
        return False

    return True


A=[1, 9]
B=[7, 8]
C= [1, 7, 8]

x=is_first_come_first_served(A,B,C)