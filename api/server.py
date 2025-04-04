from fastapi import FastAPI
from backend.routes import router

app = FastAPI(title="API de Operadoras ANS")

# Inclui as rotas definidas
app.include_router(router, prefix="/api")
