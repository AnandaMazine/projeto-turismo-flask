from flask import Blueprint, request, jsonify

hotels_bp = Blueprint('hotels',__name__)

hotels = [
    {"id":1, "nome":"Hotel X", "localizacao":"São Paulo"},
    {"id":2, "nome":"Hotel Y", "localizacao":"Rio de Janeiro"}
]

@hotels_bp.route('/', methods=['GET'])
def get_hotels():
    return jsonify(hotels), 200

@hotels_bp.route('/', methods=['GET'])
def add_hotels():
    novo_dado = request.get_json()
    hotels.append(novo_dado)
    return jsonify({"mensagem": "Hotel adicionado"})