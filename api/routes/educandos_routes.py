from flask import Blueprint, request
from datetime import datetime
from models.educando import Educando
from models.insignia import Insignia
from models.insignia_conquistada import Insignia_conquistada

educandos_bp = Blueprint("educandos", __name__)

# OK
@educandos_bp.route("/educandos", methods=["GET"])
def get_educandos():
    try:
        return [educando.to_dict() for educando in Educando.listar_educandos()], 200
    except Exception as e:
        return {"error": str(e)}, 500

# OK
@educandos_bp.route("/educando/<id>", methods=["GET"])
def get_educando(id):
    educando = Educando.carregar_educando(id)
    if not educando:
        return {"error": "Educando não encontrado."}, 404
    return educando.to_dict(), 200

# OK
@educandos_bp.route("/educando/<id>/insignias", methods=["GET"])
def get_insignias_educando(id):
    educando = Educando.carregar_educando(id)
    if not educando:
        return {"error": "Educando não encontrado"}, 404

    return {
        "data": {
            "educando_id": id,
            "educando_nome": educando.nome,
            "insignias": educando.insignias
        }
    }, 200

# OK
@educandos_bp.route("/educando/conquista", methods=["POST"])
def post_conquista_insignia():
    data = request.get_json()

    educando = Educando.carregar_educando(data.get("educando_id"))
    if not educando:
        return {"error": "Educando não encontrado"}, 404
    insignia = Insignia.carregar_insignia(data.get("insignia_id"))
    if not insignia:
        return {"error": "Insignia não encontrada"}, 404
    nivel = data.get("nivel")
    if not nivel:
        return {"error": "Nível da insignia é obrigatoria"}, 400
    data_conquista = data.get("data_conquista")
    if not data_conquista:
        return {"error": "Data da conquista é obrigatória"}, 400

    educando.insignias.append(Insignia_conquistada(insignia.id, insignia.nome, nivel, data_conquista).to_dict())
    educando.gravar_educando()
    return {"message": "Insignia adicionada ao educando com sucesso!"}, 201

# OK
@educandos_bp.route("/educando/criar", methods=["POST"])
def post_criar_educando():
    data = request.get_json()
    educando = Educando(None, data.get("nome"), data.get("trilha"), data.get("unidade"), [])
    educando.gravar_educando()
    return {"message": "Educando gravado com o ID " + educando.id}, 201

# OK
@educandos_bp.route("/educando/<id>/editar", methods=['PUT'])
def put_atualizar_educando(id):
    data = request.get_json()
    educando = Educando.carregar_educando(id)
    if not educando:
        return {"error": "Educando não encontrado"}, 404

    if "nome" in data:
        educando.nome = data["nome"]
    if "trilha" in data:
        educando.trilha = data["trilha"]
    if "unidade" in data:
        educando.unidade = data["unidade"]
    if "insignias" in data:
        educando.insignias = data["insignia"]

    mensagem = educando.atualizar_educando()
    return {
        "status": "success",
        "mensagem" : mensagem
    },201

# OK
@educandos_bp.route("/educando/<id>/deletar", methods=['DELETE'])
def delete_deletar_educando(id):
    educando = Educando.carregar_educando(id)
    if not educando:
        return {"error": "Educando não encontrado"}, 404

    if Educando.remover_educando(educando):
        return {"message": "Educando removido com sucesso"}, 200

    return {"error": "Erro ao remover educando"}, 500
