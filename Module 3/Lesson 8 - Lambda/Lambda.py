import pprint#pretty print
goods = [
    {
        'name': 'Iphone 7',
        'brand': 'Apple',
        'price': 400,
    },
    {
        'name': 'Ipad',
        'brand': 'Apple',
        'price': 500,
    },
    {
        'name': 'Windows 2023',
        'brand': 'Microsoft',
        'price': 200,
    },
]
#способ 1
# def on_price(item):#создаем функцию сортировки по цене
#     return item['price']#возвращаем значение функции по ключу словаря 'price'
# print(sorted(goods, key=on_price))#указываем ключом сортировки функцию on_price()

#способ 2
# print(sorted(goods, key=lambda item: item['price']))

# #фильтрация
# filtered_list = filter(lambda item: item['brand'] == 'Apple', goods)#фильтруем по полю 'brand' только по значению 'Apple' и указываем место фильтрации
# print(filtered_list)
# print(list(filtered_list))

#map
#1 перевод строки в числа
# numbers_list = ['1', '2', '3', '4', '5']
# mapped_list = map(int, numbers_list)
# print(mapped_list)#ленивые вычисления
# print(numbers_list)#выводим первоначальный список - значения - строки
# print(list(mapped_list))#выводим список после функции map - значения - числа

#2 создаем 2 списка, где отдельно хранятся имена и фамилии
# names_list = ['Данил', 'Миша', 'Булат']
# surnames_list = ['Устюжин', 'Сапрыкин', 'Ибрагимов']
# # persons_list = map(lambda name, surname: f'{name} {surname}', names_list, surnames_list )#лямбда функция будет формировать f'строки из значений 'name' и 'surname' и указываем место
# # print(persons_list)
# # print(list(persons_list))
# #лабо сразу оборачиваем объекты ленивых вычислений функцией List
# persons_list = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames_list ))
# print(persons_list)

# #enumerate
# indexed_goods = []#создаем пустой список
# for index, item in enumerate(goods):#ищем индексы словарей
#     indexed_goods.append({index: item})#добавляем проиндексированные словари в пустой списко indexed_goods
# print(indexed_goods)
# pprint.pprint(indexed_goods)

# #zip
# names_list = ['Марсель', 'Максим', 'Алексей']
# surnames_list = ['Тарапатин', 'Словягин', 'Щербаков']
# for name, surname in zip(names_list, surnames_list):
#     print(name, surname)

# print(__name__)#то, откуда запускается скрипт, переменная __name__ принимает разные значения
if __name__ == "__main__":#код будет исполнятся только здесь, если импортировать в другое место - исполняться не будет
    pass
else:
    print("Запуск выполнен из другого скрипта")
