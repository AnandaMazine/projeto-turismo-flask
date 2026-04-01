from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Tour
from pydantic import ValidationError
from ..schemas.tour_schema import TourSchema

tours_bp = Blueprint('tours', __name__, url_prefix='/tours')

@tours_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todos os passeios
    ---
    tags:
      - Tours
    responses:
      200:
        description: OK
    """
    passeios = Tour.query.all()
    result = [TourSchema(**t.to_dict()).model_dump() for t in passeios]
    return jsonify(result), 200

@tours_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um passeio pelo ID
    ---
    tags:
      - Tours
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do registro
    responses:
      200:
        description: OK
    """
    passeio = Tour.query.get(id)

    if not passeio:
      return jsonify({"error":"Passeio não encontrado"}), 404
    return jsonify(passeio.to_dict()), 200

@tours_bp.route('/', methods=['POST'])
def create():
    """
    Cadastra um novo passeio
    ---
    tags:
      - Tours
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Tour'
    responses:
      200:
        description: OK
    """
    try:
        data = TourSchema(**request.json)
        novo_passeio = Tour (**data.model_dump())
        db.session.add(novo_passeio)
        db.session.commit()

        return jsonify(novo_passeio.to_dict()), 201
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
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Tour'
    responses:
      200:
        description: OK
    """
    tour = Tour.query.get(id)

    if not tour:
        return jsonify({"error": "Passeio não encontrado"}), 404
    
    try:
        data = request.json
        tour.nome_passeio = data.get('nome_passeio', tour.nome_passeio)
        tour.duracao = data.get('duracao', tour.duracao)
        tour.preco = data.get('preco', tour.preco)
        tour.dificuldade = data.get('dificuldade', tour.dificuldade)
        
        db.session.commit()
        return jsonify(tour.to_dict()), 200
    except Exception as e:
        return jsonify({"errors": str(e)}), 400

@tours_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um passeio
    ---
    tags:
      - Tours
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do registro a ser removido
    responses:
      200:
        description: OK
      404:
        description: Não encontrado
    """
    passeio = Tour.query.get(id)

    if not passeio:
        return jsonify({"error": "Passeio nao encontrado"}), 404
    
    db.session.delete(passeio)
    db.session.commit()
    
    return jsonify({"message": "Passeio removido com sucesso"}), 200