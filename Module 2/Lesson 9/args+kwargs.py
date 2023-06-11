#19/02/2023

# def func(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)
#     print(kwargs.get("name"))#работать как со словарем
#
# func(10, 20, 40, 50, 60, "NAme", name="Vasya")

#аргументы по-умолчанию
#
# def func(a="Xxxx", b="Apple"):
#     print(a, b)
#
# # func(10, "Sams")
# # func(30)

#условный оператор в одну строчку тернальный if
# age = 18
# if age >= 18:
#     is_allow = True
# else:
#     is_allow = False
# print(is_allow)

#в одну строчку
# age = 18
# citizen = "Russia"
# is_allow = True if age >= 18 and citizen == "Russia" else False
# print(is_allow)

# a=b or c

# a = True
# b = False
# c = a or b
# d = b or a
# print(c)
# print(d)

#генерация списков
# my_list = []
# for i in range (1000):
#     my_list.append(i)
# print(my_list)

# в одну строчку
# my_list = [i for i in range(1000)]
# print(my_list)

# деление на 5 (если остаток от деления равен 0)
# my_list = [i for i in range(1000) if i % 5== 0]
# print(my_list)

# деление на 5 и на 3 (водзводим в квадрат если не делится на 3)
# my_list = [i if i % 3 == 0 else i **2 for i in range(1000) if i % 5== 0]
# print(my_list)

#генерация словарей (длина слов)
# my_dict = {i: len(i) for i in ["orange", "green", "blue"]}
# print(my_dict)


#исключаем grren (5)
# my_dict = {i: len(i) for i in ["orange", "green", "blue"] if len(i) != 5}
# print(my_dict)

# сравнение по id и ==
# my_list_1 = [1, 2]
# my_list_2 = [1, 2]
# a = 20
# b = 20
# # print(my_list_1 == my_list_2)
# # print(my_list_1 is my_list_2)
# # print(a is b)
#
# print(id(a), id(b))#id одинковые
# print(id(my_list_1), id(my_list_2))#id разные


#кортежи
# a = (5, 3, 2, 1, 4)#создаем кортеж
# print(a)#выводим на экран
# print(type(a))# проверяем тип = кортеж
# sorted_a = tuple(sorted(a))# сортируем кортеж методом sorted
# print(sorted_a)# выводим отсортированный кортеж на экран
# print(type(sorted_a))# проверяем тип сортированного кортежа = кортеж

# my_tuple = (1, 2, 3, 4, 5)
# print(type(my_tuple))
# print(my_tuple)
# print(my_tuple.count(4))
# print(my_tuple.index(4))
# print(my_tuple[4])

#токль показываем
# my_tuple = (i for i in range(1000))
# print(my_tuple)
#
# for i in my_tuple:
#     print(i)
#создаем кортеж
# my_tuple = tuple(i for i in range(1000))
# print(my_tuple)
#
# for i in my_tuple:
#     print(i)

#множества - неупорядочены неиндексируются, хаотичная структура данных
# my_list = [1, 1, 2, 3, 4, 4]
# my_set = set(my_list)# только уникальные элементы
# print(my_set)

#создаем множество вручнюу
# my_set = {1, 2, 3, 4, 5}
# my_set_2 = {4, 5, 6, 7, 8}
# print(my_set)
# print(my_set.intersection(my_set_2)) # ищем олбщие элементы (пересчение множеств)
# print(my_set.union(my_set_2))# объединение множеств



