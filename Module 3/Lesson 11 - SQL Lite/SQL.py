import sqlite3

# try:
#     connection = sqlite3.connect('sqlite.db')#создаем переменную connection и подключение к бд
#
# except sqlite3.DatabaseError:#отлавливаем ошибку
#     print('При подключении к БД возникла ошибка')
#
# finally:#ветка выполняется в любом случае
#     connection.close()#закрываем файл

#делаем через контекст менеджер
class User:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

def create_users_table(cur: sqlite3.Cursor):
    command = """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    gender TEXT,
    age INTEGER,
    name TEXT)
    
    
    """
    cur.execute(command)

def add_new_user(cur: sqlite3.Cursor, user: User):
    command = """
    INSERT INTO users(name, age, gender) VALUES(?, ?, ?)
    """
    cur.execute(command, (user.name, user.age, user.gender))#через параметры

def get_all_users(cur: sqlite3.Cursor):
    command = """
    SELECT * FROM users
    """
    result = cur.execute(command)
    return result.fetchall()#возвращаем результат SQL запросы

def update_user_name(cur: sqlite3.Cursor, user_id: int, name: str):#обновлдляем поля через параметры
    command = """
    UPDATE users SET name = ? WHERE id = ?
    """
    cur.execute(command, (name, user_id))

def delete_all_users(cur: sqlite3.Cursor):#удаляем пользователей
    command = """
    DELETE FROM users
    """
    cur.execute(command)

def get_user_by_id(cur: sqlite3.Cursor, user_id: int):#получаем пользователя по id
    command = """
    SELECT * FROM users WHERE id = ?
    """
    result = cur.execute(command, (user_id,))
    return result.fetchone()#возвращаем одно значение



if __name__ == '__main__':
    with sqlite3.connect('sqlite.db') as connection:#внутри блока КМ мы подключены к БД, потом соединение автоматически закрывается
        cursor = connection.cursor()#создаем курсор
        create_users_table(cursor)
        delete_all_users(cursor)#очищаем таблицу
        user1 = User(name='Максим', age=16, gender='М')#создаем эксземпляры пользователей
        user2 = User(name='Ксения', age=15, gender='Ж')#создаем эксземпляры пользователей
        add_new_user(cursor, user1)#добавляем созданных пользователей
        add_new_user(cursor, user2)#добавляем созданных пользователей
        users = get_all_users(cursor)#выводим SQL запрос в переменную
        print(users)
        update_user_name(cursor, 1, 'Гриша')# меняем имя первого пользователя
        update_user_name(cursor, 2, 'Леша')  # меняем имя первого пользователя
        users = get_all_users(cursor)
        print(users)
        lesha = get_user_by_id(cursor, 2)
        print(lesha)

