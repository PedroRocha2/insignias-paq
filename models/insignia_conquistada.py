class Insignia_conquistada:
    def __init__(self, id, nome, nivel, data):
        self.id = id
        self.nome = nome
        self.nivel = nivel
        self.data = data

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nivel": self.nivel,
            "data": self.data,
        }

    @staticmethod
    def from_dict(data):
        return Insignia_conquistada(
            id=data.get("id"),
            nome=data.get("nome"),
            nivel=data.get("nivel"),
            data=data.get("data"),
        )
