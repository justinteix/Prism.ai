from pathlib import Path
from openai import OpenAI
import os
import speech_recognition as sr
import time
import warnings
from dotenv import load_dotenv
import pygame

load_dotenv()
pygame.init()
warnings.filterwarnings("ignore", category=DeprecationWarning)
r = sr.Recognizer()

def text_gen(question):
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful voice assistant. Keep your answers brief and no more than 15 seconds long."},
        {"role": "user", "content": question}
    ],
    )
    
    return response.choices[0].message.content   


def text_to_speech(text_question):
    client = OpenAI()

    speech_file_path = "audio/answer.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="fable",
    input=text_question
    )
    
    response.stream_to_file(speech_file_path)
 
def listen_for_wake_word(source):
    print("Listening for 'Hey Prism'...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if "hey prism" in text.lower():
                wake_sound = pygame.mixer.Sound("audio/wake.mp3")
                wake_sound.play()
                print("Wake word detected.")
                listen_and_respond(source)
                break
        except sr.UnknownValueError:
            pass

def listen_and_respond(source):
    print("Listening...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            if not text:
                continue
            
            waiting_sound = pygame.mixer.Sound("audio/waiting.mp3")
            waiting_sound.play()
            text_to_speech(text_gen(text))
            my_sound = pygame.mixer.Sound("audio/answer.mp3")
            my_sound.play()
            os.remove("audio/answer.mp3")
            
            if not audio:
                listen_for_wake_word(source)
                
        except sr.UnknownValueError:
            time.sleep(2)
            print("Silence found, shutting up, listening...")
            listen_for_wake_word(source)
            break
            
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            listen_for_wake_word(source)
            break

# Usage example:
with sr.Microphone() as source:
    listen_for_wake_word(source)