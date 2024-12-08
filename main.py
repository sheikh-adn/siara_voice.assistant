#library

import speech_recognition as sr  
import webbrowser
import pyttsx3
import musiclibrary
import requests
# from openai import OpenAI
from gtts import gTTS
import pygame
import os
from groq import Groq

#ai voice
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi =  #api key



def speak_old(text):

     engine.say(text)
     engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize the mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running to allow the music to play
    while pygame.mixer.music.get_busy():

        pass

    pygame.mixer.music.unload()
    os.remove("temp.mp3")



#functions
def aiprocess(command):
 #api key
        client = Groq(
            api_key= "get_your_api_key",
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{command}",
                }
            ],
            model="llama3-8b-8192",
        )

        return (chat_completion.choices[0].message.content)



def processCommand(c):
    if "open google " in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ",1)[1]
        if song in musiclibrary.music:
            speak(f"playing {song}")
            link = musiclibrary.music[song]
            webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("get.address.n..your.api.key.here")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])

            for article in articles:
                speak(article['title'])

    else:
        output=aiprocess(c)
        speak(output)




  



#working

if __name__ == "__main__":
    speak("initialising siyara")
while True:

    #listen for the wake word siara
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("listening....")
            audio = r.listen(source,timeout = 10, phrase_time_limit=10)
            print("recognizing...")


            command = r.recognize_google(audio)
            print(command) 
            if(command.lower() == "siyara"):
                speak("ya")

    
    # recognize speech using recognise_google
       
       
    
        with sr.Microphone() as source:

            print("siara active....")
            audio = r.listen(source )
            # print("recognizing...")
            command = r.recognize_google(audio)
            print(command) 
            
            processCommand(command)
         
    except sr.UnknownValueError:
         print("sorry sir ; could not understand the command")
         speak("sorry sir could not understand the command")
    except sr.RequestError as e:
        print("friday error; {e}")
        speak("error;")
