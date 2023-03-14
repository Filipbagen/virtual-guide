from unittest import registerResult
# from playsound import playsound


from FaceTrack.FaceTrack import *
from Sound.speech_to_text import *
from Sound.text_to_speech import *



import os
#for a in face_track():


  
face = False
temp = False 
  
for face in face_track(): 
    if face == True:
        result = speech_to_text()
        print(result["text"])
        text_to_speech("Funkar det nu?")
        os.system("tts.mp3")
        
