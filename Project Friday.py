from ssl import SSL_ERROR_INVALID_ERROR_CODE
from urllib.parse import DefragResultBytes
import pyttsx3
import webbrowser
import os
import datetime
import wikipedia
import speech_recognition as sr
from wikipedia.wikipedia import summary
from youtube_search import YoutubeSearch
from googlesearch import search 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()




    


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good evening!")
        speak("Hello Sir This is Your Assistant. How can I help You?")


def takeCommand():
    #It takes microphone input from user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    
    return query


if __name__ == "__main__":
    wishme()
    while(True):
        query = takeCommand(). lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = (query).replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            speak(results)
            print(results)

        
        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open('google.co.in')

        elif 'open music' in query:
            pass


        elif 'stop listening' in query:
            speak('ok sir, I am out now.')
            break


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}.")

        elif 'open browser' in query:
            browser_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(browser_path)

    
        
        elif 'on youtube' in query:
            print(query)
            query = query.replace(' on youtube', '')
            query = query.replace('play ', '') 
            results = YoutubeSearch(query, max_results=1).to_json()
            results = results.split('url_suffix', maxsplit=-1)
            url_raw = results[-1]
            url = url_raw.replace('": "',"")
            url = url.replace('"}]}', "")
            print(url)
            webbrowser.open("www.youtube.com" + url)

        # elif 'on google' in query:
        #     query = query.replace("on google", "")
        #     query = query.replace("search", "")
        #     for j in search(query, tld="co.in", num=1, stop=1): 
        #         webbrowser.open(j)




