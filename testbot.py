# import config as cfg

import telebot

# from telebot import apihelper
# apihelper.proxy = {'http':'https://antizapret.prostovpn.org/proxy.pac'}

bot = telebot.TeleBot("644641882:AAFFlWw2nDcLpzdG5NCY42TUDAAGr24WOxk")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
