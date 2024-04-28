from fastapi import APIRouter, Depends
from services.download_service import get_download_service, DownloadService

router = APIRouter()

@router.get("/atualizar")
def atualizar(service: DownloadService = Depends(get_download_service)):
    return service.download_and_save()
