from typing import Any
from fastapi import APIRouter, Depends
from app.services.configuracao_service import ConfiguracaoService
from bson import json_util
import json

configuracao_route = APIRouter()
def criar_instancia_de_servico():
    return ConfiguracaoService()

@configuracao_route.get("/configuracao/{tipo_operacao}")
def importar(tipo_operacao, service: ConfiguracaoService = Depends(criar_instancia_de_servico)):
    response = service.obter_configuracao(tipo_operacao)
    
    return json.loads(json_util.dumps(response))

@configuracao_route.get("/configuracao")
def importar(service: ConfiguracaoService = Depends(criar_instancia_de_servico)):
    response = service.listar_configuracoes()
    
    return json.loads(json_util.dumps(response))