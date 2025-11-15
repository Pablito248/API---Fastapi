from pydantic import BaseModel, Field
from typing import List, Dict, optional

class VigilanteBase(BaseModel):
    numeroDocumento : str
    contrasena : str
    acciones: List[Dict[str, str]] = []


class VigilanteCreate(VigilanteBase):
    pass


class VigilanteUpdate(VigilanteBase):
    idVigilante: int
    idUsuario: int



