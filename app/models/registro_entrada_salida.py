from pydantic import BaseModel, Field
from datetime import datetime

class registro_entrada(BaseModel):
    idRegistro: int = Field(..., description="ID del registro")
    idUsuario: int
    fehcaHora: datetime
    tipoMovimiento: str
    numeroDocumento: str
    rol: str 