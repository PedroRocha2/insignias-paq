from flask import Blueprint, request
from models.insignia import Insignia
from models.educando import Educando

insignias_bp = Blueprint("insignias", __name__)

# OK
@insignias_bp.route("/insignias", methods=["GET"])
def get_insignias():
    try:
        return [insignia.to_dict() for insignia in Insignia.listar_insignias()], 200
    except Exception as e:
        return {"error": str(e)}, 500

# OK
@insignias_bp.route("/insignia/<id>", methods=["GET"])
def get_requisitos(id):
    insignia = Insignia.carregar_insignia(id)
    if not insignia:
        return {"error": "Insignia não encontrada."}, 404
    return insignia.to_dict(), 200

# OK
@insignias_bp.route("/insignia/<id>/educandos", methods=["GET"])
def get_educandos_por_insignia(id):
    educandos = Educando.listar_educandos_com_insignia_conquistada(id)
    if not educandos:
        return {"error": "Educandos não encontrados."}, 404
    return [{
        "id": educando.id,
        "nome": educando.nome,
    } for educando in educandos], 200

# OK
@insignias_bp.route("/insignias/conquistadas", methods=["GET"])
def get_insignias_conquistadas():
    insigniasConquistadas = {}
    educandos = Educando.listar_educandos()
    for educando in educandos:
        insigniasDoEducando = [insignia for insignia in educando.insignias]
        for insignia in insigniasDoEducando:
            if insignia['nome'] in insigniasConquistadas:
                insigniasConquistadas[insignia['nome']] += 1
            else:
                insigniasConquistadas[insignia['nome']] = 1
    listaInsignias = [{"nome": nome, "quantidade": quantidade} for nome, quantidade in insigniasConquistadas.items()]
    ordenadaPorQuantidade = sorted(listaInsignias, key=lambda insignia: insignia["quantidade"], reverse=True)
    if not insigniasConquistadas:
        return {"error": "Insignias não encontradas."}, 404
    return ordenadaPorQuantidade, 200

# OK
@insignias_bp.route("/insignias/criar", methods=["POST"])
def post_criar_insignia():
    if not request.is_json:
        return {"error": "Conteúdo deve ser do tipo 'application/json'"}, 415

    data = request.get_json()

    insignia = Insignia(
        id=None,
        nome=data.get("nome"),
        trilha=data.get("trilha"),
        niveis=data.get("niveis")
    )
    mensagem = insignia.gravar_insignia()
    return {
        "status": "success",
        "message": mensagem
    }, 201

# OK
@insignias_bp.route("/insignia/<id>/atualizar", methods=['PUT'])
def put_atualizar_insignia(id):
    data = request.get_json()
    insignia = Insignia.carregar_insignia(id)
    if not insignia:
        return {"error": "Insígnia não encontrada"}, 404

    if "nome" in data:
        insignia.nome = data["nome"]
    if "trilha" in data:
        insignia.trilha = data["trilha"]
    if "niveis" in data:
        insignia.niveis = data["niveis"]


    mensagem = insignia.gravar_insignia()
    return {
        "status": "success",
        "mensagem": mensagem
    }, 200

# OK
@insignias_bp.route("/insignia/<id>/deletar", methods=['DELETE'])
def delete_deletar_insignia(id):
    insignia = Insignia.carregar_insignia(id)
    if not insignia:
        return {"error": "Insígnia não encontrada"}, 404

    if Insignia.remover_insignia(id):
        return {"message": "Insígnia removida com sucesso"}, 200
