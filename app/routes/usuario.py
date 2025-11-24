from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from app.core.database import db
from app.models.usuario import Usuario
from bson import ObjectId
import cloudinary.uploader

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
coleccion = db["usuarios"]


@router.post("/")
async def crear_usuario(usuario: Usuario):
    result = coleccion.insert_one(usuario.dict())
    return {"mensaje": "Usuario creado con éxito", "id": str(result.inserted_id)}


@router.put("/{idUsuario}")
async def actualizar_usuario(idUsuario: int, usuario: Usuario):
    update_result = coleccion.update_one(
        {"idUsuario": idUsuario},
        {"$set": usuario.dict()}
    )
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario actualizado con éxito"}


@router.get("/{id}")
def obtener_usuario(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID de usuario inválido")
    
    usuario = coleccion.find_one({"_id": ObjectId(id)})
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    


@router.get("/")
def listar_usuarios():
        usuarios = list(coleccion.find())
        resultado = []
        for u in usuarios:
             u["_id"] = str(u["_id"])

        if "idUsuario" not in u:
            u["idUsuario"] = 0 
            resultado.append(Usuario(**u))
        
        return resultado

@router.delete("/{id}")
def eliminar_usuario(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID de usuario inválido")
    

    result = coleccion.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return {"mensaje": "Usuario eliminado correctamente"}


