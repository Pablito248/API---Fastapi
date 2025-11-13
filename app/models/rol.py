from pydantic import BaseModel, Field

class Rol(BaseModel):
    idRol: int = Field(..., description="ID único del rol")
    codigo: int