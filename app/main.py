from fastapi import FastAPI
from app.routes import usuario, vigilante, administrador, registro_entrada_salida, visitante_temporal, sistema_reconocimiento, rol

app = FastAPI(
    title="API de Gestión de Usuarios",
    description="API para gestionar usuarios con operaciones CRUD.",
    version="1.0.0"


)



@app.get("/")
def inicio():
        return {"message": "Bienvenido a la API de Gestión de Usuarios"}



app.include_router(usuario.router)

app.include_router(vigilante.router)

app.include_router(administrador.router)

app.include_router(registro_entrada_salida.router)

app.include_router(visitante_temporal.router)

app.include_router(sistema_reconocimiento.router)

app.include_router(rol.router)