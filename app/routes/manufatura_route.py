from fastapi import APIRouter, Depends,Query
from app.services.manufatura_service import ManufaturaService
from bson import json_util
import json
from typing import List

manufatura_route = APIRouter(tags=["listagem"])

def criar_instancia_de_servico():
    return ManufaturaService()

@manufatura_route.get("/manufatura")
def importar(service: ManufaturaService = Depends(criar_instancia_de_servico)
             , nome: List[str] = Query(None)
             , categoria: List[str] = Query(None)
             , operacao: List[str] = Query(None)
             , sub_operacao: List[str] = Query(None)
             , quantidade: List[str] = Query(None)
             , ano: List[str] = Query(None)
             ):
    filtro = {}
    if nome != None:
        filtro["nome"] = nome
    if categoria != None:
        filtro["categoria"] = categoria
    if operacao != None:
        filtro["operacao"] = operacao
    if sub_operacao != None:
        filtro["sub_categoria_operacao"] = sub_operacao
    if quantidade != None:
        filtro["quantidade"] = service.query_builder.escrever_query(quantidade)
    if ano != None:
        filtro["ano"] = service.query_builder.escrever_query(ano)

    response = service.listar_manufaturas()
    
    return json.loads(json_util.dumps(response))