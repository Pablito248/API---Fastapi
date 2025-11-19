from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from typing import Optional
import cloudinary.uploader
from app.models.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

Usuario_db = []


@router.post("/")
def crear_usuario(
    idUsuario: int = Form(...),
    nombre: str = Form(...),
    apellido: str = Form(...),
    tipoDocumento: str = Form(...),
    numeroDocumento: str = Form(...),
    entidad: Optional[str] = Form(None),
    rol: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
):
    # verificar duplicado antes de subir
    for u in Usuario_db:
        if u.idUsuario == idUsuario:
            raise HTTPException(status_code=400, detail="Usuario ya existe")

    usuario = Usuario(
        idUsuario=idUsuario,
        nombre=nombre,
        apellido=apellido,
        tipoDocumento=tipoDocumento,
        numeroDocumento=numeroDocumento,
        entidad=entidad,
        rol=rol,
        foto=None,
    )

    if file:
        try:
            result = cloudinary.uploader.upload(
                file.file,
                folder="usuarios",
                public_id=f"user_{idUsuario}",
                overwrite=True,
                resource_type="image",
            )
            usuario.foto = result.get("secure_url")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al subir la imagen: {e}")

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
def actualizar_usuario(
    id_usuario: int,
    nombre: Optional[str] = Form(None),
    apellido: Optional[str] = Form(None),
    tipoDocumento: Optional[str] = Form(None),
    numeroDocumento: Optional[str] = Form(None),
    entidad: Optional[str] = Form(None),
    rol: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
):
    for i, u in enumerate(Usuario_db):
        if u.idUsuario == id_usuario:
            # actualizar campos si se enviaron
            if nombre is not None:
                Usuario_db[i].nombre = nombre
            if apellido is not None:
                Usuario_db[i].apellido = apellido
            if tipoDocumento is not None:
                Usuario_db[i].tipoDocumento = tipoDocumento
            if numeroDocumento is not None:
                Usuario_db[i].numeroDocumento = numeroDocumento
            if entidad is not None:
                Usuario_db[i].entidad = entidad
            if rol is not None:
                Usuario_db[i].rol = rol

            if file:
                try:
                    result = cloudinary.uploader.upload(
                        file.file,
                        folder="usuarios",
                        public_id=f"user_{id_usuario}",
                        overwrite=True,
                        resource_type="image",
                    )
                    Usuario_db[i].foto = result.get("secure_url")
                except Exception as e:
                    raise HTTPException(status_code=500, detail=f"Error al subir la imagen: {e}")

            return {"message": "Usuario actualizado exitosamente", "usuario": Usuario_db[i]}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@router.delete("/{id_usuario}")
def eliminar_usuario(id_usuario: int):
    for i, u in enumerate(Usuario_db):
        if u.idUsuario == id_usuario:
            del Usuario_db[i]
            return {"message": "Usuario eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


