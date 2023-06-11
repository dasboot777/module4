class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):#левое сложение
        if isinstance(other, int):#проверка на тип данных
            return self.price + other
        elif isinstance(other, Item):
            return self.price + other.price#складываем цены
            # return self.weight + other.weight  # складываем вес

    def __radd__(self, other):  # правое сложение
        if isinstance(other, int):  # проверка на тип данных
            return self.price + other
        elif isinstance(other, Item):
            return self.price + other.price  # складываем цены

    def __sub__(self, other): #вычитание
        if isinstance(other, int):#проверка на тип данных
            return self.price - other
        elif isinstance(other, Item):
            return self.price - other.price#вычитаем цены

    def __mul__(self, other):#умножение на указанный множитель
        if isinstance(other, int):#проверка на тип данных
            return self.price * other
        elif isinstance(other, Item):
            return self.price * other.price#умножение на указанный множитель

    def __truediv__(self, other):#деление на указанный делитель
        if isinstance(other, int):#проверка на тип данных
            return self.price / other
        elif isinstance(other, Item):
            return self.price / other.price#деление на указанный делитель


#
item1 = Item("Видеокарта", 15_000, 0.8)
item2 = Item("Процессор", 20_000, 0.2)
item3 = Item("DDR4", 8_000, 0.4)
item4 = Item("DVD-RW", 2_000, 1.1)
#
# total_sum = item1.price + item2.price
# print(total_sum)

# total_sum = item1 + item2
total_sum = item1 + item2 + item3 + item4#складываем цены
print(f"Сложение цен в классе Item: {total_sum}")

total_sub = item1 - item4
print(f"Вычитание цен в классе Item: {total_sub}")

total_mul = item1*2
print(f"Умножение цен в классе Item на указанный множитель: {total_mul}")

total_div = item1/2
print(f"Деление цен в классе Item на указанный делитель: {total_div}")