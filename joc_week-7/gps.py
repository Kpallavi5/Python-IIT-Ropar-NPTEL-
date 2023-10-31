# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:50:33 2023

@author: User
"""
#iterative way 
def factorial(n):
    product = 1
    for i in range(1,n+1):
        product = product * i
    return product    

n= int(input('Enter a positive number '))
if(n<0):
    print('Factorial id not define on negative numbers ')
else:
    f=factorial(n)
    print('Factorial of ', n ,'is',f) 
    
    