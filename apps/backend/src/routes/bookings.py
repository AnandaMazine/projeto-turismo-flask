from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from ..schemas.booking_schema import BookingSchema

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
    return jsonify(BOOKINGS_DB), 200

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
          $ref: '#/definitions/Booking'
    responses:
      201:
        description: Criado com sucesso
      400:
        description: Erro de Validação
        schema:
          $ref: '#/definitions/Error'
    """
    try:
      data = BookingSchema(**request.json)
      BOOKINGS_DB.append(data.model_dump())
      return jsonify(data.model_dump()), 201
    except ValidationError as err:
      return jsonify({"errors": err.errors()}), 400

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
          $ref: '#/definitions/Booking'
    responses:
      200:
        description: Atualizado com sucesso
      400:
        description: Erro de validação
        schema:
          $ref: '#/definitions/Error'
      404:
        description: Reserva não encontrada
    """
    booking = next((b for b in BOOKINGS_DB if b['id'] == id), None)
    if not booking:
      return jsonify({"error": "Reserva não encontrada"}), 404
    try:
      dados = BookingSchema(**request.json)
      booking.update(dados.model_dump())
      return jsonify(booking), 200
    except ValidationError as err:
      return jsonify({"errors": err.errors()}), 400
    

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
    global BOOKINGS_DB
    BOOKINGS_DB = [b for b in BOOKINGS_DB if b['id'] != id]
    return jsonify({"message": "Removido"}), 200
