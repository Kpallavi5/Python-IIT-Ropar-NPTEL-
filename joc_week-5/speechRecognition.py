# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:57:47 2023

@author: User
"""

import speech_recognition as sr
AUDIO_FILE=("samplepallavi.wav")
#use audio file as souce 

r=sr.Recognizer() #intialise the recognizer

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
#reads the audio file 

try:
    print("audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError :
    print ("Google Speech Recognition could not understand audio")
except sr.UnknownValueError :
    print ("Couldn't get the results from Google Speech Recognition")
              
    

