from fastapi import APIRouter, HTTPException
from app.core.database import db
from app.models.rol import Rol

router = APIRouter(prefix="/roles", tags=["Roles"])
coleccion = db["roles"]


@router.post("/")
def crear_rol(rol: Rol):
    nuevo_rol = rol.model_dump()

    resultado = coleccion.insert_one(nuevo_rol)

    return {
        "mensaje": "Rol creado exitosamente",
        "id": str(resultado.inserted_id)
    }


@router.get("/")
def listar_roles():
    roles = list(coleccion.find({}))

    for r in roles:
        r["_id"] = str(r["_id"])

    return roles


@router.get("/{idRol}")
def obtener_rol(idRol: int):
    rol = coleccion.find_one({"idRol": idRol})

    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")

    rol["_id"] = str(rol["_id"])
    return rol



@router.put("/{idRol}")
def actualizar_rol(idRol: int, rol_update: Rol):

    existente = coleccion.find_one({"idRol": idRol})
    if not existente:
        raise HTTPException(status_code=404, detail="Rol no encontrado")

    datos_actualizados = rol_update.model_dump()

    coleccion.update_one(
        {"idRol": idRol},
        {"$set": datos_actualizados}
    )

    return {"mensaje": "Rol actualizado correctamente"}


@router.delete("/{idRol}")
def eliminar_rol(idRol: int):
    resultado = coleccion.delete_one({"idRol": idRol})

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Rol no encontrado")

    return {"mensaje": "Rol eliminado exitosamente"}

