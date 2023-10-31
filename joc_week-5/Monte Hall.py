# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:39:07 2023

@author: User
"""
import random
doors=[]*3
goatdoor=[]

swap=0 #No. of swap wins
dont_swap=0 #No. of dont swap wins
x=random.randint(0,2) #xth door will comprise of BMW
doors[x]='BMW'
for i in range (0,3):
    if (i==x):
        continue 
    else:
        door[i]="Goat"
        goatdoor.append9(i)
choice=int(input("Enter Your Choice"))
door_open = random.choice(goatdoor) #open a door that comprises a goat
 #open a door that comprise
while(door_open==choice):
    door-open=random.choice(goatdoor)
    
ch=input("Do you want to swap ?")
if (ch=='y'):
    if(doors[choice]=='Goat')
         print("Player wins ")
         swap=swap+1
    else:
        print("Player lost")
else:
    if(doors[choice]='Goat'):
        print("Player Lost")
    else:
        print("Player wins")
        dont_swap=dont_swap+1
        
print(swap)
print(dont_swap)
        
    
    
    

        
        
