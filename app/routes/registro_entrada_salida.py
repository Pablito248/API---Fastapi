from fastapi import APIRouter, HTTPException
from app.core.database import db
from app.models.registro_entrada_salida import (
    RegistroEntradaCreate,
    RegistroEntradaUpdate,
)
from bson import ObjectId

router = APIRouter(prefix="/registro_entrada", tags=["Registro Entrada/Salida"])
collection = db["registro_entrada_salida"]



@router.post("/")
async def create_registro(data: RegistroEntradaCreate):
    nuevo = data.model_dump()

    # Generar id incremental
    ultimo = collection.find_one(sort=[("idRegistro", -1)])
    nuevo_id = (ultimo["idRegistro"] + 1) if ultimo else 1
    nuevo["idRegistro"] = nuevo_id

    collection.insert_one(nuevo)

    return {"message": "Registro creado correctamente", "idRegistro": nuevo_id}



@router.get("/")
async def get_all_registros():
    registros = list(collection.find({}, {"_id": 0}))
    return registros



@router.get("/{idRegistro}")
async def get_registro(idRegistro: int):
    registro = collection.find_one({"idRegistro": idRegistro}, {"_id": 0})

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return registro


@router.put("/{idRegistro}")
async def update_registro(idRegistro: int, data: RegistroEntradaUpdate):
    info = data.model_dump()

   
    info.pop("idRegistro", None)

    result = collection.update_one(
        {"idRegistro": idRegistro},
        {"$set": info}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"message": "Registro actualizado correctamente"}



@router.delete("/{idRegistro}")
async def delete_registro(idRegistro: int):
    result = collection.delete_one({"idRegistro": idRegistro})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"message": "Registro eliminado correctamente"}
