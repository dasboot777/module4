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


#создаем экземпляры класса
user1 = User("Самолет-Истребитель", 100, random.randint(25, 50))
user2 = User("Самолет-бомбардировщик", 150, random.randint(20, 30))

while user1.zdorovie > 0 and user2.zdorovie > 0:
    kto_atakuet = random.choice([user1, user2])
    print(f"Первым атакует {kto_atakuet}")
    if kto_atakuet == user1:
        #вызываем метод атаки
        user1.attack(user2)
        print(f"{user1} (осталось здоровья {user1.zdorovie}) атаковал и нанес урон {user1.uron} {user2} (осталось здоровья {user2.zdorovie})")
    else:
        user2.attack(user1)
        print(f"{user2} (осталось здоровья {user2.zdorovie}) атаковал и нанес урон {user2.uron} {user1} (осталось здоровья {user1.zdorovie})")

if user1.zdorovie > user2.zdorovie:
    print((f"Битва завершена, победил {user1} "))
else:
    print((f"Битва завершена, победил {user2} "))

