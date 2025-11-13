from pydantic import BaseModel, Field
from typing import List, Dict

class vigilante(BaseModel):
    idVigilante: int = Field(..., description="ID único del vigilante")
    idUsuario: int
    numeroDocumento: str
    contrasena: str
    acciones: List[Dict[str]] = []



