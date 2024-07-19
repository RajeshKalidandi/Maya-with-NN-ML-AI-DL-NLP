import pyttsx3
import datetime


def say(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate',170)
    print(f"Maya :{text}")
    engine.say(text=text)
    engine.runAndWait()
    print(" ")


def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning Boss !")

    elif hour>=12 and hour<15:
        say("Good Afternoon Boss !")

    elif hour>=15 and hour<18:
        say("Good Evening Boss !")
    else:
        say("Good Night Boss!")

    say("Welcome Back Boss , I am Maya . Your AI Personal Assistant !!")
    print(f"      ")
    say("Please tell me how may I help you !!")

if __name__ == "__main__":
    Wishme()
 
