# number = 10
# number2 = 20
# #сложение
# print(number + number2)
# #вычитание
# print(number - number2)
# #деление
# print(number / number2)
# #деление нацело
# print(number // number2)
# #деление с остатком
# print(number % number2)
# #умножение
# print(number * number2)
# #возведение в степень
# print(number ** number2)


# name = input("Введите имя: ")
# age = int(input("Сколько вам лет: "))
# #1 способ
# print("Тебя зовут {user_name}! Тебе {user_age} лет!".format(user_name=name, user_age=age))
#
# #2 способ - подстановка по очереди
# print("Тебя зовут {}! Тебе {} лет!".format(name, age))
#
# #3 способ - f строки
# print(f"Тебя зовут {name}! Тебе {age} лет!")
# try:
#     name = input("++Введите имя: ")
#     age = int(input("Сколько вам лет: "))
# except ValueError:
#     print("Нужно ввести число ")
# else:
#     print(f"Тебя зовут {name}! Тебе {age} лет!")
# finally:
#     print("Программа завершена")

# number_list = []
# number_list.append(1_000_000)
# number_list.append(1_000)
# number_list.append(10)
# print(number_list)
# print(number_list[-1])
#
# def summa(a, b):
#     # print(a + b)
#     return a + b
#
# result = summa(100, 50)
# print(result)

# def vvod_chisla():
#     try:
#         a = int(input("Введите значение a: "))
#         b = int(input("Введите значение b: "))
#     except ValueError:
#         print("Нужно ввести число, попробуйте еще раз. ")
#         vvod_chisla()
#     else:
#         # считаем дискриминант, значение С по-умолчанию установим = 1
#         с = 1
#         D = b ** 2 - 4 * a * с
#         print(f"Дискриминант = {D}")
#
#
# vvod_chisla()

#
# def vvod_chisla():
#     try:
#         number = int(input("Введите число1: "))
#         number2 = int(input("Введите число2: "))
#     except ValueError:
#         print("Нужно ввести число ")
#         vvod_chisla()
#     else:
#         #сложение
#         print(f"Сумма: {number} + {number2} = {number + number2}")
#         #вычитание
#         print(f"Разность: {number} - {number2} = {number - number2}")
#         # #деление
#         print(f"Деление: {number} / {number2} = {number / number2}")
#         # #деление нацело
#         print(f"Деление нацело: {number} // {number2} = {number // number2}")
#         # #деление с остатком
#         print(f"Деление с остатком: {number} % {number2} = {number % number2}")
#         # #умножение
#         print(f"Умножение: {number} * {number2} = {number * number2}")
#         # #возведение в степень
#         print(f"Возведение в степень: {number} ** {number2} = {number ** number2}")
#
# vvod_chisla()

