import telebot
from telebot import types
import random
from bs4 import BeautifulSoup
import requests
f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
t = open('thinks.txt', 'r', encoding='UTF-8')
thinks = t.read().split('\n')
t.close()
bot = telebot.TeleBot('5850667236:AAG1iZs_cECbmjzRwDyJLdfFGIYB38l9vCs')
@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Факт')
    item2 = types.KeyboardButton('Приказка')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Натисни кнопку', reply_markup=markup)

# def start_message(message):
#     bot.send_message(message.chat.id,'Бомбооом🦍🦧')
@bot.message_handler(content_types=['text'])
def handler_text(message):
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    elif message.text.strip() == 'Приказка':
        answer = random.choice(thinks)
    bot.send_message(message.chat.id,answer)
bot.polling()
