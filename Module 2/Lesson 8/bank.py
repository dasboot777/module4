from sw8 import  get_currency, today
from tkinter import *

window = Tk()
window.geometry("500x500")

image_logo = PhotoImage(file=r"/Module 1/Lesson 8/logo.png")
label_logo = Label(window, image=image_logo)
label_logo.place(x=0, y=0)

label_title = Label(window, text="ЦБРФ", font="Arial 36")
label_title.place(x=230, y=50)

label_currency = Label(window, text=f"Курс на {today}:", font="Arial 20")
label_currency.place(x=50, y=170)

dollar = get_currency("R01235")
dollar_info_str = f"{dollar.get('name')} {dollar.get('value')}"#кавычки должны отличаться

label_currency = Label(window, text=dollar_info_str, font="Arial 16")
label_currency.place(x=50, y=210)

euro = get_currency("R01239")
euro_info_str = f"{euro.get('name')} {euro.get('value')}"#кавычки должны отличаться
euro_label = Label(window, text=euro_info_str, font="Arial 16")
euro_label.place(x=50, y=240)




#поле для ввода
entry = Entry(font="Arial 16")
entry.place(x=50, y=400)

y = 30 #задаем шаг для новой строки курса

#функция парс id
def search():
    global y
    currency_id = entry.get()
    # print(currency_id)
    currency_info = get_currency(currency_id)
    currency_info_str = f"{currency_info.get('name')} {currency_info.get('value')}"
    # print(currency_info_str)
    currency_label = Label(window, text=currency_info_str, font="Arial 16")
    currency_label.place(x=50, y=240+y)
    y += 30
    # print(y)

    if y > 120:#чтобы курс не убегал за рамки окна
        y = 30

button = Button(text="Найти..", font="Arial 16", command=search)
button.place(x=350, y=400)

window.mainloop()