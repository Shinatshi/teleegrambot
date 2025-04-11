import cfg
import random
import telebot
from telebot import types
from random import choice
API_TOKEN = cfg.TOKEN
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
  
  keyboard = types.ReplyKeyboardMarkup(row_width=2)
  button1 = types.KeyboardButton('Ничего не делать')
  button2 = types.KeyboardButton('Монетка')
  keyboard.add(button1,button2)

  bot.reply_to(message, 'Привет! Я бот.', reply_markup=keyboard)
    
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Вот список команд:\n/start - запуск бота\n/help - список команд")



@bot.message_handler(content_types=['text', 'photo', 'sticker'])
def handle_message(message):
    if message.text and message.text.lower()== 'привет':
      bot.send_message(message.chat.id, 'Привет! Как дела?')

    if message.photo:
        file_id = message.photo[-1].file_id
        bot.send_photo(message.chat.id, file_id, caption='Фото')

    if message.text == 'Ничего не делать':
        bot.reply_to(message, 'Вы ничего не сделали')

    if message.sticker:
      bot.send_message(message.chat.id, 'Вы отправили стикер.')

    if message.text and message.text.lower()== 'нормально':
       bot.send_message(message.chat.id, 'Ок')
       
    if message.text and message.text.lower()== 'пока':
       bot.send_message(message.chat.id, 'До встречи')

    if message.text == 'Монетка':
        coin = choice(["ОРЕЛ", "РЕШКА"])
        bot.reply_to(message, coin)

bot.infinity_polling()