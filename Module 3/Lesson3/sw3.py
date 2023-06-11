import vk_api
from  vk_api.longpoll import VkLongPoll, VkEventType
import random
from  cbrf import get_course, find_valute
from wiki import get_article

vk_session = vk_api.VkApi(token="vk1.a.2WKH4g6AdSKYyXjzi0jm08QSLR3kNSzadLJ7rIESIviy39LlRr4G9ta0vcgc9IKaypCoHIP2CdmtB_zwGjDX2hyjNtdKKbPyM4p8bgUlZIajZ9P4976fdV68RneO-Gy603n0A8N9oMj2z0ogIHtDcGjqkncmRNfMzinnI_E4HO91BvtPGiHxkScg9gskNm09_S7AISfN2iPVFF4tclTz0A")
#удалили осла
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():#генераттор событий, перебор по событиям
    # print(event)
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        # print(user_message)
        if user_message[0:2] == "-к":
            # response = "Курс доллара {0} руб. за 1 шт. \n Курс евро {1} руб. за 1 шт. \n Курс Юаня {2} руб. за 1 шт. ".format(
            #     get_course("R01235"), get_course("R01239"), get_course("R01375")
            # )
            user_currency = user_message[2:]
            response = f'Вот что я нашел: {find_valute(user_currency)}'
            print(user_currency)
            print(user_message)

        elif user_message[0:2] == "-в":
            article = user_message[2:]
            response = f'Вот что я нашел: \n\n{get_article(article)}'

        else:
            response = "Не знаю такой команды"
        vk.messages.send(user_id=event.user_id, message=response, random_id=random.randint(-10 ** 7, 10 ** 7))



