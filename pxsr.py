import pyttsx3
import speech_recognition as sr
import pyaudio
from ledconfig import *

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)    # Speed percent
engine.setProperty('volume', 0.9) 
#print(voices)
engine.setProperty('voices', voices[0].id)

#texttospeech
def speak(audio):
    led_on()
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    led_off()

def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            led_on()
            print("go on....")
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            led_off()
            print("Processing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("pardon me")
            return "None"
        query = query.lower()
        return query
