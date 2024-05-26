from fastapi import FastAPI, Depends
from app.routes.importar_route import importar_route
from app.routes.configuracao_route import configuracao_route
from app.routes.comercio_route import comercio_route
from app.routes.manufatura_route import manufatura_route
from app.routes.infra_route import infra_route
from app.routes.auth import router as auth_route, get_current_active_user 
from app.backend.mongodb_connector import MongoConnector

app = FastAPI(
    title="Embrapa Tech Challenge"
)

app.include_router(configuracao_route, dependencies=[Depends(get_current_active_user)])
app.include_router(importar_route, dependencies=[Depends(get_current_active_user)])
app.include_router(manufatura_route, dependencies=[Depends(get_current_active_user)])
app.include_router(comercio_route, dependencies=[Depends(get_current_active_user)])
app.include_router(infra_route)
app.include_router(auth_route, prefix="/auth") 
