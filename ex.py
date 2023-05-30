import telebot
from telebot import types
import random
from bs4 import BeautifulSoup
import requests

response = requests.get('https://minfin.com.ua/ua/currency/')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for script in soup.find_all(['p']):
        script.extract()
    courses = soup.find_all('div', {'class': 'sc-1x32wa2-9 bKmKjX'})
    if courses:
        course1 = courses[0]
        course2 = courses[3]
        course3 = courses[6]
        print(course1.text.strip())
        print(course2.text.strip())
        print(course3.text.strip())
    else:
        print(False)