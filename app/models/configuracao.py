from pydantic import BaseModel

class Configuracao(BaseModel):
    nome: str
    tipo_operacao: str

    def __init__(self,nome, tipo_operacao):
        super().__init__(nome=nome, tipo_operacao=tipo_operacao)