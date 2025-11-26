from fastapi import APIRouter, HTTPException
from app.core.database import db
from app.models.visitante_temporal import visitanteTemporal
from bson import ObjectId

router = APIRouter(prefix="/visitantes-temporales", tags=["Visitantes Temporales"])
coleccion = db["visitantes_temporales"]


@router.post("/")
def crear_visitante(v: visitanteTemporal):
    nuevo_visitante = v.model_dump()
    resultado = coleccion.insert_one(nuevo_visitante)

    return {
        "mensaje": "Visitante temporal creado exitosamente",
        "id": str(resultado.inserted_id)
    }


@router.get("/")
def listar_visitantes():
    visitantes = list(coleccion.find({}))
    
    for v in visitantes:
        v["_id"] = str(v["_id"])
    
    return visitantes


@router.get("/{idVisitanteTemporal}")
def obtener_visitante(idVisitanteTemporal: int):
    visitante = coleccion.find_one({"idVisitanteTemporal": idVisitanteTemporal})

    if not visitante:
        raise HTTPException(status_code=404, detail="Visitante no encontrado")

    visitante["_id"] = str(visitante["_id"])
    return visitante


@router.put("/{idVisitanteTemporal}")
def actualizar_visitante(idVisitanteTemporal: int, v_update: visitanteTemporal):

    existente = coleccion.find_one({"idVisitanteTemporal": idVisitanteTemporal})
    if not existente:
        raise HTTPException(status_code=404, detail="Visitante no encontrado")

    datos_actualizados = v_update.model_dump()

    coleccion.update_one(
        {"idVisitanteTemporal": idVisitanteTemporal},
        {"$set": datos_actualizados}
    )

    return {"mensaje": "Visitante actualizado correctamente"}


@router.delete("/{idVisitanteTemporal}")
def eliminar_visitante(idVisitanteTemporal: int):
    resultado = coleccion.delete_one({"idVisitanteTemporal": idVisitanteTemporal})

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Visitante no encontrado")

    return {"mensaje": "Visitante eliminado exitosamente"}
