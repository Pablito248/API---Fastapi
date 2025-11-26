from pydantic import BaseModel, Field
from datetime import datetime

class RegistroEntradaBase(BaseModel):
    idUsuario: int
    fechaHora: datetime
    tipoMovimiento: str
    numeroDocumento: str
    rol: str


class RegistroEntradaCreate(RegistroEntradaBase):
    pass


class RegistroEntradaUpdate(RegistroEntradaBase):
    pass
