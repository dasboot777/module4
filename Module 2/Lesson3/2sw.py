
import random
class Voin:
    def __init__(self, imya, zdorovie):
        self.zdorovie = zdorovie
        self.imya = imya

voin1 = Voin("Воин 1", 100)
voin2 = Voin("Воин 2", 100)

while voin1.zdorovie > 0 and voin2.zdorovie > 0:
    udar = random.randint(1, 3)
    if udar == 1:
        voin1.zdorovie -= 20
        print(f"{voin2.imya} (осталось здоровья = {voin2.zdorovie} ) атаковал {voin1.imya} (осталось здоровья = {voin1.zdorovie})")
    else:
        voin2.zdorovie -= 20
        print(f"{voin1.imya} (осталось здоровья = {voin1.zdorovie} )атаковал {voin2.imya} (осталось здоровья = {voin2.zdorovie})  ")
if voin1.zdorovie > voin2.zdorovie:
    print(f"Битва завершена, победил {voin1.imya}")
else:
    print(f"Битва завершена, победил {voin2.imya}")
