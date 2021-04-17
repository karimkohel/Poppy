from datetime import datetime
import requests
import random
import webbrowser

import speech

def getTime(intent):
    time = datetime.now().time()
    time = time.strftime("%I:%M %p")
    speech.speak("It's " + time)

def getWeather(intent):
    api = 'http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=04a716d70b54bf5c6c24dbb3dfa5db03&units=metric'
    allData = requests.get(api).json()
    weather = allData['weather'][0]['description']
    temp = allData['main']['temp']
    speech.speak(weather, ", ", temp)

def takeNotes(intent):
    speech.speak("Ready to take your notes")
    note = speech.takeCommand()
    with open("note.txt", 'a') as f:
        f.write(note)
        f.write("\n---------------------\n")
    speech.speak("Ok done")

def search(intent):
    speech.speak(intent)
    searchTopic = speech.takeCommand()
    speech.speak("This is what i found for " + searchTopic)
    webbrowser.open('http://google.com', new=2)
    # implement search feature with front end
    # by learning google api

def close(intent):
    speech.speak(intent)
    exit(0)


mappings = {
    'time' : getTime,
    'weather' : getWeather,
    'note' : takeNotes,
    'goodbye': close
}
