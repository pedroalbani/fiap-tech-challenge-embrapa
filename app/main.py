from fastapi import FastAPI
from app.routes.download_route import router as download_router

app = FastAPI()

app.include_router(download_router)
