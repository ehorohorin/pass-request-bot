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



REASONS = []
REASONS.append('Посещение суда')
REASONS.append('Доставка несовершеннолетних в (из) образовательные организации')
REASONS.append('Посещение медицинской или ветеринарной организации')
REASONS.append('Участие в похоронах')
REASONS.append('Восстановление паспорта')
REASONS.append('Выезд в загородный дом или из него')
REASONS.append('Посещение кредитных организаций и почтовых отделений')
REASONS.append('Доставка лекарств, продуктов питания и предметов первой необходимости')
REASONS.append('Изменение места проживания')


reason_markup = types.ReplyKeyboardMarkup(row_width=2)
for reason in REASONS:
	itembtn = types.KeyboardButton(reason)
	reason_markup.add(itembtn)
	
contact_request_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
button = types.KeyboardButton(text='Предоставить номер телефона',request_contact=True)
contact_request_markup.add(button)
	

conf=configparser.ConfigParser()
conf.read("bot.cfg")


DEBUG="true" == get_param("main", "DEBUG")



TOKEN=get_param("telegram","TOKEN")
if not TOKEN: 
	print("Please, define the TOKEN param of bot.cfg file!")
	sys.exit()

if DEBUG:
	print("DEBUG is on!")
	print(REASONS)
	print("TOKEN %s is used for connecting" % TOKEN)


SOKS5_PROXY= get_param("telegram", "SOKS5")
if SOKS5_PROXY:
	apihelper.proxy = {"https":"socks5h://"+SOKS5_PROXY}
	if DEBUG:
		print(apihelper.proxy)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Please Chose One :', reply_markup=contact_request_markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
	if DEBUG:
		print("Command is recieved: %s" % message)
	result = "hello"
	bot.send_message(message.chat.id, result)

@bot.message_handler(content_types=['contact'])
def send_contact(message):
	print(message)
	print(message.contact)

	result = "%s %s, спасибо, номер телефона получен! +%s" % (message.contact.first_name, message.contact.last_name, message.contact.phone_number)
	result += "\n"
	result += "Для оформления электронного пропуска укажите пожалуста причину:"

	bot.send_message(message.chat.id, result, reply_markup=reason_markup)

bot.polling()

