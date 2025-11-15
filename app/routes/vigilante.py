from fastapi import APIRouter, HTTPException
from app.models.vigilante import VigilanteCreate, VigilanteUpdate, VigilanteBase

router = APIRouter()

vigilantes_db = []
current_id = 1


@router.get("/vigilantes/", response_model=list[VigilanteBase])
def obtener_vigilantes():
    return vigilantes_db



@router.get("/vigilantes/{vigilante_id}", response_model=VigilanteBase)
def obtener_vigilante(vigilante_id: int):
    for v in vigilantes_db:
        if v['idVigilante'] == vigilante_id:
            return v
        
    raise HTTPException(status_code=404, detail="Vigilante no encontrado")


@router.post("/vigilantes/", response_model=VigilanteBase)
def crear_vigilante(vigilante: VigilanteCreate):
    global current_id

    nuevo_vigilante = vigilante(
        idVigilante=current_id,
        idUsuario=current_id, # Cambiar cuando se conecte a la BD
        numeroDocumento=vigilante.numeroDocumento,
        contrasena=vigilante.contrasena,
        acciones=vigilante.acciones

    )


    vigilantes_db.aappend(nuevo_vigilante)
    current_id += 1

    return nuevo_vigilante


@router.put("/vigilantes/{vigilante_id}", response_model=VigilanteBase)
def actualizar_vigilante(vigilante_id: int, vigilante: VigilanteUpdate):
    for i, v in enumerate(vigilantes_db):
        if v.idVigilante == vigilante_id:
            vigilantes_db[i] = vigilante(
                idVigilante=vigilante_id,
                idUsuario=vigilante.idUsuario,
                numeroDocumento=vigilante.numeroDocumento,
                contrasena=vigilante.contrasena,
                acciones=vigilante.acciones        
            )
            
            return vigilantes_db[i]
        
    raise HTTPException(status_code=404, detail="Vigilante no encontrado")


@router.delete("/vigilantes/{vigilante_id}")
def eliminar_vigilante(vigilante_id: int):
    for i, v in enumerate(vigilantes_db):
        if v.idVigilante == vigilante_id:
            del vigilantes_db.pop(i)
            return {"detail": "Vigilante eliminado"}
        
    raise HTTPException(status_code=404, detail="Vigilante no encontrado")