import telebot
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot('5850667236:AAG1iZs_cECbmjzRwDyJLdfFGIYB38l9vCs')
@bot.message_handlers(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Бомбооомэ🦍🦧')
@bot.message_handlers(content_type=['text'])
def handle_text(message):
    bot.send_message(message.chat.id,'BimBim: ' + message.text)
bot.polling()
