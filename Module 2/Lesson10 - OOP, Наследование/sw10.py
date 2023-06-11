class Pet:
    has_tail = True
    legs = 4
    name = None
    ears = True

    def __str__(self):#вывод форматируем
        return f"У {self.name} {self.legs} ног и {'есть хвост' if self.has_tail else 'хвоста нет'}." \
               f" У него {'есть ушки' if self.ears else 'нет ушей'}."

    def sound(self):#метод класса
        pass

class Dog(Pet):
    name = "Чарли"#переопределяем переменную
    def sound(self):
        return "Гав!!"


# print(Pet())
print(Dog())
print(Dog().sound())

class Frog(Pet):
    has_tail = False
    ears = False
    name = "Фрогги"

    def sound(self):
        return "Ква-ква"

print(Frog(), Frog().sound())
