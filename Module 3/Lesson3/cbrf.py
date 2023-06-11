import  requests
from  bs4 import  BeautifulSoup
global user_currency

url = "http://www.cbr.ru/scripts/XML_daily.asp"

response = requests.get(url)
# print(response)
# print(response.content)

soup = BeautifulSoup(response.content, features="xml")


# print(soup)

def get_course(course_id):
    return soup.find("Valute", ID=course_id).Value.text

# get_dollar_course()



