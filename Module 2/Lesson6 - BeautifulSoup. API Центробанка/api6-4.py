import requests
from bs4 import BeautifulSoup

user_currency = input("Введите первые буквы валюты, которую нужно найти: ").capitalize()


response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(response.content, features="xml")

currencies_list = soup.find_all("Valute")
for currency in currencies_list:
    currency_name = currency.Name.text
    currency_value = currency.Value.text
    currency_nominal = currency.Nominal.text
    currency_charcode = currency.CharCode.text

#endswith - на что заканчивается строка
    if currency_name.startswith(user_currency):#поиск по начальным буквам
        print(f"({currency_nominal} шт.) {currency_charcode} {currency_name} стоит(ят) {currency_value} рублей")

