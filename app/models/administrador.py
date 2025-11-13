from pydantic import BaseModel, Field
from typing import  List, Dict

class Administrador(BaseModel):
    idAdministrador: int = Field(..., description="ID único del administrador")
    idUsuario: int
    numeroDocumento: str
    contrasena: str
    acciones: List[Dict[str]] = []
