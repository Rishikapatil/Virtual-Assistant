from typing import Mapping
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")
    speak("Hello Mam, I am David. Please tell what can i do for you")
    print("Hello Mam, I am David. Please tell what can i do for you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rishikapatil26@gmail.com', 'Dnyaneshwar@1973')
    server.sendmail('rishikapatil26@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'play song on youtube' in query:
            song = query.replace('Play', '')
            speak('Playing' + song)
            print("Playing")
            pywhatkit.playonyt(song)

        elif 'who i am' in query:
            speak("You are talking so you are a human being")

        elif 'who are you' in query:
            speak("Mam, I am your personal assistant")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'music' in query:
            music_dir = 'C:\\Users\\rishi\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")
            print(strTime)

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open excel' in query:
            excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(excelPath)

        elif 'open powerpoint' in query:
            powerpointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(powerpointPath)

        elif 'open world' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)

        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rishikapatil26@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry mam. I am not able to send this email")

        elif 'news' in query:
            news = webbrowser.open_new_tab(
                "https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')

        elif "goodbye" in query or "okbye" in query or "stop" in query:
            speak(
                'your personal assistant is shutting down,Good bye mam we will meet soon')
            print(
                'your personal assistant is shutting down,Good bye mam we will meet soon')
            exit()
