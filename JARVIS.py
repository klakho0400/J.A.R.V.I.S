from gtts import gTTS
from urllib.request import urlopen
import os
import requests
import json
import speech_recognition as sr 
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import random
import urllib.request
import pandas as pd
import re
import webbrowser
import smtplib
import string
def rps():
    b = True
    while b:
        speak("starting rock paper scissors")
        speak("rock paper scissor shoot")
        f = inputlisten()
        c = random.randint(1,3)
        print(c)  
        if(('rock' in f and c == 1) or ('scissor' in f and c==3) or ('paper' in f and c==2)):
            speak('Draw')
        elif(('rock' in f and c==3) or ('scissor' in f and c==2) or ('paper' in f and c==1)):
            speak('You Win')
        elif(('rock' in f and c==2) or ('scissor' in f and c==1) or ('paper' in f and c==3)):
            speak('You Lose')
        else:
            speak('ERROR speak again')
        speak('would you like to continue')
        ans = inputlisten()
        if('yes' not in ans):
            b = False
def sevenupdown():
    coins = 50 
    b = True
    while b:
        speak("Starting seven up seven down ")
        speak("choose 7up ,7down or 7")
        p = inputlisten()
        speak('you chose '+p)
        speak("rolling the dices")
        a=random.randint(2,12)
        speak('the number is '+str(a))
        if((a < 7 and '7down' in p) or  (a>7 and '7up' in p)):
            speak("you won 20 coins")
            coins+=20
        elif(a == 7 and p == '7'):
            speak("you won 30 coins")
            coins+=30
        else:
            speak("better luck next time")
            coins-=10
        speak('would you like to continue')
        ans = inputlisten()
        if('yes' in ans):
            b = False
def play():
    reg_ex = re.search('play (.+)', command)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.youtube.com'+'/results?search_query='+domain
        webbrowser.open(url)
        print('Done!')
    else:
        pass
def askfortask():
    mytext = 'What can I do for you sir'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("welcome1.mp3") 
    os.system("mpg321 welcome1.mp3")
    print('!weather,!time','!date','!corona','!bye','!open website')
def speak(strr):
    mytext = strr
    print(mytext)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("welcome2.mp3") 
    os.system("mpg321 welcome2.mp3")
def listentome():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am listnening .... ')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = listentome()

    return command
def inputlisten():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am listnening .... ')
        r1.pause_threshold = 1
        r1.adjust_for_ambient_noise(source, duration=1)
        audio = r1.listen(source)
    try:
        c = r1.recognize_google(audio).lower()
        print('You said: ' + c + '\n')
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        c = listentome()

    return c
def weather():
    api_key = "aa425dca334316d164048c7ad4216fab"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("which city are you in ?")
    city_name = inputlisten()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"] 
        z = x["weather"]
        weather_description = z[0]["description"] 
        speak(" Temperature in "+city_name +"is" +
                        str(int((int(current_temperature)-273.15))) +"degree celsius "+
            "and the humidity is about " +
                        str(current_humidiy) + "percent"
            "\n you are looking for " +
                        str(weather_description) +"today") 
    else: 
        speak(" City Not Found ") 
def time():
    x = datetime.datetime.now().strftime("%H:%M:%S")
    speak(str(x))
def date():
    x = datetime.datetime.now().strftime("%d:%m:%Y")
    speak(str(x))
def findcases():
    main_url = 'https://www.mohfw.gov.in/'
    result = requests.get(main_url).content
    # parse the html content
    soup = BeautifulSoup(result, "html.parser")
    extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
    # find all table rows and data cells within
    stats = [] 
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract_contents(row.find_all('td')) 
        if len(stat) == 5:
            stats.append(stat)
    new_cols = ["Sr.No", "States/UT","Confirmed","Recovered","Deceased"]
    state_data = pd.DataFrame(data = stats, columns = new_cols)
    state_data['Confirmed'] = state_data['Confirmed'].astype(int)
    print(sum(state_data['Confirmed']))
    speak(str(sum(state_data['Confirmed'])))
def openreddit():
    reg_ex = re.search('open reddit (.*)', command)
    url = 'https://www.reddit.com/'
    if reg_ex:
        subreddit = reg_ex.group(1)
        url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
def openweb():
    reg_ex = re.search('open (.+)', command)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain + '.com'
        webbrowser.open(url)
        print('Done!')
    else:
        pass
def email():
    speak("who is the recipient?")
    recp = input()
    speak('enter the message')
    message = input()+'\n\n\n\n This Message was sent using JARVIS'
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls() 
    s.login("xyz@gmail.com", "pass") 
    s.sendmail("xyz@gmail.com",recp, message) 
    s.quit()
    speak('mail sent')
def takenotes():
    f= open("notes.txt","w+")
    speak("what should i note?")
    pl = inputlisten()
    f.write(pl)
    f.close()
def readnotes():
    speak("reading the notes")
    f = open("notes.txt",'r')
    contents =f.read()
    speak(contents)
def search(key):
    try:
        key = string.capwords(key)
        key = key.replace(' ','_')
        url = 'https://en.wikipedia.org/wiki/'+key
        print(url)
        html = urlopen(url) 
        desc =[]
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.select(".mw-parser-output p"):
            desc.append(item.text)
        speak(desc[1])
    except:
        speak('i am not able to find what you are looking for')

if __name__ == '__main__':
    speak("JARVIS initialising    ")
    hour = int(datetime.datetime.now().hour)
    if( hour>= 5 and hour < 12):
        speak("Good Morning Sir")
    elif(hour >= 12 and hour <16):
        speak("Good Afternoon Sir")
    elif(hour >= 16 and hour <= 23):
        speak("Good Evening Sir")
    while(1): 
        askfortask()
        command = listentome()
        if('weather' in command):
            weather()
        elif('7 up 7 down' in command):
            sevenupdown()
        elif('play' in command):
            play()
        elif('time' in command):
            time()
        elif('date' in command):
            date()
        elif('bye' in command or 'adios' in command or 'nothing' in command or 'hasta la vista' in command):
            speak('Bye sir!')
            break
        elif('corona' in command):
            findcases()
        elif('open ' in command):
            openweb()
        elif('reddit' in command):
            openreddit()
        elif('who are you' in command or 'your name' in command):
            speak('I am JARVIS I was created by Kshitiz ')
        elif('thank you' in command):
            speak('I am just doing my duty!')
        elif('pick a number' in command):
            speak(str(random.randint(1,100)))
        elif('rock paper scissor' in command):
            rps()
        elif('dice' in command):
            speak(str(random.randint(1,6)))
        elif('coin' in command):
            speak('Heads' if random.randint(1,2)==1 else 'Tails')
        elif('take notes' in command):
            takenotes()
        elif('read notes' in command):
            readnotes()
        elif('email' in command):
            email()
        elif('simon says' in command):
            s = list(command.split())
            s = s[2:]
            speak(str(s))
        elif('who is' in command or 'what is' in command or 'search for' in command):
            key = command[7:]
            search(key)
        else:
            speak("sorry i am still developing!")