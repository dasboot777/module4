class Pet:
    def __init__(self, has_tail, legs, name, ears):
        self.has_tail = has_tail
        self.legs = legs
        self.name = name
        self.ears = ears

    def sound(self):#метод класса
        pass
    def __str__(self):#вывод форматируем
        return f"У {self.name} {self.legs} ног и {'есть хвост' if self.has_tail else 'хвоста нет'}." \
               f" У него {'есть ушки' if self.ears else 'нет ушей'}."


class Dog(Pet):
    def __init__(self, legs, name, ears):
        super().__init__(name=name, legs=legs, ears=ears, has_tail=True)


dog = Dog(4, "Бобака", True)

print(dog)

class Cat(Pet):
    def __init__(self, has_tail, legs, name):
        super().__init__(has_tail=has_tail, legs=legs, name=name, ears=True)

cat = Cat(True, 4, "Кошара")
print(cat)

class A:
    def info(self):
        print("A")

class B(A):
    print("B")
    super().info()

B().info()
