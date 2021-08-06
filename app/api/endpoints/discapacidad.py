from app.schemas.Message import MessageSchema
from typing import List
from app.schemas.core.DiscapacidadSchema import DiscapacidadPostSchema, DiscapacidadSchema
from app.services.core.ServicioDiscapacidad import ServicioDiscapacidad
from fastapi import APIRouter, HTTPException, responses

router = APIRouter(prefix="/discapacidades")

@router.get("/", response_model=List[DiscapacidadPostSchema])
async def listar_discapacidades():
    return await ServicioDiscapacidad.listar()

@router.get("/{id}", response_model=DiscapacidadSchema)
async def obtener_discapacidad(id:str):
    discapacidad = await ServicioDiscapacidad.buscar_por_id(id)
    if not discapacidad:
        raise HTTPException(status_code=404, detail="Discapacidad no encontrada")
    return DiscapacidadSchema(**discapacidad[0].__dict__)

@router.post("/", status_code=201, response_model=MessageSchema)
async def registar_discapacidad(discapacidad: DiscapacidadPostSchema):
    registrado = await ServicioDiscapacidad.agregar_registro(discapacidad)
    if registrado:
        return MessageSchema(type="success", content="Se registró correctamente")
    
    return MessageSchema(type="error", content="Algo salió mal intente otra vez")