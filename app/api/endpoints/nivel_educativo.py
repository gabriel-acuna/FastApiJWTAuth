from app.schemas.core.NivelEducativoSchema import NivelEducativoSchema
from app.services.core.ServicioNivelEducativo import ServicioNivelEducativo
from typing import List
from fastapi import APIRouter, HTTPException, Response, status
from app.schemas.core.NivelEducativoSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *


router = APIRouter(prefix="/niveles-educativos")


@router.get("/", response_model=List[NivelEducativoSchema])
async def listar_niveles_educativos():
    return await ServicioNivelEducativo.listar()


@router.get("/{id}", response_model=NivelEducativoSchema)
async def obtener_nivel_educativo(id: str):
    nacionalidad = await ServicioNivelEducativo.buscar_por_id(id)
    if not nacionalidad:
        raise HTTPException(
            status_code=404, detail="Nivel educativo no encontrado"
        )
    return NivelEducativoSchema(**nacionalidad[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201)
async def registrar_nivel_educativo(response: Response, nivel: NivelEducativoPostSchema):
    existe = await ServicioNivelEducativo.existe(nivel=nivel)
    if not existe:
        registrado = await ServicioNivelEducativo.agregar_registro(nivel)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"EL nivel educativo {nivel.nivel} ya está registrado")


@router.put("/", response_model=MessageSchema)
async def actualizar_nivel_educativo(response: Response, nivel: NivelEducativoPutSchema):
    existe = await ServicioNivelEducativo.buscar_por_id(nivel.id)
    if existe:
        actualizado = await ServicioNivelEducativo.actualizar_registro(nivel)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema)
async def eliminar_nivel_educativo(id: str, response: Response):
    nacionalidad = await ServicioNivelEducativo.buscar_por_id(id)
    if nacionalidad:
        eliminado = await ServicioNivelEducativo.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
