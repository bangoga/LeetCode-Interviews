# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:10:41 2020

@author: mohsi
"""
def sol(nums,target):
    start=0
    end=len(nums)-1
    ans = recursive(nums,start,end,target)
    print ("index is {0}".format(ans))
    

## Change this to involve more and less values ad well aka add comparators 
def recursive(nums,p1,p2,target):
    
    if(p2-p1 < 2):
        if(nums[p2]==target): return p2 
        elif(nums[p1]==target): return p1 
        else: return -1
    
    mid=((p2-p1)//2 + p1)
    print(mid)
    if(nums[mid-1] == target): return mid-1
    elif(nums[mid] == target): return mid
    elif(nums[mid+1] == target): return mid+1
    
    return recursive(nums,mid+1,p2,target)
    
    


arr=[4,5,6,7,0,1,2]
arr=[7,8,9,10,11,12,1,3]

sol(arr,11)
