import requests
import pytest



def test_status_code():
    response = requests.get("https://api.pokemonbattle.me:9104/trainers", params = {'trainer_id' :2667} )
    assert response.status_code == 200
    
def test_part_of_body():
     response = requests.get("https://api.pokemonbattle.me:9104/trainers", params = {'trainer_id' :2667} )
     assert response.json()["trainer_name"] == "dd"