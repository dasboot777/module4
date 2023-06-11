class A:#применяем паттерн
    __instance = None #изначалеьнго экз класса нет

    def __new__(cls, *args, **kwargs):#вызывается первым - cls - ссылка на класс
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
                self,name = name

a = A("НГкиик")
a1 = A("аавава")
print(a is a1)
print(a.name)
print(a1.name)

#false - это разыые побъекты

