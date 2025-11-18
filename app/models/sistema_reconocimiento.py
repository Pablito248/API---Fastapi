from pydantic import BaseModel, Field
from datetime import datetime

class SistemaReconocimiento(BaseModel):
    idRegistro: int
    idusuario: int
    evento: str
    fecha: datetime
    resultado: bool