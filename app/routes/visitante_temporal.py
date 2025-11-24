from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from app.models.visitante_temporal import visitanteTemporal


router = APIRouter(
    prefix="/visitante_temporal",
    tags=["visitante_temporal"]

)

visitantes_temporales_db = []
