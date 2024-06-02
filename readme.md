# API Flask e Scripts Python para Manipulação de Dados JSON

Este repositório contém um projeto simples em Flask para criar uma API RESTful que fornece informações sobre participantes de um evento. Além disso, inclui scripts Python para consumir essa API e manipular dados JSON localmente.

## Arquivos do Projeto

### `criando_api.py`

Este arquivo contém o código para criar uma API RESTful usando Flask. A API fornece dois endpoints:

- `/participantes`: Retorna todos os participantes do evento.
- `/participante/<id>`: Retorna informações de um participante específico com base no ID fornecido.

Exemplo de dados dos participantes:

```python
participantes_evento = [
    {'id': 1, 'nome': 'Felipe', 'idade': 25, 'classe_evento': 'vip'},
    {'id': 2, 'nome': 'Ana', 'idade': 31, 'classe_evento': 'pista'},
    {'id': 3, 'nome': 'Carlos', 'idade': 42, 'classe_evento': 'pista'},
    {'id': 4, 'nome': 'Cassia', 'idade': 39, 'classe_evento': 'vip'},
]
```

### `consumindo_api.py`

Este script consome a API Flask definida em `criando_api.py` usando a biblioteca `requests` do Python. Ele possui duas funções:

- `get_participantes(url)`: Obtém todos os participantes da API e salva os dados em um arquivo JSON local (`json/data.json`).
- `get_participante(id, url)`: Obtém as informações de um participante específico com base no ID e imprime os dados na tela.

### `tratando_api.py`

Este script lê os dados JSON salvos localmente (`json/data.json`) usando a biblioteca `json` do Python. Ele possui a função `mostrar_valores_json(json_file)` que imprime na tela os detalhes de cada participante, como nome, idade e classe de evento.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas Python: Flask, requests

## Como Usar

1. **Executar a API Flask**:
   ```bash
   python criando_api.py
   ```

2. **Consumir a API**:
   ```bash
   python consumindo_api.py
   ```

3. **Manipular Dados JSON Localmente**:
   ```bash
   python tratando_api.py
   ```

Certifique-se de modificar as URLs base (`URL_BASE`) nos scripts `consumindo_api.py` e `tratando_api.py` conforme necessário para corresponder à URL onde a API Flask está sendo executada.

