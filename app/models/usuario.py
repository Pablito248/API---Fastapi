from pydantic import BaseModel, Field
from bson import ObjectId
from .object_id import PyObjectId
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


    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str},

    }


