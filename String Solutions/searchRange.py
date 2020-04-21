# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:43:58 2020

@author: mohsi
"""

def searchRange(nums,target):
    
    low    = 0
    high   = len(nums)-1
    
    result=[-1,-1]
    
    while(low<=high):
        middle = (high+low)//2
        middle_l = middle-1
        middle_r = middle+1
        
        # throw another while to go forward and see 
        if(target == nums[middle]):
            print(middle)
            if(middle_l >=0 and nums[middle_l]== target):
                result = [middle_l,middle]
            elif(middle_r < len(nums) and nums[middle_r] == target):
                result = [middle,middle_r]
            else: result = [middle,middle]
            break
        
        if(target<nums[middle]):
            high=middle-1
            
        if(target>nums[middle]):
            low = middle+1
        
    print(result)
    return result
    
# searchRange([5,7,7,8,8,10],8)
# searchRange([5,7,7,8,8,10],6)
# searchRange([3,3,3],3)
searchRange([3,3,3],3)

