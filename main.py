import requests

token = '55bef3ca8453f04951cfb979aca10ffc'
host = 'https://api.pokemonbattle.me:9104'


'''response = requests.post(f'{host}/pokemons', json = {
    "name": "Черезард",
    "photo": "https://dolnikov.ru/pokemons/albums/006.png"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})
print(response.text)

response_name = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "26992",
    "name": "Биба",
    "photo": "https://dolnikov.ru/pokemons/albums/087.png"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(response_name.text)'''

response_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "26992"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(response_pokeball.status_code)

if response_pokeball.status_code == 200:
    print('Так и надо!')
else:
	print('Так не надо!')
      




      




