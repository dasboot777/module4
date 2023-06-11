import requests

api = requests.get('https://swapi.dev/api/starships/').json()['results']

# Выводим название самого быстрого корабля
print(max(((x['name'], x['max_atmosphering_speed']) for x in api),
    key=lambda x: int(x[1].replace('n/a', '0').replace('km', '')))[0])
