from fastapi import APIRouter, HTTPException
from app.core.database import db
from app.models.sistema_reconocimiento import SistemaReconocimiento

router = APIRouter(prefix="/reconocimiento", tags=["Sistema de Reconocimiento"])
coleccion = db["sistema_reconocimiento"]



@router.post("/")
def crear_registro(registro: SistemaReconocimiento):
    nuevo_registro = registro.model_dump()

    resultado = coleccion.insert_one(nuevo_registro)

    return {
        "mensaje": "Registro creado exitosamente",
        "id": str(resultado.inserted_id)
    }


@router.get("/")
def listar_registros():
    registros = list(coleccion.find({}))

    for r in registros:
        r["_id"] = str(r["_id"])

    return registros



@router.get("/{idRegistro}")
def obtener_registro(idRegistro: int):
    registro = coleccion.find_one({"idRegistro": idRegistro})

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    registro["_id"] = str(registro["_id"])
    return registro


@router.put("/{idRegistro}")
def actualizar_registro(idRegistro: int, registro_update: SistemaReconocimiento):

    existente = coleccion.find_one({"idRegistro": idRegistro})
    if not existente:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    datos_actualizados = registro_update.model_dump()

    coleccion.update_one(
        {"idRegistro": idRegistro},
        {"$set": datos_actualizados}
    )

    return {"mensaje": "Registro actualizado correctamente"}


@router.delete("/{idRegistro}")
def eliminar_registro(idRegistro: int):
    resultado = coleccion.delete_one({"idRegistro": idRegistro})

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro eliminado exitosamente"}



