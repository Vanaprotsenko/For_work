import pyttsx3
from response.response import *
import random
import requests
import json
from bs4 import BeautifulSoup
import re


tts_engine = pyttsx3.init()

voice = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voice[2].id)


def hello_response(voice_input):
    tts_engine.say("Привет")

pharse_list.append(Type_pharse([
    'привет','добрый день','здраствуйте','хай'
],hello_response))

def name_response(voice_input):
    list_response = [
        'я карл','я думал вы знаете как меня зовут','карл к вашим услугам '
    ]
    res = random.choice(list_response)
    tts_engine.say(res)

pharse_list.append(Type_pharse([
    'как тебя зовут','твоё имя','как тебя называют'
],name_response))


def how_you_response(voice_input):
     tts_engine.say("все отлично, а у тебя")
    

pharse_list.append(Type_pharse([
    'как ты','как дела','как настроение','как у тебя настроение','как с настроением'
],how_you_response))


def answer_to_response(voice_input):
    
     tts_engine.say("Чем я могу помочь тебе")


pharse_list.append(Type_pharse([
        'у меня есть проблема','все хорошо','не очень погода плохая'
    ],answer_to_response))


def whether(voice_input):
    resultt = requests.get("https://sinoptik.ua/")
    soup = BeautifulSoup(resultt.text,'html.parser')
    date = soup.find('p',{'class':'date'}).next_element
    min = soup.find('div',{'class':'min'}).next_element.next_element.next_element
    max = soup.find('div',{'class':'max'}).next_element.next_element.next_element
    tts_engine.say(f"Дата {date} марта минимальная температура{min}а максимальная{max}")


pharse_list.append(Type_pharse([
    'какая погода в киеве'
],whether))


def what_clothes(voice_input):
    list_clothes = [
        'джинсы  футболка и кофту'
    ]
    re = random.choice(list_clothes)
    tts_engine.say(re)

pharse_list.append(Type_pharse([
    'что мне надеть','какой стиль ты мне посоветуешь'
],what_clothes))



def course_value(voice_input):
    result = requests.get("https://api.monobank.ua/bank/currency")
    res =json.loads(result.text)
    out = (res[0]['rateBuy'])
    tts_engine.say(f"Покупка доллара по {out}")
    

pharse_list.append(Type_pharse([
    'курс валюты','можешь открыть курс валют'
],course_value))


def news_response(voice_input):
   result = requests.get("https://www.bbc.com/ukrainian")
   soup = BeautifulSoup(result.text,'html.parser')
   news = soup.find('a',{'class':'focusIndicatorDisplayInlineBlock'}).next_element
   tts_engine.say(news.text)


pharse_list.append(Type_pharse([
    'новости',

],news_response))


def film(voice_input):
    result = requests.get("https://rezka.ag/?filter=watching&genre=2",headers={'Accept':'*/*','User-agent':'d'})
    soup = BeautifulSoup(result.text,'html.parser')
    
    if 'сериалы' in voice_input:
        count = 5
        series = soup.findAll('div',{'class':'b-content__inline_item-link'})
        for i in range(count):
            tts_engine.say(series[i].text.split('-')[0])

    else:
        pattern = random.randint(0,30)
        series = soup.findAll('div',{'class':'b-content__inline_item-link'})[pattern]
        tts_engine.say(series.text.split('-')[0])


pharse_list.append(Type_pharse([
    'сериал'
],film))
    


