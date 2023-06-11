import time
#1способ
nachalo1 = time.time()#засекаем время начала работы первого генератора
def kvadraty():
    for i in range(1, 1_000_001):
        yield i**2

for kvadrat in kvadraty():
    print(kvadrat)
konets1 = time.time() - nachalo1  # остановили таймер (точка останова)
print("Работа первого генератора квадратов завершена.")
time.sleep(2)#пауза 2 сек


#2способ
nachalo2 = time.time()#засекаем время начала работы второго генератора
kvadraty2 = (i**2 for i in range(1, 1_000_001))
for kvadrat2 in kvadraty2:
    print(kvadrat2)
konets2 = time.time() - nachalo2  # остановили таймер (точка останова)
print("Работа второго генератора квадратов завершена.")

time.sleep(2)#пауза 2 сек
print(f"Генератор № 1 работал {konets1} секунд")
print(f"Генератор № 2 работал {konets2} секунд")