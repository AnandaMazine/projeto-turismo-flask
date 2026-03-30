from flask import Blueprint, request, jsonify

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
    Cadastra um novo destino
    ---
    tags:
      - Destinations
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            id:
              type: integer
            nome:
              type: string
            cidade:
              type: string
            estado:
              type: string
            pais:
              type: string
    responses:
      201:
        description: Criado com sucesso
    """
    novo = request.get_json()
    DESTINATIONS_DB.append(novo)
    return jsonify(novo), 201

# FUNÇÃO PUT
@destinations_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualiza dados de um destino
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
          type: object
          properties:
            nome:
              type: string
            cidade:
              type: string
            estado:
              type: string
            pais:
              type: string
    responses:
      200:
        description: Atualizado com sucesso
    """
    dados = request.get_json()
    destino = next((d for d in DESTINATIONS_DB if d['id'] == id), None)
    if destino:
        destino.update(dados)
        return jsonify(destino), 200
    return jsonify({"error": "Not found"}), 404

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