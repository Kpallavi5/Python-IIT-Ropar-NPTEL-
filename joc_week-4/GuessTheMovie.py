# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:38:00 2023

@author: User
"""
import random
movies=['anand','drishyam','nayakan','anbe sivam','gol mMaal','vikram veda','black friday','dangal','manichithrathazhu','taare zameen par']

def play():
    p1name=input('player 1! Please enter your name: ')
    p2name=input('player 2! Please enter your name: ')
    
    pp1=0
    pp2=0
    turn=0
    willing=True #willing is variable which is true to start the game
    while willing:
        if turn%2==0:
            #player's 1 turn
            print(p1name,' Your turn')
            picked_movie=random.choice(movies) #this line will randomely pick movie from list movies
            qn=create_question(picked)
            print(qn)
            modified_qu=qn
            not_said=True
            while not_said:
                letter=input('You Letter: ')
                if(is_present(letter,picked_movie)):
                    modified_qu=unlock(modified_qu,picked_movie,ch)
                    print(modified_qu)
                    d=input('Press 1 to guess the movie or 2 to unlock another letter')
                    if d=1:
                        ans=input('Your answer')
                        if(ans==picked_movie):
                            pp1=pp1+1
                            print('Correct')       
                            not_said=False
                            print(p1name,'Your Score : ',pp1)
                        else:
                            print('wrong answer .Try again.')
                             
                else:
                    print(letter,'not found ')
            c=input(' Press 1 to continue or 0 to quit') 
            ifc==0:
                print(p1name,'Your Score : ',pp1)
                print(p2name,'Your Score : ',pp2)
                print('Thanks for playing')
                print('Have a nice day.')
                willing=False
        else:
            print(p1name,' Your turn')
            picked_movie=random.choice(movies) #this line will randomely pick movie from list movies
            qn=create_question(picked)
            print(qn)
            modified_qu=qn
            not_said=True
            while not_said:
                letter=input('You Letter: ')
                if(is_present(letter,picked_movie)):
                    modified_qu=unlock(modified_qu,picked_movie,ch)
                    print(modified_qu)
                    d=input('Press 1 to guess the movie or 2 to unlock another letter')
                    if d=1:
                        ans=input('Your answer')
                        if(ans==picked_movie):
                            pp1=pp1+1
                            print('Correct')       
                            not_said=False
                            print(p1name,'Your Score : ',pp1)
                        else:
                            print('wrong answer .Try again.')
                             
                else:
                    print(letter,'not found ')
            c=input(' Press 1 to continue or 0 to quit') 
            ifc==0:
                print(p1name,'Your Score : ',pp1)
                print(p2name,'Your Score : ',pp2)
                print('Thanks for playing')
                print('Have a nice day.')
                willing=False
            #player's 2 turn 
        turn=turn+1
                   
                    
                    
                    
          
                    
                   
                    
    

    


play()