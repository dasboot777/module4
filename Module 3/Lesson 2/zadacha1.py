import vk_api
import random
# from  cbrf import get_dollar_course
import requests

vk = vk_api.VkApi(token="vk1.a.2WKH4g6AdSKYyXjzi0jm08QSLR3kNSzadLJ7rIESIviy39LlRr4G9ta0vcgc9IKaypCoHIP2CdmtB_zwGjDX2hyjNtdKKbPyM4p8bgUlZIajZ9P4976fdV68RneO-Gy603n0A8N9oMj2z0ogIHtDcGjqkncmRNfMzinnI_E4HO91BvtPGiHxkScg9gskNm09_S7AISfN2iPVFF4tclTz0A")

while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages['count'] >= 1:
        msg_text =messages["items"][0]["last_message"]["text"]#выводим сообщени из словаря

        if msg_text.lower() == "планеты":

            response = requests.get("https://swapi.dev/api/")
            planets_url = response.json()["planets"]
            planets_list = []

            for i in range(1, 10):
                response = requests.get(f"{planets_url}{i}")
                # print(response.json())
                data = response.json()
                data["diameter"] = int(data["diameter"])  # приводим к целочисл ти пу данных
                planets_list.append(data)

            planety = (max(planets_list, key=lambda x: x["diameter"])["name"])


            ans = f"Планета с максимальным диаметром это: {planety} "
        else:
            ans = "неизвестная команда"


        user_id = messages["items"][0]["last_message"]["from_id"]  # выводим сообщени из словаря
        vk.method(
            "messages.send",
            {
                'random_id': random.randint(-10 ** 7, 10 ** 7),
                'user_id': user_id,
                'message': ans
            }
        )






