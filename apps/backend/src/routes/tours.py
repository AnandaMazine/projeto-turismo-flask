from flask import Blueprint, request, jsonify

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
          type: object
          properties:
            id:
               type: integer
            nome_passeio:
                type: string
            duracao:
                type: string
            preco:
                type: number
            dificuldade:
                type: string
    responses:
      201:
        description: Criado com sucesso
    """
    novo = request.get_json()
    TOURS_DB.append(novo)
    return jsonify(novo), 201

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
           type: object
           properties:
             nome_passeio:
               type: string
             duracao:
               type: string
             preco:
               type: number
             dificuldade:
               type: string       
    responses:
       200:
          description: Atualizado com sucesso 
    """
    dados = request.get_json()
    tour = next ((t for t in TOURS_DB if t['id'] == id), None)
    if tour:
        tour.update(dados)
        return jsonify(tour), 200
    return jsonify({"error": "Passeio não encontrado"}), 404

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