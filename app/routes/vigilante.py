from fastapi import APIRouter, HTTPException
from app.models.vigilante import VigilanteCreate, VigilanteUpdate, VigilanteBase
from app.core.database import db

router = APIRouter(prefix="/vigilantes", tags=["vigilantes"])
coleccion = db["vigilantes"]


@router.post("/")
async def crear_vigilante(vigilante: VigilanteCreate):
    result = coleccion.insert_one(vigilante.dict())
    return {"mensaje": "Vigilante creado con éxito", "id": str(result.inserted_id)}

@router.get("/")
async def listar_vigilantes():
    vigilantes = list(coleccion.find())
    for v in vigilantes:
        v["_id"] = str(v["_id"])
    return vigilantes

@router.get("/{idVigilante}")
async def obtener_vigilante(idVigilante: int):
    vigilante = coleccion.find_one({"_id": idVigilante})
    if not vigilante:
        raise HTTPException(status_code=404, detail="Vigilante no encontrado")
    vigilante["_id"] = str(vigilante["_id"])
    return vigilante

@router.put("/{idVigilante}")
async def actualizar_vigilante(idVigilante: int, vigilante: VigilanteUpdate):
    update_result = coleccion.update_one(
        {"_id": idVigilante},
        {"$set": vigilante.dict(exclude={"idVigilante"})}  
    )
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Vigilante no encontrado")
    return {"mensaje": "Vigilante actualizado con éxito"}

@router.delete("/{idVigilante}")
async def eliminar_vigilante(idVigilante: int):
    delete_result = coleccion.delete_one({"_id": idVigilante})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Vigilante no encontrado")
    return {"mensaje": "Vigilante eliminado con éxito"}



