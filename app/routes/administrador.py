from fastapi import APIRouter, HTTPException
from app.core.database import db
from app.models.administrador import AdministradorCreate, AdministradorUpdate
from bson import ObjectId

router = APIRouter(prefix="/administradores", tags=["Administradores"])
coleccion = db["administradores"]


@router.post("/")
def crear_administrador(admin: AdministradorCreate):
    nuevo_admin = admin.model_dump()
    resultado = coleccion.insert_one(nuevo_admin)

    return {
        "mensaje": "Administrador creado exitosamente",
        "id": str(resultado.inserted_id)
    }


@router.get("/")
def listar_administradores():
    admins = list(coleccion.find({}))
    
    for a in admins:
        a["_id"] = str(a["_id"]) 
    
    return admins


@router.get("/{idUsuario}")
def obtener_administrador(idUsuario: int):
    admin = coleccion.find_one({"idUsuario": idUsuario})

    if not admin:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")

    admin["_id"] = str(admin["_id"])
    return admin


@router.put("/{idUsuario}")
def actualizar_administrador(idUsuario: int, admin_update: AdministradorUpdate):

    admin = coleccion.find_one({"idUsuario": idUsuario})
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")

    datos_actualizados = admin_update.model_dump(exclude={"idAdministrador"})

    coleccion.update_one(
        {"idUsuario": idUsuario},
        {"$set": datos_actualizados}
    )

    return {"mensaje": "Administrador actualizado correctamente"}



@router.delete("/{idUsuario}")
def eliminar_administrador(idUsuario: int):
    resultado = coleccion.delete_one({"idUsuario": idUsuario})

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")

    return {"mensaje": "Administrador eliminado exitosamente"}

            
