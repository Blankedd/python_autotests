import requests

token = "ce62ae5d8581a75d6aee66314fefb1e0"
appjs = "application/json"
response = requests.post("https://api.pokemonbattle.me:9104/pokemons", json = {
    "name": "Бульбазаврик",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
},
headers = {
    "Content-Type" : "application/json",
    "trainer_token" : 'ce62ae5d8581a75d6aee66314fefb1e0'
}
              )
print(response.text)




responserename = requests.put ("https://api.pokemonbattle.me:9104/pokemons", json = {
    "pokemon_id": "12581",
    "name": "PythonPokemon",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
},
headers = {
    "Content-Type" : "application/json",
    "trainer_token" : 'ce62ae5d8581a75d6aee66314fefb1e0'
}
              )
print(responserename.text)





responsepokeball = requests.post ("https://api.pokemonbattle.me:9104/trainers/add_pokeball", json = {
    "pokemon_id": "12581"
},
headers = {
    "Content-Type" : "application/json",
    "trainer_token" : 'ce62ae5d8581a75d6aee66314fefb1e0'
}
              )
print(responsepokeball.text)