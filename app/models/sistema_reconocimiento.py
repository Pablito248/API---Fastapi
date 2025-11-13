from pydantic import BaseModel, Field
from datetime import datetime

class SistemaReconocimiento(BaseModel):
    idusuario: int
    evento: str
    fecha: datetime
    resultado: bool