from pydantic import BaseModel, Field
from datetime import datetime

class visitanteTemporal(BaseModel):
    idVisitanteTemporal: int
    nombre: str
    apellido: str
    numeroDocumento: str
    fechaHoraVisita: datetime
    ingreso: bool
    salida: bool