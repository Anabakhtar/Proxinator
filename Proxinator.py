#Proxinator application by Syed Anab Akhtar
# Steps to use this zoom attendance bot
# STEP-1 : Record your voice saying "yes maam/sir" and save it as recording.mp3 in the same folder as this exe
# STEP-2 : Enter your details (name, roll no etc
# STEP-3 : Run it once before class and test if the program understands your pronunciation of your name
# STEP-4 : You might have to tweak some spellings, for example, my name is Anab but i entered spelling as anab/unab because thats what the program reads
# STEP-5 : Run the program when your class starts, be connected to the net, and now relax lol
#If you plan to use Proxinator anywhere, please do leave a star on the repo and give credits

#Here we imported the required libraries
import speech_recognition as sr
import os
import time
import pyautogui
import keyboard

#Before your class starts, change the meeting id and password here
mid="75964867460"
passid="PCd1m2"

time.sleep(2)

#change the path to where your zoom exe is
os.system('start C:/Users/Anab/AppData/Roaming/Zoom/bin/Zoom.exe')

time.sleep(2)

#this automatically clicks on the button but make sure your zoom is open in a maximized window
pyautogui.click(817, 486)

time.sleep(2)

pyautogui.write(mid)

time.sleep(3)

pyautogui.click(985, 692)

time.sleep(3)

pyautogui.write(passid)

time.sleep(2)

pyautogui.click(985, 692)





#this is the listening function, this will run in a loop
#in the if statements, change the path of recording.mp3 to where your voice recording is
#i have written so many if statements so that any user, even a python begginer can understand this Proxinator
while (True):
    def listentome():




        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("I heard : {}".format(text))

                if r.recognize_google(audio) == "1400": #your last four reg no digits
                    os.system('start C:/Users/Anab/Documents/Sound/recording.mp3')
                    time.sleep(2)
                elif r.recognize_google(audio) == "400": #your last three reg no digits
                    os.system('start C:/Users/Anab/Documents/Sound/recording.mp3')
                    time.sleep(2)
                elif r.recognize_google(audio) == "Anab": #your name
                    os.system('start C:/Users/Anab/Documents/Sound/recording.mp3')
                    time.sleep(2)
                elif r.recognize_google(audio) == "Syed": #your first name
                    os.system('start C:/Users/Anab/Documents/Sound/recording.mp3')
                    time.sleep(2)
                elif r.recognize_google(audio) == "unab": #another possible spelling of your name
                    os.system('start C:/Users/Anab/Documents/Sound/recording.mp3')
                    time.sleep(2)
                else:
                    print("Name/Reg not recognized")

            except:
                print("I heard nothing, are you even speaking?")


    listentome()










