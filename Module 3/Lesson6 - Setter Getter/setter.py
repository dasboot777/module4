# #геттер - получаем приватный атрибуьт
# class Year:
#     def __init__(self):
#         self.__days = 365
#         self.__season = "лето"
#
#     def get_days(self):
#         return self.__days
#
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception(f"Вы передали некорректное значение,  в году не может быть {days}")
#
#
# year = Year()
# # print(year._Year__days)
# print(year.get_days())
#
# year._Year__days = 366
# print(year._Year__days)
#
# # year.set_days(364)
# print(year.get_days())


###2
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    # сеттер
    @name.setter
    def name(self, name):
        #запрет использования имен
        for sym in name:
            if sym.isdigit():#проверка, является ли текущий символ числом
                raise Exception("Имя недопустимо, т.к. содержит цифры")
        self.__name = name

person = Person("Валера", 16)
print(person.name)

person.name = "Гриша"
print(person.name)