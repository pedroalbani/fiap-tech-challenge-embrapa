from fastapi import APIRouter, Depends
from app.services.data_download_service import DataDownloadService
from bson import json_util
import json

router = APIRouter()
def createServiceInstance():
    return DataDownloadService()

@router.get("/importar")
def importar(tipo_operacao, sub_categoria = None, atualizar_base = True, service: DataDownloadService = Depends(createServiceInstance)):
    response = service.importar(tipo_operacao, sub_categoria, atualizar_base)

    return json.loads(json_util.dumps(response))