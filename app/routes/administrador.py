from fastapi import APIRouter, HTTPException
from app.models.administrador import AdministradorCreate, AdministradorUpdate, AdministradorBase

router = APIRouter()

administradores_db = []
current_id = 1


            
