from tkinter import *

window = Tk()
window.geometry("800x600")

canvas = Canvas(window, width=800, height=600, bg="white") # создание холста
canvas.pack() # прилепили холст на окно

canvas.create_rectangle(200, 200, 400, 400, fill='red', outline='blue')
canvas.create_polygon(200, 200, 300, 100, 400, 200, fill='orange')
canvas.create_rectangle(220, 300, 270, 320, fill='cyan', outline='blue')
window.mainloop()
