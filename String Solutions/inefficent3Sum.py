# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:55:55 2020

@author: mohsi
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return a list of lists that all gives a sum 0
        
        listOfSumZero=[]
        
    
        """
        a+b+nums[i] = 0 
        a+b = -nums[i]
        make a dictionary of all sums
        with the summation value as key and (a,b) tuple as a value
        [4,2,4] -- 4 - 2 = 2 2 exists but is used
        listOfSumZero with only sorted values, makes check easier by standardizing
        """
            
        dictionary = dict.fromkeys(nums , ["",""])
    

        
        for i in range(len(nums)-1):
            
            a = nums[i]
            for j in range(i+1,len(nums)):
                equation=[]
                b = nums[j]
                
                c = -a-b
                
                if(c in self.shortList(i,j,nums)):
                    #print ("number exists {0} + {1} + {2} = 0".format(a,b,c))
                    equation.append(a)
                    equation.append(b)
                    equation.append(c)
                    equation.sort()
                    if(equation not in listOfSumZero):
                        listOfSumZero.append(equation)
                    
        return listOfSumZero
    
    # function takes a list and returns a shorter list without elements a and b
    def shortList(self, a: int,b:int,arr:List[int]) -> List[int]:
        newList = arr[:]
        newList.pop(a)
        newList.pop(b-1)
        return newList