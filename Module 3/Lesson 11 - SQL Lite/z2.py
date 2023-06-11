import sqlite3

class User:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender





def create_users_table(cur: sqlite3.Cursor):#создаем таблицу
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

def add_new_user(cur: sqlite3.Cursor, user: User):#добавляем строку с данными
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


if __name__ == '__main__':
    with sqlite3.connect(
            'sqlite.db') as connection:  # внутри блока КМ мы подключены к БД, потом соединение автоматически закрывается
        cursor = connection.cursor()  # создаем курсор
        create_users_table(cursor)
        delete_all_users(cursor)  # очищаем таблицу
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
        print(users)
        update_user_name(cursor, 1, 'Гриша')  # меняем имя первого пользователя
        update_user_name(cursor, 2, 'Леша')  # меняем имя первого пользователя
        users = get_all_users(cursor)
        print(users)
        lesha = get_user_by_id(cursor, 2)
        print(lesha)

        # users = get_all_users(cursor)
        # print(f'Текущий список пользователей: {users}')
        # del_lesha = del_user_by_id(cursor, 2)
        # print(f'Из таблицы была удалена запись: {lesha}')
        # users = get_all_users(cursor)
        # print(f'Текущий список пользователей: {users}')

        spisok_devochek = get_gender(cursor, 'Ж')
        print(f'Список девочек: {spisok_devochek}')
        spisok_malchikov = get_gender(cursor, 'М')
        print(f'Список мальчиков: {spisok_malchikov}')


