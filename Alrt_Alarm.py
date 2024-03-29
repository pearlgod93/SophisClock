#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:14:25 2019

@author: muthu93
"""
#Libraries
import speech_recognition as sr
import datetime as dt
import os
import time
from gtts import gTTS
import subprocess as sb
#======================================#

#Recognizer initialization
r = sr.Recognizer()

#Variable list - Add values to the dictionary
#alarm_list = {1: '06:15', 2: '12:15', 3: '16:15', 4: '20:15'} #Delete after test

global RightAns
# Check time for every second
def AlertAlarm(alarm_list, name):
    # Pass a dictionary of values and your name for Greeting purpose
    j = 1
    while (j == 1):
        for i in list(alarm_list.values()):
            if (i == ReadTime()):
                playAlarm(name, int(i[0:2]))
        time.sleep(10)
        
#Read_Time
def ReadTime():
    curr_time = dt.datetime.now()
    time_hrmn = curr_time.strftime("%H:%M")
    print(time_hrmn)
    return str(time_hrmn)

"""#TO-DO
#Set alarm time - Change to different module
def Set_Alm_Time():
    Alm_tim = input("Enter the alarm time in 24-Hour (HH:MM) format: ")
    if (Alm_tim not in alarm_list.values):
        alarm_list.update({(len(alarm_list)+1): Alm_tim})"""

#Listen for the answer
def ListAns():
    with sr.Microphone() as source:
        print('Speak Something')
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            #print('You said: {}'.format(text))
            return text
        except:
            print('Sorry could not recognize anything !!')
            return "zxyz"
            
#Playing Alarm with the question
def playAlarm(name, num):
    RightAns = False
    #Selecting the Greeting
    if(num >= 00 and num < 12):
        Wish = "Good morning"
    elif(num >= 12 and num < 16):
        Wish = "Good Afternoon"
    elif(num > 15 and num < 21):
        Wish = "Good Evening"
    else:
        Wish = "Good Night"


    Speech_format  = 'Hello ' + name + '!! ' + Wish + '!!'
    tts = gTTS(text  = Speech_format,  lang='en')
    tts.save('Wishes.mp3')
    sb.call(["afplay","Wishes.mp3"])
    if(RightAns == False):
        PlayQues()
    else:
        ReadTime()
    
def PlayQues():
    Ques = "Say 'Hello', to stop the alarm my friend!"    
    ttsQues = gTTS(text  = Ques,  lang='en')
    ttsQues.save('Ques.mp3')
    sb.call(["afplay","Ques.mp3"])
    AnswerList()

def AnswerList():
    if('hello' in ListAns()):
        ttsGJ = gTTS(text  = 'Good Job, buddy!',  lang='en')
        ttsGJ.save('Good_job.mp3')
        sb.call(["afplay","Good_job.mp3"])
        time.sleep(30)
    else:
        ttsPls = gTTS(text  = 'Please state your answer correctly!',  lang='en')
        ttsPls.save('Please_Repeat.mp3')
        sb.call(["afplay","Please_Repeat.mp3"])
        PlayQues()


"""#Function to  call the alarm app
#Example Function call
alarm_list = {1: '16:26', 2: '16:24'} #Delete after test
AlertAlarm(alarm_list, "Muthu")""""
