from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from ..schemas.tour_schema import TourSchema

tours_bp = Blueprint('tours', __name__)

TOURS_DB = [
    {
        "id": 1,
        "nome_passeio": "Trilha da Caverna do Diabo",
        "duracao": "4 horas",
        "preco": 120.00,
        "dificuldade": "Fácil"
    },
    {
        "id": 2,
        "nome_passeio": "Circuito Lagoa Azul (4x4)",
        "duracao": "5 horas",
        "preco": 250.00,
        "dificuldade": "Média"
    }
]

@tours_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todos os passeios
    ---
    tags:
      - Tours
    responses:
      200:
        description: Lista recuperada com sucesso
    """
    return jsonify(TOURS_DB), 200

@tours_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um passeio pelo ID
    ---
    tags:
      - Tours
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Passeio encontrado
      404:
        description: Passeio não encontrado
    """
    res = next((t for t in TOURS_DB if t['id'] == id), None)
    return jsonify(res) if res else (jsonify({"error":"Passeio não encontrado"}), 404)

@tours_bp.route('/', methods=['POST'])
def create():
    """
    Cadastra um novo passeio
    ---
    tags:
      - Tours
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/Tour'
    responses:
      201:
        description: Criado com sucesso
      400:
        description: Erro de Validação
        schema:
          $ref: '#/definitions/Error'
    """
    try:
        data = TourSchema(**request.json)
        TOURS_DB.append(data.model_dump())
        return jsonify(data.model_dump()), 201
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

@tours_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar um passeio
    ---
    tags:
      - Tours
    parameters:
      - name: id
        in: path
        required: true
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/Tour'
    responses:
      200:
        description: Atualizado com sucesso
      400:
        description: Erro de validação
        schema:
          $ref: '#/definitions/Error'
      404:
        description: Passeio não encontrado
    """
    tour = next((t for t in TOURS_DB if t['id'] == id), None)
    if not tour:
        return jsonify({"error": "Passeio não encontrado"}), 404
    try:
        dados = TourSchema(**request.json)
        tour.update(dados.model_dump())
        return jsonify(tour), 200
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

@tours_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um passeio
    ---
    tags:
      - Tours
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Removido com sucesso
    """
    global TOURS_DB
    TOURS_DB = [t for t in TOURS_DB if t['id'] != id]
    return jsonify({"message": "Removido"}), 200