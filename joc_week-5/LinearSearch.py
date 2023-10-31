# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:38:13 2023

@author: User
"""
def linear_search(n,x): # n is range ,x is parameter which i want to find
    element=[]
    for i in range(1,n):
        element.append(i)
    count = 0    
    flag = 0
    for i in element:
        
         count+=1
         if(i==x):
             print("Yes I found my number at position:"+str(i))
             #print("Yes I found my number at position:",element[i])
             flag = 1
             break
             
    if(flag==0):
        print("Number is Not found")
         
    
    
    print("Number of iteration : "+str(count)) 
    
    
    
def binary_search(a,x):
    first_pos =0
    last_pos =len(a)-1
    flag=0# flag=0 means that the element has not been found yet
    count =0
    print("the last position is", last_pos)
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid=(first_pos+last_pos)//2
        if(x==a[mid]):
            flag=1
            print("The element is present at pos:" +str(mid))
            print("The number of iteration are:" +str(count))
            return
        else:
            if(x<a[mid]):
               last_pos = mid-1
            else:
                first_pos=mid+1
                 
    print(" The Number is not present ") 
    
    
a= [ ]
for i in range(1,10):
    a.append(i)
print(a)
print(len(a))
    
binary_search(a,6)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    