import random
my_list = [1, 2, 3, 4, 5]
# for i in my_list:
#     print(i)

# iterator = iter(my_list)
# for i in iterator:
#     print(i)


# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# #print(next(iterator))#StopIteration элементы закончились - следующего нет

#итератор случайных чисел
class RandomIterator:
    def __init__(self, limit):
        self.limit = limit
        self.__reload = limit
    def __iter__(self):
        self.limit = self.__reload#перезагружаем итератор
        return self
    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -= 1
        return random.randint(0, 100)
my_iter = RandomIterator(10)
for i in my_iter:
    print(i)

for i in my_iter:
    print(i)

for i in my_iter:
    print(i)
