from fastapi import APIRouter, HTTPException
from app.models.usuario import Usuario

router = APIRouter(prefix= "/usuarios", tags=["Usuarios"])

Usuario_db = []

@router.post("/")
def crear_usuario(usuario: Usuario):
    for u in Usuario_db:
        if u.idUsuario == usuario.idUsuario:
            raise HTTPException(status_code=400, detail="Usuario ya existe")
    Usuario_db.append(usuario)
    return {"message": "Usuario creado exitosamente", "usuario": usuario}



@router.get("/")
def listar_usuarios():
    return Usuario_db


@router.get("/{id_usuario}")
def obtener_usuario(id_usuario: int):
    for u in Usuario_db:
        if u.idUsuario == id_usuario:
            return u
    raise HTTPException(status_code=404, detail="Usuario no encontrado")



@router.put("/{id_usuario}")
def actualizar_usuario(id_usuario: int, usuario_actualizado: Usuario):
    for i, u in enumerate(Usuario_db):
        if u.idUsuario == id_usuario:
            Usuario_db[i] = usuario_actualizado
            return {"message": "Usuario actualizado exitosamente", "usuario": usuario_actualizado}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@router.delete("/{id_usuario}")
def eliminar_usuario(id_usuario: int):
    for i, u in enumerate(Usuario_db):
        if u.idUsuario == id_usuario:
            del Usuario_db[i]
            return {"message": "Usuario eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


