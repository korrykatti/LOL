import pyttsx3
# import speech_recognition as sr
from gtts import gTTS
import datetime



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 160)
#print(voices)
engine.setProperty('voice', voices[11].id)



print('''

                                                                   
                                                                   
LLLLLLLLLLL                  OOOOOOOOO     LLLLLLLLLLL             
L:::::::::L                OO:::::::::OO   L:::::::::L             
L:::::::::L              OO:::::::::::::OO L:::::::::L             
LL:::::::LL             O:::::::OOO:::::::OLL:::::::LL             
  L:::::L               O::::::O   O::::::O  L:::::L               
  L:::::L               O:::::O     O:::::O  L:::::L               
  L:::::L               O:::::O     O:::::O  L:::::L               
  L:::::L               O:::::O     O:::::O  L:::::L               
  L:::::L               O:::::O     O:::::O  L:::::L               
  L:::::L               O:::::O     O:::::O  L:::::L               
  L:::::L               O:::::O     O:::::O  L:::::L               
  L:::::L         LLLLLLO::::::O   O::::::O  L:::::L         LLLLLL
LL:::::::LLLLLLLLL:::::LO:::::::OOO:::::::OLL:::::::LLLLLLLLL:::::L
L::::::::::::::::::::::L OO:::::::::::::OO L::::::::::::::::::::::L
L::::::::::::::::::::::L   OO:::::::::OO   L::::::::::::::::::::::L
LLLLLLLLLLLLLLLLLLLLLLLL     OOOOOOOOO     LLLLLLLLLLLLLLLLLLLLLLLL
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   
                                                                   

 , ''')

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

a = input("Filename please ( must be .txt ) and must be in same folder: \n")

print("Proceeds to speak")

f = open(a, "r")
speak(f.read())

print("More file type support soon .")
print("Contribute : https://github.com/korrykatti/LOL")