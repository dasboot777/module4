#задача 1
# a = (5, 3, 2, 1, 4)#создаем кортеж
# print(a)#выводим на экран
# print(type(a))# проверяем тип = кортеж
# sorted_a = tuple(sorted(a))# сортируем кортеж методом sorted
# print(sorted_a)# выводим отсортированный кортеж на экран
# print(type(sorted_a))# проверяем тип сортированного кортежа = кортеж

#Задача 2

# def chet_nechet(*args):
#
#
#     nechet_list = []
#     chet_list = []
#
#     for i in range (10):
#         if i % 2 == 0:
#             chet_list.append(i)
#         else:
#             nechet_list.append(i)
#
#     print(f"Список с четными числами: {chet_list}, Список с нечетными числами: {nechet_list}")
#
# chet_nechet()



nechet_list = []
chet_list = []

for i in range (10):
    if i % 2 == 0:
        chet_list.append(i)
    else:
        nechet_list.append(i)

print(f"Список с четными числами: {chet_list}, Список с нечетными числами: {nechet_list}")

