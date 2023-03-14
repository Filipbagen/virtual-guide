from gtts import gTTS

def text_to_speech(text):

   # Skapa en instans av gTTS för svenska
    tts = gTTS(text=text, lang='sv', slow=False)
    # Spara tal som en MP3-fil
    # Hamnar i en annan map av en anledning
    tts.save("tts.mp3")









