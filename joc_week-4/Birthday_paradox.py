# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:05:28 2023

@author: User
"""

import random
year=random.randint(1990,2018)
print(year)
if (year%4==0 and year%100!=0 or year%400==0):
    print("Given year is a Leap Year")
else:
    print("Given yera is not a leap Year")
    
