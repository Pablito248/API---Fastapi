from fastapi import APIRouter, HTTPException
from app.models.administrador import AdministradorCreate, AdministradorUpdate, AdministradorBase

router = APIRouter()

administradores_db = []
current_id = 1


@router.get("/administradores/", response_model=list[AdministradorBase])
def get_administradores():
    return administradores_db


@router.get("/administradores/{idAdministrador}", response_model=AdministradorBase)
def get_administrador(idAdministrador: int):
    for admin in administradores_db:
        if admin['idAdministrador'] == idAdministrador:
            return admin
    raise HTTPException(status_code=404, detail="Administrador not found")



@router.post("/administradores/", response_model=AdministradorBase)
def create_administrador(administrador: AdministradorCreate):
    global current_id

    nuevo_admin = administrador(
        idAdministrador=current_id,
        idUsuario=administrador.idUsuario,
        numeroDocumento=administrador.numeroDocumento,
        contrasena=administrador.contrasena,
        acciones=administrador.acciones

    )

    administradores_db.append(nuevo_admin)
    current_id += 1
    return nuevo_admin


@router.put("/administradores/{idAdministrador}", response_model=AdministradorBase)
def actualizar_administrador(idAdministrador: int, administrador: AdministradorUpdate):
    for i, admin in enumerate(administradores_db):
        if admin.administrador == idAdministrador:
            administradores_db[i] = administrador(
                idAdministrador=idAdministrador,
                idUsuario=administrador.idUsuario,
                numeroDocumento=administrador.numeroDocumento,
                contrasena=administrador.contrasena,
                acciones=administrador.acciones
            )

            return administradores_db[i]
    raise HTTPException(status_code=404, detail="Administrador not found")


@router.delete("/administradores/{idAdministrador}")
def eliminar_administrador(idAdministrador: int):
    for i, admin in enumerate(administradores_db):
        if admin['idAdministrador'] == idAdministrador:
            administradores_db.pop(i)
            return {"detail": "Administrador deleted"}
        
    raise HTTPException(status_code=404, detail="Administrador not found")


            
