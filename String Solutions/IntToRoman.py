# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:45:23 2020

@author: mohsi
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        remainder = num
        roman = ""
        while(remainder>1):
            if((remainder-1000)>=0):
                remainder = remainder-1000
                roman=roman+"M"
            
            
            elif((remainder-900)>=0):
                remainder = remainder-900
                roman=roman+"CM"
                
            elif((remainder-500)>=0):
                remainder = remainder-500
                roman=roman+"D"
            
            
            elif((remainder-400)>=0):
                remainder = remainder-400
                roman=roman+"CD"
                
            elif((remainder-100)>=0):
                remainder = remainder-100
                roman=roman+"C"
                
            elif((remainder-90)>=0):
                remainder = remainder-90
                roman=roman+"XC"

            elif((remainder-50)>=0):
                remainder = remainder-50
                roman=roman+"L"
                
            elif((remainder-40)>=0):
                remainder = remainder-40
                roman=roman+"XL"
                
            elif((remainder-10)>=0):
                remainder = remainder-10
                roman=roman+"X"
                
            elif((remainder-9)>=0):
                remainder = remainder-9
                roman=roman+"IX"
                
            elif((remainder-5)>=0):
                remainder = remainder-5
                roman=roman+"V"
            
            elif((remainder-4)>=0):
                remainder = remainder-4
                roman=roman+"IV"
            
            elif((remainder-1)>0):
                remainder = remainder-1
                roman=roman+"I"
                
        if(remainder ==1):
            roman=roman+"I"
        print(roman)
        
        return roman
            