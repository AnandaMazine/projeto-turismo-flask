from flask import Blueprint, request, jsonify

hotels_bp = Blueprint('hotels',__name__)

HOTELS_DB = [
    {
        "id": 1, 
        "nome_hotel": "Eco Pousada Beira Rio", 
        "estrelas": 4, 
        "valor_diaria": 350.00, 
        "cidade": "Iporanga"
    },
    {
        "id": 2, 
        "nome_hotel": "Porto Preguiças Resort", 
        "estrelas": 5, 
        "valor_diaria": 890.00, 
        "cidade": "Barreirinhas"
    }
]

@hotels_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todos os hotéis
    ---
    tags:
      - Hotels
    responses:
      200:
        description: Lista recuperada com sucesso
    """
    return jsonify(HOTELS_DB), 200

@hotels_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um hotel pelo ID
    ---
    tags:
      - Hotels
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Hotel encontrado
      404:
        description: Hotel não encontrado
    """
    res = next((h for h in HOTELS_DB if h['id'] == id), None)
    return jsonify(res) if res else (jsonify({"error": "Hotel não encontrado"}), 404)

# FUNÇÃO POST
@hotels_bp.route('/', methods=['POST'])
def create():
    """
    Cadastra um novo hotel
    ---
    tags:
      - Hotels
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            id:
              type: integer
            nome_hotel:
              type: string
            estrelas:
              type: integer
            valor_diaria:
              type: number
            cidade:
              type: string
    responses:
      201:
        description: Criado com sucesso
    """
    novo = request.get_json()
    HOTELS_DB.append(novo)
    return jsonify(novo),201

#FUNÇÃO PUT
@hotels_bp.route('/<int:id>', methods=['PUT'])
def update_hotels(id):
    """
    Atualizar dados de um hotel
    ---
    tags:
      - Hotels
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
            nome_hotel:
              type: string
            estrelas:
              type: integer
            valor_diaria:
              type: number
            cidade:
              type: string
    responses:
      200:
        description: Atualizado com sucesso
    """
    dados = request.get_json()
    hotel = next((h for h in HOTELS_DB if h['id'] == id), None)
    if hotel:
        hotel.update(dados)
        return jsonify(hotel), 200
    return jsonify({"error": "Hotel não encontrado"}), 404
   
#FUNÇÃO DELETE 
@hotels_bp.route('/<int:id>', methods=['DELETE'])
def delete_hotels(id):
    """
    Exclui um hotel
    ---
    tags:
      - Hotels
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Removido com sucesso
    """
    global HOTELS_DB
    HOTELS_DB = [h for h in HOTELS_DB if h['id'] != id]
    return jsonify({"message": "Removido"}), 200