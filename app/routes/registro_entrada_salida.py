from fastapi import APIRouter, HTTPException
from app.models.registro_entrada_salida import registro_entrada
from typing import List
from datetime import datetime

router = APIRouter(
    prefix="/registro_entrada_salida",
    tags=["registro_entrada_salida"]
)

registro_entradas_db: list [registro_entrada] = []


