class Employee:
    def __init__(self, name, salary, on_vacation):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation

    def info(self):
        print(f'У {self.name} зарплата равна {self.salary}, статус работника: {"В отпуске." if self.on_vacation else "На работе."}')


employee1 = Employee('Данил', 225_000, True)
employee2 = Employee('Алина', 224_000, True)
employee3 = Employee('Андрей', 223_000, False)
employee4 = Employee('Вася', 221_000, True)
employee5 = Employee('Сирожа', 222_000, True)

my_list = []

my_list.append(employee1)
my_list.append(employee2)
my_list.append(employee3)
my_list.append(employee4)
my_list.append(employee5)

for employee in my_list:
    employee.info()

# my_list.remove(employee3)
# print(my_list)

