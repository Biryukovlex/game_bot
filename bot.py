# -*- coding: utf-8 -*-

import telebot
import parser
from telebot.types import Message
from telegram import *
import imagedb
import urllib
import os
import random
import config
import status

TOKEN = 'put_your_token_here'

bot = telebot.TeleBot(TOKEN)

PATH = '/Users/alexanderbiryukov/Desktop/Coding/Bot_project/bot/documents/'

def send_pic(message):
	with open(f'{PATH}/kukerech.jpg', 'rb') as f:
		vassal = f.read()
		bot.send_photo(message.chat.id, vassal)

def add_player(player):
	try:
		os.mkdir(PATH+f'{player}')
	except OSError:
		return False
	else:
		return True


@bot.message_handler(commands=['start', 'help'])
def command_handler(message):
	bot.reply_to(message, 'Приветики -  пистолетики')

@bot.message_handler(commands=['add_vassals'])
def add_vassals(message: Message):
	if status.get_status(message.chat.id) == False:
		status.add_status(message.chat.id, '1', '0')
	else:
		status.update_status(message.chat.id, '1')
	bot.send_message(message.chat.id, text="Напиши имя противника")

@bot.edited_message_handler(content_types=['text'])
@bot.message_handler(content_types=['text'])
def start_handler(message: Message):
	if status.get_status(message.chat.id) == False:
		status.add_status(message.chat.id, '0', '0')
	if 'Привет' in message.text and status.get_status(message.chat.id) == '0':
		bot.reply_to(message, 'Привет, меня зовут Кукереч! Я личный бот лучшей гильдии на свете!')
	elif ('Покажи себя' or 'Покажись' in message.text) and status.get_status(message.chat.id) == '0':
		send_pic(message)
	elif status.get_status(message.chat.id) == '1':
		add_player(message.text)
		status.update_name(message.chat.id, f'{message.text}')
		bot.reply_to(message, 'Теперь пришли картинку')
		status.update_status(message.chat.id, '0')
	else:
		bot.reply_to(message, 'Не понял')
		

@bot.message_handler(content_types=['photo'])
def get_pic(message):
	try:
		#Подготовили файл
		file_name = message.photo[-1].file_id
		file_info = bot.get_file(message.photo[-1].file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		save_dir = status.get_name(message.chat.id)
		if add_player(save_dir):
			bot.send_message(message.chat.id, f'Добавил нового игрока {save_dir}')
		else:
			bot.send_message(message.chat.id, f'Буду сохранять в {save_dir}')
		src = file_name
		path_to_file = PATH+f'{save_dir}/{src}'
		with open(path_to_file, 'wb') as new_file:
			new_file.write(downloaded_file)
		config.push_player_pics(save_dir, file_name, path_to_file)
		bot.send_message(message.chat.id, f'Сохранил в {save_dir}')
		status.update_name(message.chat.id, '0')
	except Exception as ex:
		bot.send_message(message.chat.id, "[!] error - {}".format(str(ex)))
	
bot.polling()