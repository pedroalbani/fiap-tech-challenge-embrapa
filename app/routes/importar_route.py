from fastapi import APIRouter, Depends
from app.services.baixar_dados_service import BaixarDadosService
from bson import json_util
import json

importar_route = APIRouter()
def criar_instancia_de_servico():
    return BaixarDadosService()

@importar_route.get("/importar")
def importar(tipo_operacao, sub_categoria = None, atualizar_base = True, service: BaixarDadosService = Depends(criar_instancia_de_servico)):
    response = service.importar(tipo_operacao, sub_categoria, atualizar_base)

    return json.loads(json_util.dumps(response))