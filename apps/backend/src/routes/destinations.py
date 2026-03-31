from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from ..schemas.destination_schema import DestinationSchema
from models import Destination

destinations_bp = Blueprint('destinations', __name__)

DESTINATIONS_DB = [
    {
        "id": 1, 
        "nome": "Caverna do Diabo", 
        "cidade": "Eldorado", 
        "estado": "SP", 
        "pais": "Brasil"
    },
    {
        "id": 2, 
        "nome": "Parque Nacional dos Lençóis Maranhenses", 
        "cidade": "Barreirinhas", 
        "estado": "MA", 
        "pais": "Brasil"
    }
]

# FUNÇÃO GET ALL
@destinations_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todos os destinos turísticos
    ---
    tags:
      - Destinations
    responses:
      200:
        description: Lista recuperada com sucesso
    """
    return jsonify(DESTINATIONS_DB), 200

# FUNÇÃO GET BY ID
@destinations_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um destino pelo ID
    ---
    tags:
      - Destinations
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Destino encontrado
      404:
        description: Destino não encontrado
    """
    res = next((d for d in DESTINATIONS_DB if d['id'] == id), None)
    return jsonify(res) if res else (jsonify({"error": "Destino não encontrado"}), 404)

# FUNÇÃO POST
@destinations_bp.route('/', methods=['POST'])
def create():
    """
    Criar um novo destino
    ---
    tags:
      - Destinations
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/Destination'
    responses:
      201:
        description: Criado com sucesso
      400:
        description: Erro de validação
        schema:
          $ref: '#/definitions/Error'
    """
    try:
        data = DestinationSchema(**request.json)
        DESTINATIONS_DB.append(data.model_dump())
        return jsonify(data.model_dump()), 201
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

# FUNÇÃO PUT
@destinations_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualiza um destino existente
    ---
    tags:
      - Destinations
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/Destination'
    responses:
      200:
        description: Atualizado com sucesso
      400:
        description: Erro de validação
        schema:
          $ref: '#/definitions/Error'
      404:
        description: Destino não encontrado
    """
    destino = next((d for d in DESTINATIONS_DB if d['id'] == id), None)
    if not destino:
        return jsonify({"error": "Destino não encontrado"}), 404
    try:
        dados = DestinationSchema(**request.json)
        destino.update(dados.model_dump())
        return jsonify(destino), 200
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

# FUNÇÃO DELETE
@destinations_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um destino
    ---
    tags:
      - Destinations
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Removido com sucesso
    """
    global DESTINATIONS_DB
    DESTINATIONS_DB = [d for d in DESTINATIONS_DB if d['id'] != id]
    return jsonify({"message": "Removido"}), 200