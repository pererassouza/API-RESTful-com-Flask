import requests
import json


URL_BASE = 'http://127.0.0.1:5000'


def get_participantes(url: str):
    try:
        response = requests.get(f'{url}/participantes')
        if response.status_code == 200:
            participantes = response.json()

            with open('json/data.json', 'w') as json_file:
                json.dump(participantes, json_file, indent=4)
                print('Dados salvos com sucesso em (json/data.json)')
        else:
            print("Erro ao obter participantes")
    except Exception as e:
        print(f"Error: {e}")


def get_participante(id, url):
    try:
        response = requests.get(f'{url}/participante/{id}')
        if response.status_code == 200:
            participante = response.json()
            print(participante)
        else:
            print("Erro ao obter dados do participante")

    except Exception as e:
        print(f'Ocorreu um erro em: {e}')


get_participantes(URL_BASE)
get_participante(5, URL_BASE)
