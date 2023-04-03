from response.response import *
import json
import random
import requests
from bs4 import BeautifulSoup
import pyttsx3
from response.response import *
import main

tts_engine = pyttsx3.init()



result = requests.get('https://www.atbmarket.com/promo/economy',headers={'Accept':'*/*','User-agent':'d'})
soup = BeautifulSoup(result.text,'html.parser')





share = soup.find('div',{'class':'catalog-item__title wbh-14'}).next_element.next_element.next_element

print(share)
