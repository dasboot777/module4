from tkinter import *
import random
window = Tk()
window.geometry("600x600")


class Steam:

    image = PhotoImage(file=r'C:\Users\I7\PycharmProjects\sw_pythonProject\Module 3\Lesson 7\elements\aroma.png').subsample(4, 4)#уменьшаем картинку в 4 раза
    def __add__(self, other):
        if isinstance(other, Fire):
            return Water()
        elif isinstance(other, Earth):
            return Clay()
        elif isinstance(other, Water):
            return Wind()
        elif isinstance(other, Wind):
            return Fire()

class Dust:

    image = PhotoImage(file=r'C:\Users\I7\PycharmProjects\sw_pythonProject\Module 3\Lesson 7\elements\free-icon-dust-2396941.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Steam):
            return Clay()
        elif isinstance(other, Earth):
            return Wind()
        elif isinstance(other, Water):
            return Earth()

class Clay:

    image = PhotoImage(file=r'C:\Users\I7\PycharmProjects\sw_pythonProject\Module 3\Lesson 7\elements\free-icon-pottery-7942410.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Wind()
        elif isinstance(other, Fire):
            return Earth()

class Wind:

    image = PhotoImage(file=r'C:\Users\I7\PycharmProjects\sw_pythonProject\Module 3\Lesson 7\elements\wind.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Clay):
            return Earth()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Fire):
            return Clay()
        elif isinstance(other, Steam):
            return Water()
        elif isinstance(other, Dust):
            return Fire()

class Earth:

    image = PhotoImage(file=r'C:\Users\I7\PycharmProjects\sw_pythonProject\Module 3\Lesson 7\elements\ground.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust()
        elif isinstance(other, Water):
            return Clay()
        elif isinstance(other, Fire):
            return Steam()

class Fire:

    image = PhotoImage(file=r'C:\Users\I7\PycharmProjects\sw_pythonProject\Module 3\Lesson 7\elements\free-icon-fire-9509865.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Steam):
            return Water()
        elif isinstance(other, Earth):
            return Clay()

class Water:

    image = PhotoImage(file=r'C:\Users\I7\PycharmProjects\sw_pythonProject\Module 3\Lesson 7\elements\free-icon-water-drop-4246703.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Clay()
        elif isinstance(other, Steam):
            return Earth()


canvas = Canvas(width=600, height=600)#натягиваем хоолст
canvas.pack()
elements = [Earth(), Water(), Wind(), Fire()]
for elem in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)

def move(event):
    # print("Вы кликнули на окно")
    images_ids = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)#метод находит объекты в указанных координатах
    if len(images_ids) ==2:#проверяем 2 элемента вместе
        images_id_1, images_id_2 = images_ids[0], images_ids[1]#получасем id этих элементов
        elem_1 = elements[images_id_1 - 1]#указываем инджексы на 1 мешьше
        elem_2 = elements[images_id_2 - 1]  # указываем инджексы на 1 мешьше

        new_elem = elem_1 + elem_2#реакция должна сработь только 1 раз, нужно проверить есть ли этот элемиент в списке
        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)


    canvas.coords(images_ids, event.x, event.y)
    # print(images_ids)


window.bind('<B1-Motion>', move)

window.mainloop()



