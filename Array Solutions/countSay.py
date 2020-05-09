# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:35:54 2020

@author: mohsi
"""

# =============================================================================
#   The number n is between 1 and 30
#   count in the lowest possible way a number can be read
#   2- 1 is read off as "one 1" or 11.
#   3- 11 is read off as "two 1s" or 21.
#   4- 21 is read off as "one 2, then one 1" or 1211.
#   5- 111221

#   nth term is the read-off of the (n - 1)th term

#   so seeing how many types of a digit exist in the previous iteration, that is new number

#   if 111221 is the last one 
#   first unique digit is 1, how many of 1s are here? only one, so we write down 1
#   second unique [unhindered/sequenced] digit is 2, how many twos in sequence, 2 so we write 22's
#   third is 1, and how many 1's together? well 3 so we write 31's

#   combine all together its 31's + 22's + 11's so 312211 is the new number

#   think recursively
#   Base case = 1 

# =============================================================================
def countAndSay(n):
    
    if (n == 1):
        return "1"
    
    if (n == 2):
        return "11"

    prev = countAndSay(n-1)
    ret_string = ""
    
    print(n)
    c_char = prev[len(prev)-1]
    count = 1
    index = -1
    all_counts=[]
    # goes from previous lens to 0 
    for i in range(len(prev)-1,-1,-1):
        if(c_char == prev[i]):
            count = count +1
        # if its the last one 
        elif:
        else :
            ret_string = str(count)+c_char+ret_string
            count = 1
            c_char = prev[i]
            
    return ret_string

countAndSay(3)



x = "21"
r = x[len(x)-1]
# =============================================================================
# 
# 
# 
# =============================================================================
