
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    # сеттер
    @name.setter
    def name(self, name):
        #запрет использования имен
        for sym in name:
            if sym.isdigit():#проверка, является ли текущий символ числом
                raise Exception("Имя недопустимо, т.к. содержит цифры")
        self.__name = name
    # делитер

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

#создаем экземпляр класса Person с именем и возрастом
person = Person("Валера", 16)
print(person.name, person.age)

#изменяем атрибут name
person.name = "Гриша"
print(person.name)

#изменяем атрибут age
person.age = 22
print(person.age)

#применяем делитер
del person.name
del person.age
#значения атрибутов удалены - слоаврь пуст
print(person.__dict__)
#заново присваиваем значения
person.name = "Вася"
person.age = 38
print(person.name, person.age)