# 06/03/2023 проект

import random
import speech_recognition as sr
from tkinter import *


window = Tk()
window.geometry("600x600")
canvas = Canvas(window, width=600, height=600)
canvas.pack()

background = PhotoImage(file=r"C:\Users\I7\PycharmProjects\sw_pythonProject\Lesson4\bg_2.png")



class Knight:
    def __init__(self):
        self.v = 0
        self.x = 150
        self.y = 350
        self.photo = PhotoImage(file=r"C:\Users\I7\PycharmProjects\sw_pythonProject\Lesson4\knight.png")
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
        self.photo = PhotoImage(file=r"C:\Users\I7\PycharmProjects\sw_pythonProject\Lesson4\dragon.png")

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


recognizer = sr.Recognizer()

while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите слово 'Дракон'")

        speech = recognizer.listen(source)
        speech_to_text = recognizer.recognize_google(speech, language="ru_RU")
        print(f"Вы сказали:{speech_to_text}")

        if speech_to_text.capitalize() == "Дракон":
            game()
            break
# game()
window.resizable(height=False, width=False)#запрет на изменение размера окна
window.mainloop()
