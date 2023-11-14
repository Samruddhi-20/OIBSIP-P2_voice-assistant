import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import webbrowser

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg123 response.mp3")

# Function to listen to user's voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand your command.")
            return ""
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")
            return ""

# Main voice assistant loop
while True:
    command = listen()
    
    if "hello" in command:
        response = "Hello! How can I help you?"
        speak(response)
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        response = "The current time is " + current_time
        speak(response)
    elif "date" in command:
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        response = "Today's date is " + current_date
        speak(response)
    elif "search" in command:
        query = command.replace("search", "")
        response = "Searching the web for " + query
        speak(response)
        query = query.strip()
        search_url = "https://www.google.com/search?q=" + query
        webbrowser.open(search_url)
    elif "exit" in command:
        response = "Goodbye!"
        speak(response)
        break
