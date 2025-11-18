from fastapi import APIRouter, HTTPException
from app.models.registro_entrada_salida import registro_entrada
from typing import List
from datetime import datetime

router = APIRouter(
    prefix="/registro_entrada_salida",
    tags=["registro_entrada_salida"]
)

registro_entradas_db: list [registro_entrada] = []

@router.post("/", response_model=registro_entrada)
def crear_registro(registro: registro_entrada):
    for r in registro_entradas_db:
        if r.idRegistroEntrada == registro.idRegistroEntrada:
            raise HTTPException(status_code=400, detail="El registro ya existe")
        
    registro_entradas_db.append(registro)
    return registro

@router.get("/", response_model=List[registro_entrada])
def listar_registros():
    return registro_entradas_db


@router.get("/{idRegistroEntrada}", response_model=registro_entrada)
def obtener_registro(idRegistro: int):
    for r in registro_entradas_db:
        if r.idRegistroEntrada == idRegistro:
            return r
    raise HTTPException(status_code=404, detail="Registro no encontrado")

@router.put("/{idRegistroEntrada}", response_model=registro_entrada)
def registrar_salida(idRegistro: int, horaSalida: datetime):
    for i, r in enumerate(registro_entradas_db):
        if r.idRegistroEntrada == idRegistro:
            registro_entradas_db[i].horaSalida = horaSalida
            return registro_entradas_db[i]
        
    raise HTTPException(status_code=404, detail="Registro no encontrado")


@router.delete("/{idRegistroEntrada}")
def eliminar_registro(idRegistro: int):
    for i, r in enumerate(registro_entradas_db):
        if r.idRegistroEntrada == idRegistro:
             registro_entradas_db.pop(i)
             return {"detail": "Registro eliminado"}
        
    raise HTTPException(status_code=404, detail="Registro no encontrado")

