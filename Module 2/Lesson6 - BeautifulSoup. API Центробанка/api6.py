import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(response.content, features="xml")
# print(response.content)
# print(soup.find("Valute", ID="R01010"))#выводим австраллийский доллар
australian_dollar = soup.find("Valute", ID="R01010")
# print((australian_dollar.Value.text))
currency_value = australian_dollar.Value.text
currency_nominal = australian_dollar.Nominal.text
currency_name = australian_dollar.Name.text
currency_charcode = australian_dollar.CharCode.text

print(f"({currency_nominal} шт.) {currency_charcode} {currency_name} стоит {currency_value} рублей")
