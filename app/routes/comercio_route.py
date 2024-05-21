from typing import Any
from fastapi import APIRouter, Depends
from app.services.comercio_service import ComercioService
from bson import json_util
import json

comercio_route = APIRouter()
def criar_instancia_de_servico():
    return ComercioService()

@comercio_route.get("/comercio")
def importar(service: ComercioService = Depends(criar_instancia_de_servico)):
    response = service.listar_comercios()
    
    return json.loads(json_util.dumps(response))