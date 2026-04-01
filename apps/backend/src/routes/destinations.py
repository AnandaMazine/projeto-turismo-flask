from flask import Blueprint, request, jsonify
from database import db
from models import Destination
from schemas.destination_schema import DestinationSchema
from pydantic import ValidationError

destinations_bp = Blueprint('destinations', __name__, url_prefix='/destinations')

@destinations_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todos os destinos do banco de dados
    ---
    tags:
      - Destinations
    responses:
      200:
        description: OK
    """
    destinos = Destination.query.all()
    result = [DestinationSchema(**d.to_dict()).model_dump() for d in destinos]
    return jsonify(result), 200

@destinations_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Busca um destino específico pelo seu ID
    ---
    tags:
      - Destinations
    responses:
      200:
        description: OK
    """
    destino = Destination.query.get(id)
    
    if not destino:
        return jsonify({"error": "Destino não encontrado"}), 404

    return jsonify(destino.to_dict()), 200

@destinations_bp.route('/', methods=['POST'])
def create():
    """
    Cadastra um novo destino
    ---
    tags:
      - Destinations
    responses:
      200:
        description: OK
    """
    try:
        data = DestinationSchema(**request.json)
        novo_destino = Destination(**data.model_dump())
        db.session.add(novo_destino)
        db.session.commit()
        
        return jsonify(novo_destino.to_dict()), 201
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

@destinations_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualiza um destino existente
    ---
    tags:
      - Destinations
    responses:
      200:
        description: OK
    """
    destino = Destination.query.get(id)
    
    if not destino:
        return jsonify({"error": "Destino não encontrado"}), 404
        
    try:
        data = request.json
        destino.nome = data.get('nome', destino.nome)
        destino.cidade = data.get('cidade', destino.cidade)
        destino.estado = data.get('estado', destino.estado)
        destino.pais = data.get('pais', destino.pais)
        
        db.session.commit()
        return jsonify(destino.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@destinations_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Remove um destino
    ---
    tags:
      - Destinations
    responses:
      200:
        description: OK
    """
    destino = Destination.query.get(id)
    
    if not destino:
        return jsonify({"error": "Destino não encontrado"}), 404
        
    db.session.delete(destino)
    db.session.commit()
    
    return jsonify({"message": "Destino removido com sucesso"}), 200