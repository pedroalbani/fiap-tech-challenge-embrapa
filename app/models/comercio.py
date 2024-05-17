from pydantic import BaseModel
class Comercio(BaseModel):
    pais: str
    ano: int
    quantidade: int
    valor: float
    operacao: str

    def __init__(self,pais,ano,quantidade,valor,operacao):
        super().__init__(pais=pais,ano=ano,quantidade=quantidade,valor=valor,operacao=operacao)

