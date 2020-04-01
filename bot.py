#!/usr/bin/python 

import sys
import telebot
import urllib.request
from telebot import apihelper
from telebot import types
import configparser


def get_param(section, option):
	try:
		result = conf.get(section, option)
	except (configparser.NoOptionError, configparser. NoSectionError):
		result=0

	return result


	

conf=configparser.ConfigParser()
conf.read("bot.cfg")


DEBUG="true" == get_param("main", "DEBUG")


TOKEN=get_param("telegram","TOKEN")
if not TOKEN: 
	print("Please, define the TOKEN param of bot.cfg file!")
	sys.exit()

if DEBUG:
	print("DEBUG is on!")
	print("TOKEN %s is used for connecting" % TOKEN)


SOKS5_PROXY= get_param("telegram", "SOKS5")
if SOKS5_PROXY:
	apihelper.proxy = {"https":"socks5h://"+SOKS5_PROXY}
	if DEBUG:
		print(apihelper.proxy)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('Посещение суда')
	itembtn2 = types.KeyboardButton('Доставка несовершеннолетних в (из) образовательные организации')
	itembtn3 = types.KeyboardButton('Посещение медицинской или ветеринарной организации')
	itembtn4 = types.KeyboardButton('Участие в похоронах')
	itembtn5 = types.KeyboardButton('Восстановление паспорта')
	itembtn6 = types.KeyboardButton('Выезд в загородный дом или из него')
	itembtn7 = types.KeyboardButton('Посещение кредитных организаций и почтовых отделений')
	itembtn8 = types.KeyboardButton('Доставка лекарств, продуктов питания и предметов первой необходимости')
	itembtn9 = types.KeyboardButton('Изменение места проживания')
	markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9)
	bot.send_message(message.chat.id, 'Привет, для оформления электронного пропуска укажите пожалуйста причину:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
	if DEBUG:
		print("Command is recieved: %s" % message)
	result = "hello"
	bot.send_message(message.chat.id, result)

bot.polling()

