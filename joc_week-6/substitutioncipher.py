# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 07:31:51 2023

@author: User
"""
import string 
dict = { }
data=" "
file=open("op_cipherdemo.txt","w")
for i in range (len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("cipherdemo.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print ("End  of file ")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)    
        print(data)    
file.close()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    