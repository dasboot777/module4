# 25.12.2022

from utils import welcome_keyboard, get_random_photo, BASE_FILES_PATH, poem_keyboard, sovet_keyboard
# импорт функций из отдельного файла
# бот-ретранслятор
import random
from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

bot = TeleBot(token="5978902105:AAFeledAflrmiOTp-a6ZucG6BoVvVDkVS0o")


#аннотация типов
@bot.message_handler(commands=["start", "help"])  # декоратор
def welcome(message: Message):
    keyboard = welcome_keyboard()# вызваем созданную клаву
    bot.send_message(message.from_user.id, "Привет, выбери себе..", reply_markup=keyboard)  # отправл сообщ: кому отправляем, сам текст, указ клав-ру

@bot.message_handler(commands=["cats"])  # декоратор
def cats(message: Message):
    random_img = get_random_photo()

    bot.send_photo(message.from_user.id, random_img)

@bot.message_handler(commands=["music"])  # декоратор
def music(message: Message):
    audio = open(fr"{BASE_FILES_PATH}\happy.mp3", "rb")  # открывыаем случайны файл, rb - read bytes - режим чтения
    bot.send_audio(message.from_user.id, audio)

@bot.message_handler(commands=["poem"])  # декоратор
def poem(message: Message):
    keyboard = poem_keyboard()
    bot.send_message(message.from_user.id, "Села муха на вариенье", reply_markup=keyboard)


@bot.message_handler(commands=["sticker"])
def sticker(message: Message):
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEHLBVjuq8sJLaNzzFZGW1_o5f5DPJKxQACHSYAAvBkKElgG1EAARdJBGAtBA")


@bot.message_handler(commands=["sovet"])
def sovet(message: Message):
    keyboard = sovet_keyboard()
    bot.send_message(message.from_user.id, "Выберите игру:", reply_markup=keyboard)


bot.polling()  # запуск
