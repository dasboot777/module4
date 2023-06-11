from tkinter import *
window = Tk()
window.geometry("800x600")
canvas = Canvas(window, width=800, height=600, bg="white")#создание холста
canvas.pack()#натянули холст на окно

canvas.create_rectangle(200, 200, 400, 400, fill='red', outline='blue')# создаем прямоугльник по двум координатам
canvas.create_polygon(200, 200, 300, 100, 400, 200, fill='orange')#треугольник (крыша)
canvas.create_rectangle(220, 220, 280, 280, fill='cyan', outline='blue')#прямоугольник (окно внтури прямогулльника)
canvas.create_rectangle(220, 300, 380, 380, fill='cyan', outline='blue')#прямоугольник (окно внтури прямогулльника)
canvas.create_polygon(300, 280, 340, 220, 380, 280, fill='green', outline="black")#треугольник

window.mainloop()





