from pydantic import BaseModel, Field
from typing import  List, Dict


class AdministradorBase(BaseModel):
    idUsuario: int
    numeroDocumento : str
    contrasena : str
    acciones: List[Dict[str, str]] = []


class AdministradorCreate(AdministradorBase):
    pass


class AdministradorUpdate(AdministradorBase):
    idAdministrador: int