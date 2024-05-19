from fastapi import APIRouter, Depends
from typing import Annotated
from app.services.data_download_service import DataDownloadService

router = APIRouter()
def createServiceInstance():
    return DataDownloadService()


@router.get("/importar",response_model=None)
def importar(tipo_operacao, sub_categoria= None, atualizar_base= True, service: DataDownloadService = Depends(createServiceInstance)):
    return service.importar(tipo_operacao,sub_categoria,atualizar_base)
