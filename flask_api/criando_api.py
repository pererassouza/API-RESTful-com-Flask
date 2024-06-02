from flask import Flask, jsonify


app = Flask(__name__)

participantes_evento = [
    {'id': 1, 'nome': 'Felipe', 'idade': 25, 'classe_evento': 'vip'},
    {'id': 2, 'nome': 'Ana', 'idade': 31, 'classe_evento': 'pista'},
    {'id': 3, 'nome': 'Carlos', 'idade': 42, 'classe_evento': 'pista'},
    {'id': 4, 'nome': 'Cassia', 'idade': 39, 'classe_evento': 'vip'},
]


@app.route("/participantes", methods=['GET'])
def get_participantes():
    return jsonify({'participantes': participantes_evento})


@app.route("/participante/<int:id>")
def get_participante(id):
    participante = next((participante for participante in
                         participantes_evento if participante['id'] == id),
                        None)

    if participante:
        return jsonify(participante)
    return jsonify({"error", 'participante não encontrado'}), 404


if __name__ == "__main__":
    app.run(debug=True)
