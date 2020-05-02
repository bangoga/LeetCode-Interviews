# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:08:05 2020

@author: mohsi
"""

#   Given a string "A" you can perform these operations on it
#   Captialize 0 or more letters of A that are lowercase
#   Delete the rest of the lowercases of A
#   
#   With that in mind if you have two strings A and B, determine if 
#   These two strings can have the same abbreviations
#   
#   Approach will be to save all Capital letters in order in an two arrays
#   If they don't have same capitals [Aka one capital is a letter captial not even existing as any case in other] return no] return no 
#   Else use that as dynamic arrays.

"""
        Note string B is ONLY capital letters.
"""


#   [B] and [A,B,C]
#   Knowing cancel condition is Having a letter not in B or finding string same size of B
#
#   AbcDE and ABDE
#   [A] -> its a good capital, let it remain, [B] is a good capital as wel capitalize it, C not, D is and E is 
 
#   You can choose these steps on your own. as well. Consider 
#   daBcd and ABC I know B and ABC are valid and to length difference is 2
#   So I can selected two values and delete the others 
#


# Save in the memory whats already a valid capital so string value B is saved. 
# [0,2]


a = "abcd"

a[len(a)-1]

import math
import os
import random
import re
import sys


def abbreviation(a, b):

        
ans = abbreviation("daBcd","ABC")