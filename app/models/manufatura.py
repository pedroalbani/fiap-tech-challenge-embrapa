from pydantic import BaseModel
class Manufatura(BaseModel):
    nome: str
    categoria: str
    ano: int
    quantidade: int
    operacao: str
    sub_categoria_operacao: str

    def __init__(self,nome,categoria,ano,quantidade,operacao,subcat_operacao):
        if type(categoria) != "string" or categoria == nome:
            categoria = ""
        super().__init__(nome = nome, 
                         categoria = categoria, 
                         ano = ano, 
                         quantidade = quantidade, 
                         operacao = operacao, 
                         sub_categoria_operacao = subcat_operacao)

