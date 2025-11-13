from pydantic import BaseModel, Field
from typing import Optional

class Usuario(BaseModel):
    idUsuario: int = Field(..., description="ID único del usuario")
    nombre: str
    apellido: str
    tipoDocumento: str
    numeroDocumento: str
    foto: Optional[str] = None 
    entidad: Optional[str] = None 
    rol: Optional[str] = None 