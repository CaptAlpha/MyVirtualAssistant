import pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib


print("Intializing")

MASTER = "Arhit"
#speak function speak the text input
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Initializing Virtual Assistant....")

def wishMe():

    hour = int(datetime.datetime.now().hour)
    
    if hour>=12 and hour<12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<18:
        speak("Good afternoon" + MASTER)
    else:
        speak("Good evening" + MASTER)
wishMe()
speak("Hello")

#Main Programme:

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")
    except Exception as e:
        print("I did'nt get you")
        speak("I did'nt get you")
        query = None
    return query

query = takeCommand()
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls('emailid@gmail.com', 'password@gmail.com')
    server.sendmail('emailid@gmail.com',to, content)
    server.close()

#Logic For Execution
if 'wikipedia' in query.lower():
    speak("Searching Wikipedia")
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences =2)
    speak(results)
    print(results)
elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")
   
elif 'open google' in query.lower():
     webbrowser.open("google.com")
elif 'open whatsapp' in query.lower():
     webbrowser.open("https://web.whatsapp.com/")
elif 'the time' in query.lower():
    strTime =datetime.datetime.now().strftime("%H:%M:%S")
    speak("The time is {}".format(strTime))
    print("The time is {}".format(strTime))
elif 'open code' in query.lower():
    codePath = "C:\\Users\\Arhit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
elif 'email' in query.lower():
    try:
        speak("Please state your content")
        content = takeCommand()
        to = "emailid@gmail.com"
    except Exception as e:
        print(e)
