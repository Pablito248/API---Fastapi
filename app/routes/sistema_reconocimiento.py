from fastapi import APIRouter, HTTPException
from typing import List
from app.models.sistema_reconocimiento import SistemaReconocimiento


router = APIRouter(
    prefix="/sistema_reconocimiento",
    tags=["sistema_reconocimiento"]

)


sistema_reconocimiento_db = []



@router.post("/", response_model=SistemaReconocimiento)
def crear_registro(registro: SistemaReconocimiento):

    for r in sistema_reconocimiento_db:
        if r.idRegistro == registro.idRegistro:
            raise HTTPException(status_code=400, detail="Registro con este ID ya existe")
        
    sistema_reconocimiento_db.append(registro)
    return registro


@router.get("/", response_model=List[SistemaReconocimiento])
def obtener_registros():
    return sistema_reconocimiento_db



@router.get("/usuario/{idUsuario}", response_model=List[SistemaReconocimiento])
def obtener_registros_por_usuario(idUsuario: int):
    resultados = [r for r in sistema_reconocimiento_db if r.idUsuario == idUsuario]
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron registros para este usuario")
    return resultados


@router.get("/{idRegistro}", response_model=SistemaReconocimiento)
def obtener_registro_por_id(idRegistro: int):
    for r in sistema_reconocimiento_db:
        if r.idRegistro == idRegistro:
            return r    
    raise HTTPException(status_code=404, detail="Registro no encontrado")


@router.put("/{idRegistro}", response_model=SistemaReconocimiento)
def actualizar_registro(idRegistro: int, registro_actualizado: SistemaReconocimiento):
    for i, r in enumerate(sistema_reconocimiento_db):
        if r.idRegistro == idRegistro:
            sistema_reconocimiento_db[i] = registro_actualizado
            return registro_actualizado
    raise HTTPException(status_code=404, detail="Registro no encontrado")


@router.delete("/{idRegistro}")
def eliminar_registro(idRegistro: int):
    for i, r in enumerate(sistema_reconocimiento_db):
        if r.idRegistro == idRegistro:
            sistema_reconocimiento_db.pop(i)
            return {"detail": "Registro eliminado"}
    raise HTTPException(status_code=404, detail="Registro no encontrado")