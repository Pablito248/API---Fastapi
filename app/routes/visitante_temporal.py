from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from app.models.visitante_temporal import visitanteTemporal


router = APIRouter(
    prefix="/visitante_temporal",
    tags=["visitante_temporal"]

)

visitantes_temporales_db = []

@router.post("/", response_model=visitanteTemporal)
def crear_visitante_temporal(visitante: visitanteTemporal):
    for v in visitantes_temporales_db:
        if v.idVisitanteTemporal == visitante.idVisitanteTemporal:
            raise HTTPException(status_code=400, detail="Visitante temporal ya existe") 
    visitantes_temporales_db.append(visitante)
    return visitante


@router.get("/", response_model=List[visitanteTemporal])
def listar_visitantes_temporales():
    return visitantes_temporales_db



@router.get("/{idVisitanteTemporal}", response_model=visitanteTemporal)
def obtener_visitante_temporal(idVisitanteTemporal: int):
    for v in visitantes_temporales_db:
        if v.idVisitanteTemporal == idVisitanteTemporal:
            return v
    raise HTTPException(status_code=404, detail="Visitante temporal no encontrado")



@router.put("/{idVisitanteTemporal}/ingreso", response_model=visitanteTemporal)
def registrar_ingreso(idVisitanteTemporal: int):
    for i, v in enumerate(visitantes_temporales_db):
        if v.idVisitanteTemporal == idVisitanteTemporal:
            visitantes_temporales_db[i].ingreaso = True

            if not visitantes_temporales_db[i].fechaHoraVisita:
                visitantes_temporales_db[i].fechaHoraVisita = datetime.now()
            return visitantes_temporales_db[i]
    raise HTTPException(status_code=404, detail="Visitante temporal no encontrado")


@router.put("/{idVisitanteTemporal}/salida", response_model=visitanteTemporal)
def registrar_salida(idVisitanteTemporal: int):
    for i, v in enumerate(visitantes_temporales_db):
        if v.idVisitanteTemporal == idVisitanteTemporal:
            visitantes_temporales_db[i].salida = True
            return visitantes_temporales_db[i]
    raise HTTPException(status_code=404, detail="Visitante temporal no encontrado")


@router.delete("/{idVisitanteTemporal}")
def eliminar_visitante_temporal(idVisitanteTemporal: int):
    for i, v in enumerate(visitantes_temporales_db):
        if v.idVisitanteTemporal == idVisitanteTemporal:
            visitantes_temporales_db.pop(i)
            return {"detail": "Visitante temporal eliminado"}
    raise HTTPException(status_code=404, detail="Visitante temporal no encontrado")