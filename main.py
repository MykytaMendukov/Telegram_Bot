import telebot
from telebot import types
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
def start_message(message):
    bot.send_message(message.chat.id,'Бомбооом🦍🦧')
@bot.message_handler(content_types=['text'])
def handler_text(message):
    bot.send_message(message.chat.id, 'BimBim: ' + message.text)
bot.polling()
