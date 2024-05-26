from typing import Any
from fastapi import APIRouter, Depends, Query
from app.services.comercio_service import ComercioService
from bson import json_util
import json
from typing import List

comercio_route = APIRouter(tags=["listagem"])

def criar_instancia_de_servico():
    return ComercioService()


@comercio_route.get("/comercio")
def listar_dados_comercio(service: ComercioService = Depends(criar_instancia_de_servico)
                          , operacao: List[str] = Query(None)
                          , sub_operacao: List[str] = Query(None)
                          , pais: List[str] = Query(None)
                          , valor: List[str] = Query(None)
                          , quantidade: List[str] = Query(None)
                          , ano: List[str] = Query(None)
                          ):
    filtro = {}
    if operacao != None:
        filtro["operacao"] = operacao
    if sub_operacao != None:
        filtro["sub_categoria_operacao"] = sub_operacao
    if pais != None:
        filtro["pais"] = pais
    if valor != None:
        filtro["valor"] = service.query_builder.escrever_query(valor)
    if quantidade != None:
        filtro["quantidade"] = service.query_builder.escrever_query(quantidade)
    if ano != None:
        filtro["ano"] = service.query_builder.escrever_query(ano)

    response = service.listar_comercios(filtro)

    return json.loads(json_util.dumps(response))