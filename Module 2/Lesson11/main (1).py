class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self._passport = "123456"
        self.__date_of_birth = date_of_birth

    def __info(self):
        print(self.name, self._passport)



person = Person("Захар", "01/01/2010")
print(person._Person__date_of_birth)
person._Person__date_of_birth = "01/01/1990"
print(person._Person__date_of_birth)
