from fastapi import FastAPI
from app.routes import usuario, vigilante

app = FastAPI(
    title="API de Gestión de Usuarios",
    description="API para gestionar usuarios con operaciones CRUD.",
    version="1.0.0"


)

app.include_router(usuario.router)

@app.get("/")
def inicio():
        return {"message": "Bienvenido a la API de Gestión de Usuarios"}


app.include_router(vigilante.router)