import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(response.content, features="xml")
print(soup)



def get_course(currency_id):
    australian_dollar = soup.find("Valute", ID=currency_id)
    # print(australian_dollar)
    currency_value = australian_dollar.Value.text
    currency_nominal = australian_dollar.Nominal.text
    currency_name = australian_dollar.Name.text

    print(f"({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value} рублей")

currencies_list = soup.find_all("Valute")
for currency in currencies_list:
    # print(currency["ID"])
    get_course(currency["ID"])
