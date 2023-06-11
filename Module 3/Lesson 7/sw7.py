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


#
item1 = Item("Видеокарта", 15_000, 0.8)
item2 = Item("Процессор", 20_000, 0.2)
item3 = Item("DDR4", 8_000, 0.4)
item4 = Item("DVD-RW", 2_000, 1.1)
#
# total_sum = item1.price + item2.price
# print(total_sum)

# total_sum = item1 + item2
total_sum = item1 + item2 + item3 + item4
print(total_sum)