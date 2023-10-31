# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:03:41 2023

@author: User
"""

def magic_square(n):
    
    magicSquare = []
    for i in range (n):
        l=[]
        for j in range (n):
            l.append(0)
        magicSquare.append(l)    
        

    for i in range (n):
        
    
        for j in range (n):
            print(magicSquare[i][j], end = " ")
        print()
            
         
          
      
       
            