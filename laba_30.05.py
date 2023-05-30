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
    else:
        print(False)
bot = telebot.TeleBot('6108076129:AAFig6WPxWSPiTmOreXd8jGXQRTxwtyRyvY')
@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Доллар')
    item2 = types.KeyboardButton('Євро')
    item3 = types.KeyboardButton('Злоти')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, 'Натисни кнопку', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def handler_text(message):
    if message.text.strip() == 'Доллар':
        answer = course1
    elif message.text.strip() == 'Євро':
        answer = course2
    elif message.text.strip() == 'Злоти':
        answer = course3
    bot.send_message(message.chat.id,answer)
bot.polling()
