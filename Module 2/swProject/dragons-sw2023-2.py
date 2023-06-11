# 06/03/2023 проект

import random
import speech_recognition as sr
from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime


window = Tk()
window.geometry("600x800")
canvas = Canvas(window, width=600, height=800)
canvas.pack()


background = PhotoImage(file=r"C:\Users\I7\PycharmProjects\sw_pythonProject\Module 2\Lesson4\bg_2.png")

#игра дракончики
def dragonsgame():


    class Knight:
        def __init__(self):
            self.v = 0
            self.x = 150
            self.y = 350
            self.photo = PhotoImage(file=r"C:\Users\I7\PycharmProjects\sw_pythonProject\Module 2\Lesson4\knight.png")
            self.v2 = 0

        def up(self, event):
            self.v = -5

        def down(self, event):
            self.v = 5

        def right(self, event):
            self.v2 = +5

        def left(self, event):
            self.v2 = -5

        def stop(self, event):
            self.v = 0
            self.v2 = 0

    knight = Knight()

    class Dragon:
        def __init__(self):
            self.x = random.randint(500, 600)
            self.y = random.randint(50, 550)
            self.v = random.randint(1, 3)#задаем скорость драконов
            self.photo = PhotoImage(file=r"C:\Users\I7\PycharmProjects\sw_pythonProject\Module 2\Lesson4\dragon.png")

    dragons = []# создаем 3 драконов
    for i in range(5):
        dragons.append(Dragon())

    def game():
        canvas.delete("all")#все стираем в окне
        canvas.create_image(300, 300, image=background)#рисуем задний фон
        canvas.create_image(knight.x, knight.y, image=knight.photo)#рисуем рыцаря
        knight.y += knight.v
        knight.x += knight.v2
        # print(knight.v, knight.v2)

        for dragon in dragons:#рисуем драконов
            canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
            dragon.x -= dragon.v

            #удаляем драконов
            if ((dragon.x - knight.x) ** 2 + (dragon.y - knight.y) ** 2) ** 0.5 < 50:
                dragons.remove(dragon)

        #не даем рыцарю покинуть пределы окна
        if knight.y <= 59:
            knight.y = 60
        if knight.y >= 535:
            knight.y = 534
        if knight.x <= 50:
            knight.x = 51
        if knight.x >= 550:
            knight.x = 549

        #проверяем условия победы
        if len(dragons) == 0:#выигрыш, если список драконов пуст
            canvas.create_text(300, 300, text="Поздравляем, вы победили", fill='red', font="Arial 24")
            return#выход из цикла


        if dragon.x <= 0:#проигрыш, если дракон пересек координату x=0
            canvas.create_text(300, 300, text="Вы проиграли!", fill='cyan', font="Arial 38")
            return#выход из цикла


        window.after(10, game)# зацикливаем каждые 10 мс

    #биндим стрелки
    window.bind("<Key-Up>", knight.up)
    window.bind("<Key-Down>", knight.down)
    window.bind("<KeyRelease>", knight.stop)
    window.bind("<Key-Right>", knight.right)
    window.bind("<Key-Left>", knight.left)

    game()

#построить дом
def house():
   #
    canvas.create_rectangle(200, 200, 400, 400, fill='red', outline='blue')
    canvas.create_polygon(200, 200, 300, 100, 400, 200, fill='orange')
    canvas.create_rectangle(220, 300, 270, 320, fill='cyan', outline='blue')

#курсы валют
def kursdollara():
    today = datetime.today().strftime("%d.%m.%Y")  # форматируем дату
    print(today)

    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp", params={"date_req": today})
    # print(response)

    soup = BeautifulSoup(response.content, features="xml")

    # print(soup)

    def get_currency(currency_id):
        valute = soup.find("Valute", ID=currency_id)  # ищем по тегу Valute
        valute_value = valute.Value.text
        valute_name = valute.Name.text

        # создаем словарь
        valute_info = {"name": valute_name, "value": valute_value}
        return valute_info

    image_logo = PhotoImage(file=r"C:\Users\I7\PycharmProjects\sw_pythonProject\Lesson 8\logo.png")
    label_logo = Label(window, image=image_logo)
    label_logo.place(x=0, y=0)

    label_title = Label(window, text="ЦБРФ", font="Arial 36")
    label_title.place(x=230, y=50)

    label_currency = Label(window, text=f"Курс на {today}:", font="Arial 20")
    label_currency.place(x=50, y=170)

    dollar = get_currency("R01235")
    dollar_info_str = f"{dollar.get('name')} {dollar.get('value')}"  # кавычки должны отличаться
    label_currency = Label(window, text=dollar_info_str, font="Arial 16")
    label_currency.place(x=50, y=210)

    euro = get_currency("R01239")
    euro_info_str = f"{euro.get('name')} {euro.get('value')}"  # кавычки должны отличаться
    euro_label = Label(window, text=euro_info_str, font="Arial 16")
    euro_label.place(x=50, y=240)

    # Добавляем юань
    yuan = get_currency("R01375")
    yuan_info_str = f"{yuan.get('name')} {yuan.get('value')}"  # кавычки должны отличаться
    yuan_label = Label(window, text=yuan_info_str, font="Arial 16", fg="red")
    yuan_label.place(x=50, y=270)

    # поле для ввода
    entry = Entry(font="Arial 16", fg="blue", bg="yellow")
    entry.place(x=50, y=400)

    y = 30  # задаем шаг для новой строки курса

    # функция парс id
    def search():
        global y
        currency_id = entry.get()
        # print(currency_id)
        currency_info = get_currency(currency_id)
        currency_info_str = f"{currency_info.get('name')} {currency_info.get('value')}"
        # print(currency_info_str)
        currency_label = Label(window, text=currency_info_str, font="Arial 16", fg="green")
        currency_label.place(x=50, y=270 + y)
        y += 30
        # print(y)

        if y > 90:  # чтобы курс не убегал за рамки окна
            y = 30

    button = Button(text="Найти..", font="Arial 16", fg="pink", bg="green", command=search)
    button.place(x=350, y=400)

def govorun():
    canvas.delete("all")

    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone(device_index=1) as source:
            print("Скажите слово 'Дракон'")

            speech = recognizer.listen(source)
            speech_to_text = recognizer.recognize_google(speech, language="ru_RU")
            print(f"Вы сказали:{speech_to_text}")

            if speech_to_text.capitalize() == "Дракон":
                dragonsgame()
                break
            elif speech_to_text.capitalize() == "Дом":
                house()
                break
            elif speech_to_text.capitalize() == "Курс":
                kursdollara()
                break


button = Button(text="Нажмите на эту кнопку и скажите одно из этих слов: 'Дом', 'Дракон' или 'Курс'.", bg="yellow", font="Arial 12", command=govorun)
button.place(x=15, y=700)

# window.resizable(height=False, width=False)#запрет на изменение размера окна
window.mainloop()
