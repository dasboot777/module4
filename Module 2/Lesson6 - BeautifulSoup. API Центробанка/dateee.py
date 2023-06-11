from datetime import datetime
# print(datetime.now().date().month)
# print(datetime.now().time().hour)

my_str = "17/01/2002"
#переводим строку  вдату
str_to_date = datetime.strptime(my_str, "%d/%m/%Y")
print((str_to_date.year))

#Обратно
date_to_str = datetime.now().strftime("%d/%m/%Y")
print(date_to_str)
