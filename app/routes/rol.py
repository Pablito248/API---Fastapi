from fastapi import APIRouter
from app.models.rol import Rol

router = APIRouter()

roles_db = []


@router.post("/roles", )
def crear_rol(rol: Rol):    

    for r in roles_db:
        if r.idRol == rol.idRol:
            return {"error": "Rol con este ID ya existe"}
        
    roles_db.append(rol)
    return {"mensaje": "Rol creado exitosamente", "rol": rol}


@router.get("/roles/{idRol}")
def obtener_rol(idRol: str):
    for r in roles_db:
        if r.idRol == idRol:
            return r    
    return {"error": "Rol no encontrado"}


@router.put("/roles/{idRol}")
def actualizar_rol(idRol: str, rol_actualizado: Rol):
    for index, r in enumerate(roles_db):
        if r.idRol == idRol:
            roles_db[index] = rol_actualizado
            return {"mensaje": "Rol actualizado exitosamente", "rol": rol_actualizado}
    return {"error": "Rol no encontrado"}


@router.delete("/roles/{idRol}")
def eliminar_rol(idRol: str):
    for index, r in enumerate(roles_db):
        if r.idRol == idRol:
            roles_db.pop(index)
            return {"mensaje": "Rol eliminado exitosamente"}
    return {"error": "Rol no encontrado"}