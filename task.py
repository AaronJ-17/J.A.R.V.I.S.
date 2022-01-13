from pxsr import *
from ledconfig import *
import datetime
import os
from play import *
import webbrowser
import speedtest
import pyautogui
from time import *
import wikipedia
import pyjokes
from pywikihow import *
from urllib.request import url2pathname
import sys
import psutil
import requests

#for greeting
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning sir!")
    elif hour>12 and hour<18:
        speak("good afternoon sir!")
    else:
        speak("good evening sir!")
    speak("how may i help you?")
#for time
def time():
    strTime = datetime.datetime.now().strftime("%H:%M")
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<= 12:
        speak(f"it's {strTime} A.M")
        speak("have a good day sir.")
    elif hour>= 12 and hour<= 18:
        speak(f"it's {strTime} P.M")
    else:
        speak(f"it's {strTime} P.M")
#for going out
def going():
    query = takecommand()
    speak("where are you going sir?")
    td = takecommand()
    speak("oh ok come back soon i will be waiting for you!")
    if "i am back" in query or "where did i stop" in query:
        speak("aaaahhhhh i was waiting for you sir.")
        speak(f"did you finish doing: {td}")
    elif "yup" in query:
        speak("nioce")
    else:
        speak("ohhh ok sir.")
#for news update
def news():
        main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=ba410dbe8663498d955f70ebad3cd4e4'

        main_page = request.get(main_url).json()
        articles = main_page["articles"]
        head = []
        day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range(len(day)):
            speak(f"today's {day[i]} news is: {head[i]}")
#for task
def task():
        wish()
        while True:
            query = takecommand()

            #generl talk
            if "hai" in query or "hi" in query or "hey" in query or "sup" in query:
                speak("hello sir.")
                time()
                speak("how may i help you?")
            elif "how are you" in query or "what about you" in query:
                speak("i am always fine")
                speak("anyways thank you for asking")
            elif "how is life" in query:
                speak("how can life be better than this")
                speak("lol")
                speak("how is your day going sir ?")
            elif "good" in  query or "not bad" in query or "fine" in query:
                speak("good to hear from you!")
                speak("hope you will have always have good days")
            elif "bad" in query or "worst" in query:
                speak("oh , sad to hear for you sir")
                speak("hope you will have a nice day tomorrow....")
            elif "coming" in query or "will be back" in query or "i have to go" in query:
                going()
            elif "thank you" in query or "thanks" in query:
                speak("never mention it")
            elif "bye" in query or "buy" in query or "break" in query:
                speak("ok then....... it was nice talking and working for you")
                speak("addioss")
                break;
            #introduction
            elif "what are you" in query or "who are you" in query or "introduce" in query or "what is your name" in query:
                speak("I am Jarvis. a virtual assistant")
                speak("and i am here to help you with a variety of task which i can do the best")
                speak("i will be available 24 hours a day and 7 days a week if i am powered on...... lol!")
                speak("so , how may i help you?")
            #time
            elif "time" in query or "Time" in query:
                time()
            #shutting down the system
            elif "shut down" in query or "shutdown" in query or "power off" in query or "poweroff" in query or "power of" in query or "powerof" in query:
                speak("ok then sir.... it was nice talking and working for you")
                speak("adios")
                os.system("init 0")
            #rebooting the system
            elif "reboot" in query or "Reboot" in query:
                speak("oh ok.... 1 sec")
                os.system("init 6")
            #upgrading the system
            elif "update" in query or "upgrade" in query:
                speak("will do....")
                os.system("sudo apt-get update")
                os.system("sudo apt-get upgrade -y")
                speak("the lastest update is installed in your computer.... rebooting the computer is recommended")
            #playing a song
            elif "play" in query:
                query = query.replace("play","")
                speak("as you wish")
                play(query)
                speak(f"playing: {query}")
            #my likes
            elif "likes" in query or "life" in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<=12:
                    speak("sure sir! working on it!")
                    lm = 'https://www.youtube.com/watch?v=EmRwe-oY3VQ'
                    play(lm)
                elif hour>12 and hour<18:
                    speak("working on it!")
                    lm = 'https://www.youtube.com/watch?v=lRa-lrUeyJY'
                    play(lm)
                else:
                    speak("copy that!")
                    lm = 'https://www.youtube.com/watch?v=ziWPOQs-QCw'
                    play(lm)
            #youtube
            elif "youtube search how to" in query:
                speak("will do")
                query = query.replace("youtube search","")
                yt = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(yt)
                speak(f"playing {query}")
            #maths
            elif "calculator" in query or "calculate" in query:
                speak("sir what should i calculate?")
                speak("tell the first number")
                num = takecommand()
                speak("tell the operator")
                oper = takecommand()
                speak("tell me the second number")
                num_2 = takecommand()
                if oper == "+" or oper == "plus":
                    ans_1 = (num + num_2)
                    speak("your result is:")
                    speak(ans_1)
                elif oper == "-" or oper == "subtract":
                    ans_2 = (num - num_2)
                    speak("your result is:")
                    speak(ans_2)
                elif oper == "*" or oper == "multiply":
                    ans_3 = (num * num_2)
                    speak("your result is:")
                    speak(ans_3)
                else:
                    ans_4 = (num / num_2)
                    speak("your result is:")
                    speak(ans_4)
            #ip address
            elif "ip address" in query:
                ip = request.get('https://api.ipify.org').text
                speak(f"your ip address in {ip}")
            #google search
            elif "google" in query or "Google" in query:
                speak("sir, what shoud i search on google")
                cm = takecommand().lower()
                webbrowser.open(f"https://google.com/search?q=" + cm)
                speak(f"sir wait for 2 second, searching for {cm}...")
            #google search advanced
            elif "show me" in query:
                speak("as you wish")
                query = query.replace("jarvis","")
                query = query.replace("show me","")
                sm = 'https://google.com/search?q=' + query
                webbrowser.open(sm)
                speak(f"opening google to show you {query}")
            #google search advanced
            elif "i want to see" in query:
                speak("on it")
                query = query.replace("jarvis","")
                query = query.replace("i want to see","")
                sm = 'https://google.com/search?q=' + query
                webbrowser.open(sm)
                speak(f"opening google to show you {query}")
            #open websites
            elif "open" in query:
                speak("on it")
                query = query.replace("jarvis","")
                query = query.replace("open","")
                webbrowser.open(f"https://google.com/search?q=" + query)
                speak("sir wait for 2 second, opening " + query)
           #for speedtest
            elif "internet speed test" in query:
                speak("why not?")
                speak("lol")
                st = speedtest.Speedtest()
                dl = st.download()/1000000
                up = st.upload()/1000000
                speak(f"sir we have {dl} Mbps dowloading speed....")
                speak(f"and {up} Mbps uploading speed....")
            #to switch the window
            elif "switch the window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab") 
                sleep(1)
                pyautogui.keyUp("alt")
                speak("switching the window")
            #to switch the window
            elif "close the tab" in query:
                pyautogui.keyDown("Ctrl")
                pyautogui.press("W") 
                sleep(1)
                pyautogui.keyUp("Ctrl")
                speak("closing the tab")
            #to switch the window
            elif "close the window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("F4") 
                sleep(1)
                pyautogui.keyUp("alt")
                speak("closing the window")
            #wikipedia
            elif 'wikipedia' in query:
                speak("searching wikipedia")
                query = query.replace("jarvis","")
                query = query.replace("wikipedia","")
                wiki = wikipedia.summary(query,2)
                speak("accrording to wikipedia : ")
                speak({wiki})
            #jokes
            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)
            #news
            elif "tell me the news" in query:
                speak("please wait sir, feteching the latest news")
                news()
            #for finding location
            elif "where am i" in query or "location" in query or "where are we" in query:
                    speak("wait sir, let me check")
                    ipAdd = request.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = get('https://get.geojs.io/v1/ip/geo/59.93.250.207.json').text
                    geo_requests = request.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} in {state} of {country}")
            #remebering
            elif "remember" in query:
                rememberMsg = query.replace("remember that","")
                rememberMsg = rememberMsg.replace("jarvis", "")
                speak("the reminder is:" + rememberMsg)
                remeber = open('data.txt','w')
                remeber.write(rememberMsg)
                remeber.close()
            #reminder
            elif "do I have" in query:
                with open('data.txt') as f:
                    lines = f.read()
                    speak(f"sir you told me to remember this: {lines}")
            #power
            elif "how much power we have" in query or "how much power left" in query or "battery" in query:
                battery = psutil.sensors_battery()
                percentage = battery
                speak(f"sir our system have {percentage} percent battery")
            #screenshot
            elif "take screenshot" in query or "take a screenshot" in query:
                speak("sir, please tell me the name for this screenshot file")
                name = takecommand().lower()
                speak("please sir hold the screen for 2 second, i am taking a screenshot")
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder")
            #how to mod
            elif "how to" in query:
                how = query.replace("how to","how to")
                max_result = 1
                lang = 'en'
                how_to = search_wikihow(how,max_result,lang)
                speak(how_to[0].summary)
