from tkinter import *

window = Tk()
window.geometry("800x600")

canvas = Canvas(window, width=800, height=600, bg="white")  # создание холста
canvas.pack()  # прилепили холст на окно


class House:
    def __init__(self, color_of_walls, color_of_triangle, color_of_rectangle):
        self.color_of_walls = color_of_walls
        self.color_of_triangle = color_of_triangle
        self.color_of_rectangle = color_of_rectangle

    def build_house(self):

        canvas.create_rectangle(200, 200, 400, 400, fill=self.color_of_walls,
                                outline='blue')  # создаем прямоугльник по двум координатам
        canvas.create_polygon(200, 200, 300, 100, 400, 200, fill=self.color_of_triangle)  # треугольник (крыша)
        canvas.create_rectangle(220, 220, 280, 280, fill=self.color_of_rectangle,
                                outline='blue')  # прямоугольник (окно внтури прямогулльника)
        canvas.create_rectangle(220, 300, 380, 380, fill=self.color_of_rectangle,
                                outline='blue')  # прямоугольник (окно внтури прямогулльника)
        canvas.create_polygon(300, 280, 340, 220, 380, 280, fill=self.color_of_triangle, outline="black")  # треугольник

house = House('cyan', 'orange', 'red')
house.build_house()

window.mainloop()
