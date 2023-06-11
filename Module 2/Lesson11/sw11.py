class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.__date_of_birth = date_of_birth
        # два подчеркивания __защищаем атрибут от несанкцированного доустпа

    def __info(self):#защита метода
        print(self.name)



person = Person("Захар", "01.01.2010")

print(person._Person__date_of_birth)


