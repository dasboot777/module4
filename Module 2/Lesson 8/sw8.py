#12/02/2023
import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime("%d.%m.%Y")#форматируем дату
print(today)

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp", params={"date_req": today})
# print(response)

soup = BeautifulSoup(response.content, features="xml")
# print(soup)

def get_currency(currency_id):
    valute = soup.find("Valute", ID=currency_id)#ищем по тегу Valute
    valute_value = valute.Value.text
    valute_name = valute.Name.text

    #создаем словарь
    valute_info = {"name": valute_name, "value": valute_value}
    return valute_info


# # currency_id = input("Введите id валюты:")
# currency_id = "R01010"
#
#
# #функция словаря
# # get_currency(currency_id)
#
# print(get_currency(currency_id)["name"])