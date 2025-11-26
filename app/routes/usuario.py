from fastapi import APIRouter, HTTPException
from app.core.database import db
from app.models.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
coleccion = db["usuarios"]



@router.post("/")
async def crear_usuario(usuario: Usuario):
    result = coleccion.insert_one(usuario.dict())
    return {"mensaje": "Usuario creado con éxito", "idMongo": str(result.inserted_id)}



@router.get("/")
async def listar_usuarios():
    usuarios = list(coleccion.find())
    resultado = []

    for u in usuarios:
        u["_id"] = str(u["_id"])
        resultado.append(u)

    return resultado



@router.get("/{idUsuario}")
async def obtener_usuario(idUsuario: int):
    usuario = coleccion.find_one({"idUsuario": idUsuario})

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario["_id"] = str(usuario["_id"])
    return usuario




@router.put("/{idUsuario}")
async def actualizar_usuario(idUsuario: int, usuario: Usuario):
    update_result = coleccion.update_one(
        {"idUsuario": idUsuario},
        {"$set": usuario.dict()}
    )

    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return {"mensaje": "Usuario actualizado con éxito"}


@router.delete("/{idUsuario}")
async def eliminar_usuario(idUsuario: int):
    delete_result = coleccion.delete_one({"idUsuario": idUsuario})

    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return {"mensaje": "Usuario eliminado correctamente"}
