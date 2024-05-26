from fastapi import FastAPI
from app.routes.importar_route import importar_route
from app.routes.configuracao_route import configuracao_route
from app.routes.comercio_route import comercio_route
from app.routes.manufatura_route import manufatura_route

app = FastAPI(
    title="Embrapa Tech Challenge"
)

app.include_router(configuracao_route)
app.include_router(importar_route)
app.include_router(manufatura_route)
app.include_router(comercio_route)
