from flask import Blueprint, request, jsonify

bookings_bp = Blueprint('bookings', __name__)

BOOKINGS_DB = [
    {
        "id": 1,
        "hospede": "Ananda Mazine",
        "hotel_id": 1,
        "data_reserva": "2026-04-15",
        "valor_total": 700.00,
        "status": "Confirmado"
    },
    {
        "id": 2,
        "hospede": "João Silva",
        "hotel_id": 2,
        "data_reserva": "2026-05-20",
        "valor_total": 1780.00,
        "status": "Pendente"
    }
]

@bookings_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todas as reservas
    ---
    tags:
      - Bookings
    responses:
      200:
        description: Lista recuperada com sucesso
    """
    return jsonify(TOURS_DB),200

@bookings_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista todas as reservas
    ---
    tags:
      - Bookings
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Reserva encontrada
      404:
        description: Reserva não encontrada
    """    
    res = next((b for b in BOOKINGS_DB if b['id'] == id), None)
    return jsonify(res) if res else (jsonify({"error":"Reserva não encontrado"}), 404)

@bookings_bp.route('/', methods=['POST'])
def create():
    """
    Criar uma nova Reserva
    ---
    tags:
      - Bookings
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            id:
               type: integer
            hospede:
                type: string
            data_reserva:
                type: string
            valor_total:
                type: number
            status:
                type: string            
    responses:
      201:
        description: Criado com sucesso
    """
    novo = request.get_json()
    BOOKINGS_DB.append(novo)
    return jsonify(novo), 201

@bookings_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar uma reserva
    ---
    tags:
      - Bookings
    parameters:
      - name: id
        in: path
        required: true
      - name: body
        in: body
        required: true
        schema:
           type: object
           properties:
              hospede:
                type: string
              data_reserva:
                type: string
              valor_total:
                type: number
              status:
                type: string
    responses:
      201:
        description: Atualizado com sucesso 
    """
    dados = request.get_json()
    booking = next((b for b in BOOKINGS_DB if b['id'] == id), None)
    if booking:
        booking.update(dados)
        return jsonify(booking), 201
    return jsonify({"error": "Reserva não encontrada"}), 404

@bookings_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui uma reserva
    ---
    tags:
      - Bookings
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
    TOURS_DB = [b for b in TOURS_DB if b['id'] != id]
    return jsonify({"message": "Removido"}), 200