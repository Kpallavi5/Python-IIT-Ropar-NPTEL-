# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:12:49 2023

@author: User
"""
def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=="Rock " and player_two=="Scissor"):
        print("Player one wins!!")
    elif(player_one[p1]=="Rock " and player_two=="Paper"):
         print("Player two wins!!")
    elif(player_one[p1]=="Paper" and player_two=="Scissor"):
         print("Player two wins!!")
    elif(player_one[p1]=="Paper" and player_two=="rock"):
         print("Player one wins!!")
    elif(player_one[p1]=="Scissor" and player_two=="rock"):
         print("Player two wins!!")
    elif(player_one[p1]=="Scissor" and player_two=="Paper"):
         print("Player one wins!!")

player_one ={0:'Rock',1:'Paper',2:'Scissor'}
player_two ={0:'Rock',1:'Paper',2:'Scissor'}
while(1):
    num1=input("PLayer one,Enter your choice")
    num2=input("PLayer two,Enter your choice")
    bit1=int(input("Player one ,Enter the screct bit Position"))
    bit2=int(input("Player two ,Enter the screct bit Position"))
    rock_paper_scissor(num1, num2, bit1, bit2)
    ch=input("Do you want to continue? y/n")
    if(ch=='n'):
        break
