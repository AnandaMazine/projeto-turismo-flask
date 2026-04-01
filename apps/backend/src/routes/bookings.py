from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Booking
from ..schemas.booking_schema import BookingSchema
from pydantic import ValidationError

bookings_bp = Blueprint('bookings', __name__, url_prefix='/bookings')

@bookings_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todas as reservas
    ---
    tags:
      - Bookings
    responses:
      200:
        description: OK
    """
    bookings = Booking.query.all()
    result = [BookingSchema(**b.to_dict()).model_dump() for b in bookings]
    return jsonify(result), 200

@bookings_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista uma reseva específica pelo ID
    ---
    tags:
      - Bookings
    responses:
      200:
        description: OK
    """
    reserva = Booking.query.get(id)

    if not reserva:
        return jsonify({"error": "Reserva não encontrada"}), 404
    
    return jsonify(reserva.to_dict()), 200


@bookings_bp.route('/', methods=['POST'])
def create():
    """
    Criar uma nova Reserva
    ---
    tags:
      - Bookings
    responses:
      200:
        description: OK
    """
    try:
       data = BookingSchema(**request.json)
       nova_reserva = Booking(**data.model_dump())
       db.session.add(nova_reserva)
       db.session.commit()
       
       return jsonify(nova_reserva.to_dict()),201
    except ValidationError as err:
      return jsonify({"errors": err.errors()}), 400

@bookings_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar uma reserva existente
    ---
    tags:
      - Bookings
    responses:
      200:
        description: OK
    """
    reserva = Booking.query.get(id)

    if not reserva:
        return jsonify ({"error": "Reserva não encontrada"}), 404
    try:
        data = request.json
        reserva.hospede = data.get('hospede', reserva.hospede)
        reserva.data_reserva = data.get('data_reserva', reserva.data_reserva)
        reserva.valor_total = data.get('valor_total', reserva.valor_total)
        reserva.status = data.get('status', reserva.status)
        reserva.hotel_id = data.get('hotel_id', reserva.hotel_id)
        
        db.session.commit()
        return jsonify(reserva.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bookings_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui uma reserva
    ---
    tags:
      - Bookings
    responses:
      200:
        description: OK
    """  
    reserva = Booking.query.get(id)

    if not reserva:
        return jsonify({"error": "Reserva não encontrada"}), 404
    
    db.session.delete(reserva)
    db.session.commit()

    return jsonify({"mensagem":"Reserva removida com sucesso"}), 200

