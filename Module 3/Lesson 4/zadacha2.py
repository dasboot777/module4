import contextlib
import  requests
from  bs4 import  BeautifulSoup

url = "http://www.cbr.ru/scripts/XML_daily.asp"

response = requests.get(url)
# print(response)
# print(response.content)

soup = BeautifulSoup(response.content, features="xml")

# print(soup)

@contextlib.contextmanager

def get_currency(currency_id):
    try:
        currency = soup.find("Valute", ID=currency_id)#ищем по тегу Valute
        currency_name = currency.Name.text
        currency_value = currency.Value.text
        currency_nominal = currency.Nominal.text
        currency_charcode = currency.CharCode.text
        znachenie = f"({currency_nominal} шт.) {currency_charcode} {currency_name} стоит(ят) {currency_value} рублей"
        # return znachenie
        yield znachenie

    except:
        yield "Такая валюта не найдена"

currency_id = input("Введите id валюты:")
# get_currency(currency_id)#вызываем в print
# print(get_currency(currency_id))

with get_currency(currency_id) as znachenie:
    print(znachenie)




# def exc_handler(*args):  # отлавливаем ошибку
#     try:
#         yield
#     except* args:
#         print("Ошибка, но мне все равно")
#
#
# my_list = [1, 2]
# with exc_handler(IndexError, ValueError, KeyError, AttributeError,
#                  SyntaxError):  # типы ошибок (игнорировать исключения)
#     my_list[4]  # намеренно строка с ошибкой
#     my_list(уууу)
