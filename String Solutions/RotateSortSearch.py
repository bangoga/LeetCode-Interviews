# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:10:41 2020

@author: mohsi
"""

def recursive(nums,x,target):
    
    p1= len(nums)//2 -1
    p2 = p1+1
    
    if(len(nums)<=3):
        if(nums[0]==target or nums[1] == target):
            return 0
            
        else: 
            return -1
        
    
    if(nums[p1]<nums[p2]):
        print(nums[p1],p1,nums[p2],p2)
        
    
    return recursive(nums[p1:len(nums)],p1,target)
    


arr=[4,5,6,7,0,1,2]
p1= len(arr)//2 -1
p2 = p1+1
arr[p1:len(arr)]
recursive(arr,0,0)