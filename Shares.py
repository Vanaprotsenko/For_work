from response.response import *
import json
import random
import requests
from bs4 import BeautifulSoup
import pyttsx3
from response.response import *
import main

tts_engine = pyttsx3.init()


def film_in_cinema(voice_input):

        result = requests.get('https://planetakino.ua/ru/movies/',headers={'Accept':'*/*','User-agent':'d'})
        soup = BeautifulSoup(result.text,'html.parser')
        count = 4
        share = soup.findAll('div',{'class':'movie-block__mobile-name'})
        for i in range(count):
            tts_engine.say(share[i].text.split('-')[0])

        pharse_list.append(Type_pharse([
            'фильмы'
        ],film_in_cinema))



