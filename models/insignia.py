from models.modelo_base import Modelo_base
from models.nivel_insignia import Nivel_insignia
from bson import ObjectId
from dotenv import load_dotenv
from config.database import crie_conexao_mongo

load_dotenv()

insignias_collection = crie_conexao_mongo("insigniasCollection")

class Insignia(Modelo_base):
    def __init__(self, id, nome, trilha, niveis):
        self.id = id
        self.nome = nome
        self.trilha = trilha
        self.niveis = [Nivel_insignia(**nivel) if isinstance(nivel, dict) else nivel for nivel in (niveis or [])]

    @staticmethod
    def carregar_insignia(insignia_id):
        if not ObjectId.is_valid(insignia_id):
            raise ValueError(f"ID inválido: {insignia_id}")

        document = insignias_collection.find_one(filter={"_id": ObjectId(insignia_id)})
        if not document:
            return None
        return Insignia.from_dict(document)

    @staticmethod
    def listar_insignias():
        documents = insignias_collection.find()
        return [Insignia.from_dict(doc) for doc in documents]

    def gravar_insignia(self):
      data = self.to_dict()
      if self.id:
          insignias_collection.update_one({"_id": ObjectId(self.id)}, {"$set": data})
          return f"Insígnia {self.nome} atualizada com sucesso!"
      else:
          result = insignias_collection.insert_one(data)
          self.id = str(result.inserted_id)
          return f"Insígnia {self.nome} salva com sucesso!"

    def insignia_atualizada(self):
          return (
              "A insígnia " + self.nome + " foi atualizada com sucesso."
          )

    def remover_insignia(id):
        res = insignias_collection.delete_one({"_id": ObjectId(id)})
        return res.deleted_count > 0

    def to_dict(self):
            data = {
                "id": self.id,
                "nome": self.nome,
                "trilha": self.trilha,
                "niveis": [
                   nivel.to_dict() if isinstance(nivel, Nivel_insignia) else nivel
                   for nivel in self.niveis
                ],
            }
            return data

    @staticmethod
    def from_dict(data):
        return Insignia(
            id=str(data["_id"]),
            nome=data["nome"],
            trilha=data["trilha"],
            niveis=[Nivel_insignia.from_dict(nivel) for nivel in data.get("niveis", [])]

        )

