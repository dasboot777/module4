import random
class User:
    def __init__(self, imya, zdorovie, uron):
        self.imya = imya
        self.zdorovie = zdorovie
        self.uron = uron

    def __str__(self):
        return self.imya

    def attack(self, target):#метод атаки
        # uron = 10  # Базовый урон атаки
        target.nanesti_uron(self.uron)

    def nanesti_uron(self, uron):#метод урона
        self.zdorovie -= uron


class Mag(User):
    pass

class Voin(User):
    pass

class Luchnik(User):
    pass


#создаем экземпляры класса
user1 = Mag("Маг", 100, random.randint(25, 50))
user2 = Voin("Воин", 150, random.randint(20, 30))
user3 = Luchnik("Лучник", 200, random.randint(10, 25))

while user1.zdorovie > 0 and user2.zdorovie > 0 and user3.zdorovie > 0:
    kto_atakuet = random.choice([user1, user2, user3])
    kogo_atakuut = random.choice([user1, user2, user3])
    if kto_atakuet != kogo_atakuut:
        print(f"Первым атакует {kto_atakuet}")
        #вызываем метод атаки
        kto_atakuet.attack(kogo_atakuut)
        print(f"{kto_atakuet} (осталось здоровья {kto_atakuet.zdorovie}) атаковал и нанес урон {kto_atakuet.uron} {kogo_atakuut} (осталось здоровья {kogo_atakuut.zdorovie})")
        if kogo_atakuut.zdorovie < 0:
            print(f"Битва заверщена, {kogo_atakuut} погиб в бою смертью храбрых")
            break
        else:
            pass

    else:
        pass
