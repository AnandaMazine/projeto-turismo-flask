from flask import Blueprint, request, jsonify
from database import db
from models import Hotel
from pydantic import ValidationError
from schemas.hotel_schema import HotelSchema

hotels_bp = Blueprint('hotels', __name__, url_prefix='/hotels')

@hotels_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todos os hotéis
    ---
    tags:
      - Hotels
    responses:
      200:
        description: OK
    """
    hoteis = Hotel.query.all()
    result = [HotelSchema(**h.to_dict()).model_dump() for h in hoteis]
    return jsonify(result), 200

@hotels_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um hotel pelo ID
    ---
    tags:
      - Hotels
    responses:
      200:
        description: OK
    """
    hotel = Hotel.query.get(id)

    if not hotel:
        return jsonify({"error": "Hotel não encontrado"}), 404
    return jsonify(hotel.to_dict()), 200

# FUNÇÃO POST
@hotels_bp.route('/', methods=['POST'])
def create():
    """
    Cadastra um novo hotel
    ---
    tags:
      - Hotels
    responses:
      200:
        description: OK
    """
    try:
        data = HotelSchema(**request.json)
        novo_hotel = Hotel(**data.model_dump())
        db.session.add(novo_hotel)
        db.session.commit()

        return jsonify(novo_hotel.to_dict()), 201
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

#FUNÇÃO PUT
@hotels_bp.route('/<int:id>', methods=['PUT'])
def update_hotels(id):
    """
    Atualizar dados de um hotel
    ---
    tags:
      - Hotels
    responses:
      200:
        description: OK
    """
    hotel = Hotel.query.get(id)

    if not hotel:
        return jsonify({"error": "Hotel não encontrado"}), 404
   
    try:
        data = request.json
        hotel.nome_hotel = data.get('nome_hotel', hotel.nome_hotel)
        hotel.estrelas = data.get('estrelas', hotel.estrelas)
        hotel.valor_diaria = data.get('valor_diaria', hotel.valor_diaria)
        hotel.cidade = data.get('cidade', hotel.cidade)
        db.session.commit()
        return jsonify(hotel.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
#FUNÇÃO DELETE 
@hotels_bp.route('/<int:id>', methods=['DELETE'])
def delete_hotels(id):
    """
    Exclui um hotel
    ---
    tags:
      - Hotels
    responses:
      200:
        description: OK
    """
    hotel = Hotel.query.get(id)

    if not hotel:
        return jsonify ({"error": "Hotel não encontrado"}), 404
    
    db.session.delete(hotel)
    db.session.commit()

    return jsonify({"message": "Hotel removido com sucesso"}), 200