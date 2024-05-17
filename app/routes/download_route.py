from fastapi import APIRouter, Depends
from app.services.data_download_service import DataDownloadService

router = APIRouter()

@router.get("/atualizar")
def atualizar(service: DataDownloadService):
    return service.downloadData()
