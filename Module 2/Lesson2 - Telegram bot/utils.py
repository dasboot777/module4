import random
from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

def welcome_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                   one_time_keyboard=True)  # создаем клавиатуру, задаем размер и исчезающую клав
    # создаем 4 кнопки
    button1 = KeyboardButton("/sport")
    button2 = KeyboardButton("/action")
    button3 = KeyboardButton("/strategic")
    button4 = KeyboardButton("/simulator")

     # добавляем кнопки в клавру
    keyboard.add(button1, button2, button3, button4)
    return keyboard #возвращаем созданную клав


def sovet1_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Спорт и гонки. Скачать игру можно здесь:", url="https://store.steampowered.com/category/sports_and_racing/")
    keyboard.add(button)
    return keyboard  # возвращаем созданную клав
def sovet2_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Экшен. Скачать игру можно здесь:", url="https://store.steampowered.com/category/action/")
    keyboard.add(button)
    return keyboard  # возвращаем созданную клав
def sovet3_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Стратегии. Скачать игру можно здесь:", url="https://store.steampowered.com/category/strategy/")
    keyboard.add(button)
    return keyboard  # возвращаем созданную клав
def sovet4_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Симуляторы. Скачать игру можно здесь:", url="https://store.steampowered.com/category/simulation/")
    keyboard.add(button)
    return keyboard  # возвращаем созданную клав