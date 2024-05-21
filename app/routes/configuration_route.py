from typing import Any
from fastapi import APIRouter, Depends
from app.services.configuration_service import ConfigurationService
from bson import json_util
import json

router = APIRouter()
def createServiceInstance():
    return ConfigurationService()

@router.get("/configuracao/{tipo_operacao}")
def importar(tipo_operacao, service: ConfigurationService = Depends(createServiceInstance)):
    response = service.get_only_configuration(tipo_operacao)
    
    return json.loads(json_util.dumps(response))

@router.get("/configuracao")
def importar(service: ConfigurationService = Depends(createServiceInstance)):
    response = service.list_configuration()
    
    return json.loads(json_util.dumps(response))