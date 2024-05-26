from fastapi import APIRouter, Depends,Query
from app.services.manufatura_service import ManufaturaService
from bson import json_util
import json
from typing import List

manufatura_route = APIRouter(tags=["listagem"])

def criar_instancia_de_servico():
    return ManufaturaService()

@manufatura_route.get("/manufatura",summary="Lista e filtra os dados referentes ao Processamento, Comercialização e Produção")
def importar(service: ManufaturaService = Depends(criar_instancia_de_servico)
             , nome: List[str] = Query(None)
             , categoria: List[str] = Query(None)
             , operacao: List[str] = Query(None)
             , sub_operacao: List[str] = Query(None)
             , quantidade: List[str] = Query(None)
             , ano: List[str] = Query(None)
             ):
    """
        Utilize esse serviço para listar os dados importados em  <a href="/docs/#/importar/importar_importar_get" target="_self">importar</a>

        Os campos String (Nome, Categoria, Operacao e Sub_Operacao), aceitam uma lista inclusiva, que será tratado como um filtro IN.

        Para os campos Numéricos, será necessário utilizar ao menos um dos seguintes filtros:

          [gt] - <i>Maior que</i>

          [lt] - <i>Menor que</i>

          [eq] - <i>Igual a</i>

          [gte] - <i>Maior ou igual a </i>

          [lte] - <i>Menor ou igual a</i>

        Ex: Ano=[gt]1000&Ano=[lt]1500
    """
    filtro = {}
    if nome != None:
        filtro["nome"] = service.query_builder.escrever_filtro_string(nome)
    if categoria != None:
        filtro["categoria"] = service.query_builder.escrever_filtro_string(categoria)
    if operacao != None:
        filtro["operacao"] = service.query_builder.escrever_filtro_string(operacao)
    if sub_operacao != None:
        filtro["sub_categoria_operacao"] = service.query_builder.escrever_filtro_string(sub_operacao)
    if quantidade != None:
        filtro["quantidade"] = service.query_builder.escrever_filtro_numerico(quantidade)
    if ano != None:
        filtro["ano"] = service.query_builder.escrever_filtro_numerico(ano)

    response = service.listar_manufaturas(filtro)
    
    return json.loads(json_util.dumps(response))