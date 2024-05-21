from fastapi import FastAPI
from app.routes.download_route import router as download_router
from app.routes.configuration_route import router as configuration_router

app = FastAPI()

app.include_router(download_router)
app.include_router(configuration_router)
