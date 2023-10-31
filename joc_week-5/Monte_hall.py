# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:45:44 2023

@author: User
"""

import random
doors = [''] * 3
goatdoor = [] *2

swap = 0  # No. of swap wins
dont_swap = 0  # No. of don't swap wins
j=0
while(j<10):
    x = random.randint(0, 2)  # xth door will comprise of BMW
    doors[x] = 'BMW'
    for i in range(0, 3):
        if (i == x):
            continue
        else:
            doors[i] = 'Goat'
            goatdoor.append(i)
    choice = int(input("Enter Your Choice"))
    door_open = random.choice(goatdoor)  # open a door that comprises a goat
    while(door_open == choice):
        door_open = random.choice(goatdoor)
     
    ch = input("Do you want to swap? y/ n ")
    if (ch == 'y'):
        if(doors[choice] == 'Goat'):
            print("Player wins")
            swap = swap + 1
        else:
            print("Player lost")
    else:
        if(doors[choice] == 'Goat'):
            print("Player Lost")
        else:
            print("Player wins")
            dont_swap = dont_swap + 1

    print("Swap wins:", swap)
    print("Don't swap wins:", dont_swap)

    
