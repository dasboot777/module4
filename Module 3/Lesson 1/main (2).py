# name = "Иван"
# salary = 200_000

# print('У ' + name + ' зарплата равна ' + str(salary))
# print(f'У {name} зарплата равна {salary}')
#
# print('У {name1} зарплата равна {salary1}'.format(
#     name1=name,
#     salary1=salary
# ))

# employee = {'name': 'Иван', 'salary': 200_000, 'on_vacation': True}
# print(f'У {employee.get("name")} зарплата равна {employee.get("salary")}')
# on_vacation = "в отпуске " if employee.get('on_vacation') else 'на работе'
#
# print(on_vacation)

# employees_list = [
#     {
#         'name': 'Данил',
#         'salary': 200_000,
#     },
#
#     {
#         'name': 'Алина',
#         'salary': 250_000,
#     },
#
#     {
#         'name': 'Андрей',
#         'salary': 225_000,
#     }
#
# ]

# for employee in employees_list:
#     print(f'У {employee.get("name")} зарплата равна {employee.get("salary")}')

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f'У {self.name} зарплата равна {self.salary}')


employee1 = Employee('Данил', 200_000)
employee2 = Employee('Алина', 250_000)
employee3 = Employee('Андрей', 225_000)

my_list = []

my_list.append(employee1)
my_list.append(employee2)
my_list.append(employee3)

for employee in my_list:
    employee.info()

my_list.remove(employee3)
print(my_list)
