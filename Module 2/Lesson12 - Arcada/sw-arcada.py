from tkinter import *
import  time

window = Tk()
window.geometry('500x400')
window.resizable(width=False, height=False)

class Ball:#создаем класс Шарик
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.x = 1#задаем скорость шарика по координатам x,y
        self.y = 1

    #отрисовываем шарик заново
    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        position = self.canvas.coords(self.oval)#текущие координаты шарика
        print(position)
        if position[0] <= 0:# проверяем по левой границе x
            self.x = -self.x
        if position[2] > 500:# проверяем по левой границе y
            self.x = -self.x
        if position[1] < 0:# проверяем по левой границе y
            self.y = -self.y
        if position[3] > 400:# проверяем по левой границе x
            self.y = -self.y

class Platform:#создаем платформу
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(200, 200, 300, 230, fill=color)
        self.x = 0
        # self.y = 300

    def left(self, event):#методы будут менять напрявление движения прямоугольника
        self.x = -2

    def right(self, event):
        self.x = 2

    def draw(self):
        self.canvas.move(self.rect, self.x, 280)


canvas = Canvas(window, width=500, height=400)
canvas.pack()
ball = Ball(canvas=canvas, color="red")
platform = Platform(canvas, color="green")


#биндим кнопки
window.bind("<Key-Left>", platform.left)
window.bind("<Key-Right>", platform.right)

while True:
    ball.draw()
    window.update()
    #замедляем программу
    time.sleep(0.01)



