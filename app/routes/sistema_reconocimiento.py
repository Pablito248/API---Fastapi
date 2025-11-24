from fastapi import APIRouter, HTTPException
from typing import List
from app.models.sistema_reconocimiento import SistemaReconocimiento


router = APIRouter(
    prefix="/sistema_reconocimiento",
    tags=["sistema_reconocimiento"]

)


sistema_reconocimiento_db = []


