# https://swapi.dev/api/
import requests
response = requests.get("https://swapi.dev/api/")
# print(response.json())

planets_url = response.json()["planets"]
# print(planets_url)

# response = requests.get(planets_url)
# print(response.json())

# https://swapi.dev/api/planets/

planets_list = []

for i in range(1, 10):
    response = requests.get(f"{planets_url}{i}")
    # print(response.json())
    data = response.json()
    data["diameter"] = int(data["diameter"])#приводим к целочисл ти пу данных
    planets_list.append(data)

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

print(max(planets_list, key=lambda x: x["diameter"])["name"])
# print(max(planets_list, key=lambda x: x["diameter"]))
# print(max(((x['name'], x['diameter']) for x in planets_list)))