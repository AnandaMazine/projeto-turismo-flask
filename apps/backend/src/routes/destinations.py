from flask import Blueprint, request, jsonify

destinations_bp = Blueprint('destinations', __name__)

# Simulação de Banco de Dados
destinos = [
    {"id": 1, "nome": "Paris", "pais": "França"},
    {"id": 2, "nome": "Miracatu", "pais": "Brasil"}
]

# 1. READ (GET) - Listar todos
@destinations_bp.route('/', methods=['GET'])
def get_destinations():
    return jsonify(destinos), 200

# 2. CREATE (POST) - Adicionar novo
@destinations_bp.route('/', methods=['POST'])
def add_destination():
    novo_dado = request.get_json() # Pega o que o usuário enviou
    destinos.append(novo_dado)
    return jsonify({"mensagem": "Destino adicionado!", "dados": novo_dado}), 201

# 3. UPDATE (PUT) - Editar um existente
@destinations_bp.route('/<int:id>', methods=['PUT'])
def update_destination(id):
    dados_atualizados = request.get_json()
    for d in destinos:
        if d['id'] == id:
            d.update(dados_atualizados)
            return jsonify({"mensagem": "Atualizado com sucesso", "destino": d}), 200
    return jsonify({"erro": "Não encontrado"}), 404

# 4. DELETE (DELETE) - Remover
@destinations_bp.route('/<int:id>', methods=['DELETE'])
def delete_destination(id):
    global destinos
    destinos = [d for d in destinos if d['id'] != id]
    return jsonify({"mensagem": f"Destino {id} removido"}), 200