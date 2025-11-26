from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class VigilanteBase(BaseModel):
    idUsuario: int
    numeroDocumento : str
    contrasena : str
    acciones: List[Dict[str, str]] = []


class VigilanteCreate(VigilanteBase):
    pass


class VigilanteUpdate(VigilanteBase):
    pass



