from typing import Any
from fastapi import APIRouter, Depends
from app.services.manufatura_service import ManufaturaService
from bson import json_util
import json

manufatura_route = APIRouter()
def criar_instancia_de_servico():
    return ManufaturaService()

@manufatura_route.get("/manufatura")
def importar(service: ManufaturaService = Depends(criar_instancia_de_servico)):
    response = service.listar_manufaturas()
    
    return json.loads(json_util.dumps(response))