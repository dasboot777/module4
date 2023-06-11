import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(response.content, features="xml")


valute_from = "EUR"
valute_to = "USD"

amount = int(input(f"Введите сумму {valute_from}, которую вы хотите конвертировать в {valute_to}: "))
#
def course(valute_from, valute_to, amount):
    #парсим данные валюты №1 EUR
    valute_from_data = soup.find("Valute", ID="R01239")
    from_currency_value = valute_from_data.Value.text
    from_currency_value = float(from_currency_value.replace(',', '.'))

    # print(type(from_currency_value))

    from_currency_nominal = valute_from_data.Nominal.text
    from_currency_name = valute_from_data.Name.text
    from_currency_charcode = valute_from_data.CharCode.text
    # print(from_currency_value, from_currency_charcode, from_currency_nominal, from_currency_name)
    #
    # # парсим данные валюты №2 USD
    valute_to_data = soup.find("Valute", ID="R01235")
    to_currency_value = valute_to_data.Value.text
    to_currency_value = float(to_currency_value.replace(',', '.'))


    to_currency_nominal = valute_to_data.Nominal.text
    to_currency_name = valute_to_data.Name.text
    to_currency_charcode = valute_to_data.CharCode.text
    # print(to_currency_value, to_currency_name, to_currency_charcode, to_currency_name)
    #
    itogo = (amount * int(from_currency_value)) / int(to_currency_value)

    if valute_from == "RUR":
        print(f"При конвертации {amount} {valute_from} Российских рублей получится {itogo} {valute_to} {to_currency_name}")
    else:
        print(f"При конвертации {amount} {valute_from} {from_currency_name} получится {itogo} {valute_to} {to_currency_name}")
#
course(valute_from, valute_to, amount)
