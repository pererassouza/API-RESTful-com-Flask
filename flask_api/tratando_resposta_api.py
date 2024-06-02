import json

dataname = 'json/data.json'

with open(dataname, 'r') as json_file:
    data = json.load(json_file)


def mostrar_valores_json(json_file: dict):
    for i in json_file['participantes']:
        id = i['id'] - 1
        nome_participante = json_file['participantes'][id]['nome']
        classe_evento = json_file['participantes'][id]['classe_evento']
        idade = json_file['participantes'][id]['idade']
        print(f'Nome: {nome_participante} | Idade: {idade} |\
 Classe: {classe_evento}')


mostrar_valores_json(data)
