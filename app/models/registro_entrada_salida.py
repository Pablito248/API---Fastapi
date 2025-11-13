from pydantic import BaseModel, Field
from datetime import datetime

class SistemaReconocimiento(BaseModel):
    idRegistro: int = Field(..., description="ID del registro")
    idUsuario: int
    fehcaHora: datetime
    tipoMovimiento: str
    numeroDocumento: str
    rol: str  