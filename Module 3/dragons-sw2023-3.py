# 28/05/2023 проект3
import speech_recognition as sr
from tkinter import *
import sqlite3

window = Tk()
window.geometry("600x800")
canvas = Canvas(window, width=600, height=800)

canvas.pack()

label_currency = Label(window, text="Для работы программы должен быть подключен микрофон\n"
                                    "Программа будет выводить сообщения в терминале \n"
                                    "\nНажмите кнопку и скажите команду (что надо сделать):\n"
                  "1. 'База' - создать БД и вывести на экран ее содержимое\n"
                  "2. 'Изменить' - изменить значения имен в БД\n"
                  "3. 'Девочки' или 'Мальчики' - вывести список девочек или мальчиков из БД\n"
                  "4. Назвать имя (Лёша, Эрнест, Варвара, Константин, Гриша, Елизавета)\n и получить данные по этой записи из БД\n"
                  "5. 'Удалить всё' - очистить БД \n",
                                     font="Arial 13", justify='left', fg='blue')
label_currency.place(x=10, y=10)

class User:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

def govorun():
    canvas.delete("all")

    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone(device_index=1) as source:
            print("Нажмите кнопку и скажите команду (что надо сделать):"
                  )


            speech = recognizer.listen(source)
            speech_to_text = recognizer.recognize_google(speech, language="ru_RU")
            print(f"Вы сказали:{speech_to_text}")

            if speech_to_text.capitalize() == "База":
                bd()
                break
            elif speech_to_text.capitalize() == "Изменить":
                izmenit()
                break
            elif speech_to_text.capitalize() == "Девочки":
                spisok_devochek = get_gender(cursor, 'Ж')
                print(f'Список девочек: {spisok_devochek}')
                break
            elif speech_to_text.capitalize() == "Мальчики":
                spisok_malchikov = get_gender(cursor, 'М')
                print(f'Список мальчиков: {spisok_malchikov}')
                break
            elif speech_to_text.capitalize() == "Удалить всё":
                delete_all_users(cursor)
                users = get_all_users(cursor)  # выводим SQL запрос в переменную
                print(f'База данных очищена: {users}')
                break



            elif speech_to_text.capitalize() == "Лёша" or "Эрнест" or "Варвара" or "Константин" or "Гриша" or "Елизавета":
                print(speech_to_text.capitalize())
                user_name = speech_to_text.capitalize()
                spisok = get_user_by_name(cursor, user_name)
                print(f'Вот что было найдено: {spisok}')
                break

            # elif speech_to_text.capitalize() == "1" or "2" or "3" or "4" or "5" or "6":
            #     print(speech_to_text.capitalize())
            #     user_id = speech_to_text.capitalize()
            #
            #     del_user_by_id(cursor, user_id)
            #     print(f'Из таблицы была удалена запись id: {user_id}')
            #
            #     users = get_all_users(cursor)  # выводим SQL запрос в переменную
            #     print(f'База данных теперь выглядит так: {users}')
            #     break






def bd():#создаем базу данных и выводим содержимое
    delete_all_users(cursor)  # очищаем таблицу
    create_users_table(cursor)

    user1 = User(name='Максим', age=16, gender='М')  # создаем эксземпляры пользователей
    user2 = User(name='Ксения', age=15, gender='Ж')  # создаем эксземпляры пользователей
    user3 = User(name='Василий', age=18, gender='М')  # создаем эксземпляры пользователей
    user4 = User(name='Юлия', age=17, gender='Ж')  # создаем эксземпляры пользователей
    user5 = User(name='Василиса', age=20, gender='Ж')  # создаем эксземпляры пользователей
    user6 = User(name='Сергей', age=22, gender='М')  # создаем эксземпляры пользователей
    add_new_user(cursor, user1)  # добавляем созданных пользователей
    add_new_user(cursor, user2)  # добавляем созданных пользователей
    add_new_user(cursor, user3)  # добавляем созданных пользователей
    add_new_user(cursor, user4)  # добавляем созданных пользователей
    add_new_user(cursor, user5)  # добавляем созданных пользователей
    add_new_user(cursor, user6)  # добавляем созданных пользователей

    users = get_all_users(cursor)  # выводим SQL запрос в переменную
    print(f'Содержимое базы данных: {users}')

def izmenit():# Изменяем имена в БД
    update_user_name(cursor, 1, 'Гриша')  # меняем имя первого пользователя
    update_user_name(cursor, 2, 'Лёша')  # меняем имя второго пользователя
    update_user_name(cursor, 3, 'Елизавета')  # меняем имя второго пользователя
    update_user_name(cursor, 4, 'Эрнест')  # меняем имя второго пользователя
    update_user_name(cursor, 5, 'Варвара')  # меняем имя второго пользователя
    update_user_name(cursor, 6, 'Константин')  # меняем имя второго пользователя
    users = get_all_users(cursor)
    print(f'Теперь имена выглядят так: {users}')

def create_users_table(cur: sqlite3.Cursor):  # создаем таблицу
    command = """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    gender TEXT,
    age INTEGER,
    name TEXT)
    """
    cur.execute(command)

def get_gender(cur: sqlite3.Cursor, user_gender: str):
    command = """
    SELECT * FROM users WHERE gender = ?
    """
    result = cur.execute(command, (user_gender,))
    return result.fetchall()  # возвращаем результат SQL запроса

def del_user_by_id(cur: sqlite3.Cursor, user_id: int):  # удаляем пользователя по id
    command = """
    DELETE FROM users WHERE id = ?
    """
    result = cur.execute(command, (user_id,))
    return result.fetchone()  # возвращаем одно значение

def del_user_by_name(cur: sqlite3.Cursor, user_name: str):  # удаляем пользователя по имени
    command = """
    DELETE FROM users WHERE name = ?
    """
    result = cur.execute(command, (user_name,))
    return result.fetchone()  # возвращаем одно значение


def add_new_user(cur: sqlite3.Cursor, user: User):  # добавляем строку с данными
    command = """
    INSERT INTO users(name, age, gender) VALUES(?, ?, ?)
    """
    cur.execute(command, (user.name, user.age, user.gender))  # через параметры

def get_all_users(cur: sqlite3.Cursor):
    command = """
    SELECT * FROM users
    """
    result = cur.execute(command)
    return result.fetchall()  # возвращаем результат SQL запроса

def update_user_name(cur: sqlite3.Cursor, user_id: int, name: str):  # обновляем поля через параметры
    command = """
    UPDATE users SET name = ? WHERE id = ?
    """
    cur.execute(command, (name, user_id))

def delete_all_users(cur: sqlite3.Cursor):  # удаляем пользователей
    command = """
    DELETE FROM users
    """
    cur.execute(command)

def get_user_by_id(cur: sqlite3.Cursor, user_id: int):  # получаем пользователя по id
    command = """
    SELECT * FROM users WHERE id = ?
    """
    result = cur.execute(command, (user_id,))
    return result.fetchone()  # возвращаем одно значение

def get_user_by_name(cur: sqlite3.Cursor, user_name: str):  # получаем пользователя по имени
    command = """
    SELECT * FROM users WHERE name = ?
    """
    result = cur.execute(command, (user_name,))
    return result.fetchone()  # возвращаем одно значение

if __name__ == '__main__':
    with sqlite3.connect(
            'sqlite.db') as connection:  # внутри блока КМ мы подключены к БД, потом соединение автоматически закрывается
        cursor = connection.cursor()  # создаем курсор



        button = Button(text="Нажмите на эту кнопку\n и скажите одно из этих слов:\n\n 'База', \n'Изменить', \n'Девочки', \n'Мальчики',  \n\n имя для поиска из этого списка: \nЛёша, Эрнест, Варвара, \nКонстантин, Гриша, Елизавета.\n\nдля очистки БД скажите \n'Удалить всё'",
                        bg="yellow", font="Arial 12", fg="red", command=govorun)
        button.place(x=150, y=300, height=300, width=300)

        window.resizable(height=False, width=False)#запрет на изменение размера окна
        window.mainloop()















