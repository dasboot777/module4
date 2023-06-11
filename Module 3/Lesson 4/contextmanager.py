# file = open("test.txt", "w", encoding="utf-8")#создаем файл
# file.write("веб по контекстному менеджеру")
# file.close()

# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("веб по контекстному менеджеру")
#     print(file.closed)#файл открыт
# print(file.closed)#файл закрыт

# import  contextlib
# @contextlib.contextmanager
# def reverse_str(string):
#     yield string[::-1]# обратная сортировка строки
#
# with reverse_str("hello") as reversed_string:
#     print(reversed_string)

import  contextlib
@contextlib.contextmanager
def exc_handler(*args):#отлавливаем ошибку
    try:
        yield
    except *args:
        print("Ошибка, но мне все равно")
my_list = [1, 2]
with exc_handler(IndexError, ValueError, KeyError, AttributeError, SyntaxError):#типы ошибок (игнорировать исключения)
    my_list[4]# намеренно строка с ошибкой
    my_list(уууу)
    