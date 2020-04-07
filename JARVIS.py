from gtts import gTTS
import os
import requests
import json
import speech_recognition as sr
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import random
import pandas as pd
import re
import webbrowser
import smtplib
def askfortask():
    mytext = 'What can I do for you Kshitiz'
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
def weather():
    api_key = "aa425dca334316d164048c7ad4216fab"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name : ") 
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
while(1):
    askfortask()
    command = listentome()
    if('weather' in command):
        weather()
    elif('time' in command):
        time()
    elif('date' in command):
        date()
    elif('bye' in command or 'adios' in command):
        break
    elif('corona' in command):
        findcases()
    elif('open ' in command):
        openweb()
    elif('reddit' in command):
        openreddit()
    elif('who are you' in command or 'your name' in command):
        speak('I am JARVIS  was created by Kshitiz ')
    elif('thank you' in command):
        speak('I am just doing my duty!')
    elif('pick a number' in command):
        speak(str(random.randint(1,100)))
    elif('dice' in command):
        speak(str(random.randint(1,6)))
    elif('coin' in command):
        speak('Heads' if random.randint(1,2)==1 else 'Tails')
    else:
        speak("sorry i am still developing!")