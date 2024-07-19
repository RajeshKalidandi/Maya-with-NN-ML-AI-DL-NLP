import datetime
from speak import say
import wikipedia
import pywhatkit
import webbrowser

def Time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    say(time)

def Date():
    date = datetime.date.today()
    say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    say(day)

def NonInput(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()


def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("Who is","").replace("about","").replace("What is","").replace("wikipedia","")
        result = wikipedia.summary(name)
        say(result)

    elif "google" in tag:
        query = str(query).replace("google","").replace("search","")
        pywhatkit.search(query)

    elif "youtube" in tag:
        query = query.replace("youtube search","")
        query = query.replace("Maya","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)

    elif "website" in tag:
        query = query.replace("maya","")
        query = query.replace("website","")
        web1 = query.replace("open","")
        web2 = 'https://www.' + web1 + '.com'
        webbrowser.open(web2)
        



        


    