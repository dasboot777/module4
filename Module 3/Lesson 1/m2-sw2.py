class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee

    def info(self):#инициализируем вывод сотрудников
        print(f'У {self.name} зарплата равна {self.salary}, статус работника: {"В отпуске." if self.on_vacation else "На работе."} {"Это хороший сотрудник." if self.is_good_employee else "Это плохой работник: рекомендуется к увольнению."}')

    def uvolnenie(self):#инициализируем вывод при увольнении
        print(f'--------------------------------------------------------' '\n'    
              f'Плохой сотрудник {self.name} уволен. Он зря получал зарплату: {self.salary} рублей.')

#создаем сотрудников на основе шаблона класса (экземпляры класса)
employee1 = Employee('Данил', 225_000, True, True)
employee2 = Employee('Алина', 224_000, True, False)
employee3 = Employee('Андрей', 223_000, False, True)
employee4 = Employee('Вася', 221_000, True, True)
employee5 = Employee('Сирожа', 222_000, True, True)

my_list = []# создаем пустой список и добавляем сотрудников

my_list.append(employee1)
my_list.append(employee2)
my_list.append(employee3)
my_list.append(employee4)
my_list.append(employee5)

for employee in my_list:#проходим по созданному списку и выводим инфу по шаблону info
    employee.info()


for employee in my_list:# удаляем плохих работников
    if employee.is_good_employee == False:
        my_list.remove(employee)
        employee.uvolnenie()
print(f'--------------------------------------------------------' '\n'     
      f'Все плохие сотрудники уволены. В организации остались только хорошие сотрудники ')

#конечный список сотрудников
for employee in my_list:#проходим по созданному списку и выводим инфу по шаблону info
    employee.info()