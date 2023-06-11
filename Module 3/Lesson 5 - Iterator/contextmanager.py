import time
import sys

class CodeTimer:#замерячет время рабоыт нашшего кода
    def __init__(self):
        self.start = None# момент, с которго начнем отсчет
    def __enter__(self):#засекать наше время
        self.start = time.time() #точка старта
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_type)
        # print(exc_val)
        # print(exc_tb)

        t = time.time() - self.start# остановили таймер (точка останова)
        print(f"Код работал {t} секунд")

        if exc_type is IndexError:# обработка исключений
            return True#исключение подавляется, если возвращаем значение True

timer = CodeTimer()

with timer as t:
    l = [x for x in range (100_000_000)]
    print(t)

#

# class TreadRedirect:#перенаправление вывода
#     def __init__(self):
#         self.stdout = sys.stdout
#     def __enter__(self):
#         sys.stdout = open("file.txt", "w", encoding="utf-8")
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         sys.stdout = self.stdout
#
# with TreadRedirect():
#     print("Hello World")
