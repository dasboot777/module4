import  requests
from  bs4 import  BeautifulSoup

url = "http://www.cbr.ru/scripts/XML_daily.asp"

response = requests.get(url)
# print(response)
# print(response.content)

soup = BeautifulSoup(response.content, features="xml")

# print(soup)

def get_dollar_course():
    return soup.find("Valute", ID="R01235").Value.text

# get_dollar_course()



