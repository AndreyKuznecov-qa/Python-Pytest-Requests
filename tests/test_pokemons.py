import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '0f9d44e19d0bf4b9d7c60113c4237d45'

def test_status_code():
	response = requests.get(f'{host}/trainers', params = {'trainer_id': 4480 })
	assert response.status_code == 200, '''status_code ответа не равен 200'''
	
	

def test_part_of_body():
	response = requests.get(f'{host}/trainers', params = {'trainer_id': 4480 })
	assert "trainer_name" in response.json()
	assert response.json()["trainer_name"] == 'Kot_v_Sapogah', '''В ответе не пришло имя тренера'''