class Item:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    def __repr__(self):
        return self.brand
Items_list = [
    Item(1000, 'Apple'),
    Item(1200, 'Apple'),
    Item(900, 'Samsung'),
    Item(700, 'Samsung'),
    Item(660, 'Xiaomi'),
]
# print(Items_list)#начальный список брендов
#
# filtered_list = filter(lambda item: item.brand == 'Apple', Items_list)#фильтруем по значению 'Apple'
# print(list(filtered_list))

print(list(filter(lambda item: item.brand == 'Apple', Items_list)))
