# 25.12.2022

from utils import welcome_keyboard, sovet1_keyboard, sovet2_keyboard, sovet3_keyboard, sovet4_keyboard
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
    bot.send_message(message.from_user.id, "Привет, в игру какого жанра вы хотели бы сыграть?:", reply_markup=keyboard)  # отправл сообщ: кому отправляем, сам текст, указ клав-ру

@bot.message_handler(commands=["sport"])  # декоратор
def sport(message: Message):
    keyboard = sovet1_keyboard()
    bot.send_message(message.from_user.id, "Выберите игру:", reply_markup=keyboard)

@bot.message_handler(commands=["action"])  # декоратор
def action(message: Message):
    keyboard = sovet2_keyboard()
    bot.send_message(message.from_user.id, "Выберите игру:", reply_markup=keyboard)

@bot.message_handler(commands=["strategic"])  # декоратор
def strategic(message: Message):
    keyboard = sovet3_keyboard()
    bot.send_message(message.from_user.id, "Выберите игру:", reply_markup=keyboard)

@bot.message_handler(commands=["simulator"])
def simulator(message: Message):
    keyboard = sovet4_keyboard()
    bot.send_message(message.from_user.id, "Выберите игру:", reply_markup=keyboard)


bot.polling()  # запуск
