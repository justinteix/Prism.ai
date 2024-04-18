from openai import OpenAI
import warnings
import os
from dotenv import load_dotenv
warnings.filterwarnings("ignore", category=DeprecationWarning)
load_dotenv()

def text_gen(question):
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful voice assistant. Keep your answers brief and no more than 30 seconds long."},
        {"role": "user", "content": question}
    ],
    )
    
    return response.choices[0].message.content

def text_to_speech(text_question):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    speech_file_path = "./answer.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="fable",
    input=text_question
    )
    
    response.stream_to_file(speech_file_path)


def speech_to_text(filename):
    client = OpenAI()

    audio_file= open(filename, "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
    )
    answer = transcription
    return answer


print(speech_to_text("./answer.mp3"))