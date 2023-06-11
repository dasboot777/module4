# https://swapi.dev/api/
# API — starships_api = response.get('starships')
# Максимальная скорость — max_atmosphering_speed

import requests
response = requests.get("https://swapi.dev/api/")
# print(response.json())

starships_api = response.json()["starships"]
# print(starships_api)

# response = requests.get(planets_url)
# print(response.json())

# https://swapi.dev/api/planets/

starships_list = []
max_speed = 0
fastest_ship = ""

for i in range(1, 6):
    response = requests.get(f"{starships_api}{i}")
    # print(response.json())
    data = response.json()
    # if data.get("max_atmosphering_speed") == "n/a":
    #     data["max_atmosphering_speed"] = 0
    #
    # data["max_atmosphering_speed"] = int(data["max_atmosphering_speed"])#приводим к целочисл ти пу данных
    # starships_list.append(data)

    speed = data.get("max_atmosphering_speed")
    if speed == "n/a":
        speed = 0
    if speed == "1000km":
        speed = 1000
    speed = int(speed)
    if speed > max_speed:
        max_speed = speed
        fastest_ship = data.get("name")
    starships_list.append(data)
print("The fastest ship is:", fastest_ship)

# #сортировка диаметра плаент
# max_diameter = 0
# for planet in planets_list:
#     if planet["diameter"] > max_diameter:
#         max_diameter = planet["diameter"]
# # print(max_diameter)
# for planet in planets_list:
#     if planet ["diameter"] == max_diameter:
#         print(planet)
#         break
#

# print(max(starships_list, key=lambda x: x["max_atmosphering_speed"]))