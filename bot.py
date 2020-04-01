#!/usr/bin/python 

import sys
import telebot
import urllib.request
from telebot import apihelper
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
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
	if DEBUG:
		print("Command is recieved: %s" % message)
	result = "hello"
	bot.send_message(message.chat.id, result)

bot.polling()

