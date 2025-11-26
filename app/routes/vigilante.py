from fastapi import APIRouter, HTTPException
from app.core.database import db
from app.models.vigilante import VigilanteCreate, VigilanteUpdate, VigilanteBase

router = APIRouter(prefix="/vigilantes", tags=["Vigilantes"])
coleccion = db["vigilantes"]


@router.post("/")
async def crear_vigilante(vigilante: VigilanteCreate):
    result = coleccion.insert_one(vigilante.dict())
    return {"mensaje": "Vigilante creado con éxito", "idMongo": str(result.inserted_id)}


@router.get("/")
async def listar_vigilantes():
    vigilantes = list(coleccion.find())
    resultado = []

    for v in vigilantes:
        v["_id"] = str(v["_id"])
        resultado.append(v)

    return resultado


@router.get("/{idUsuario}")
async def obtener_vigilante(idUsuario: int):
    vigilante = coleccion.find_one({"idUsuario": idUsuario})

    if not vigilante:
        raise HTTPException(status_code=404, detail="Vigilante no encontrado")

    vigilante["_id"] = str(vigilante["_id"])
    return vigilante


@router.put("/{idUsuario}")
async def actualizar_vigilante(idUsuario: int, vigilante: VigilanteUpdate):
    update_result = coleccion.update_one(
        {"idUsuario": idUsuario},
        {"$set": vigilante.dict(exclude={"idVigilante"})} 
    )

    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Vigilante no encontrado")

    return {"mensaje": "Vigilante actualizado con éxito"}


@router.delete("/{idUsuario}")
async def eliminar_vigilante(idUsuario: int):
    delete_result = coleccion.delete_one({"idUsuario": idUsuario})

    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Vigilante no encontrado")

    return {"mensaje": "Vigilante eliminado correctamente"}



