from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioMotivoDesvinculacion import ServicioMotivoDesvinculacion, MotivoDesvinculacionSchema, MotivoDesvinculacionPutSchema, MotivoDesvinculacionPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/motivos-desvinculaciones")


@router.get("/",
            response_model=List[MotivoDesvinculacionSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_motivos_desvinculaciones():
    return await ServicioMotivoDesvinculacion.listar()


@router.get("/{id}",
            response_model=List[MotivoDesvinculacionSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_motivo_desvinculacion(id: str):
    motivo_desvinculacion = await ServicioMotivoDesvinculacion.buscar_por_id(id)
    if not motivo_desvinculacion:
        raise HTTPException(
            status_code=404, detail="Motivo de desvinculación no encontrado")
    return motivo_desvinculacion


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_motivo_desvinculacion(motivo_desvinculacion: MotivoDesvinculacionPostSchema, response: Response):
    existe = await ServicioMotivoDesvinculacion.existe(motivo_desvinculacion)
    if not existe:
        registrado = await ServicioMotivoDesvinculacion.agregar_registro(motivo_desvinculacion)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El motivo de desvinculación {motivo_desvinculacion.estado} ya está resgistrado")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_motivo_desvinculacion(motivo_desvinculacion:  MotivoDesvinculacionPutSchema, response: Response):
    existe = await ServicioMotivoDesvinculacion.buscar_por_id(motivo_desvinculacion.id)
    if existe:
        actualizado = await ServicioMotivoDesvinculacion.agregar_registro(motivo_desvinculacion)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_motivo_desvinculacion(id: str, response: Response):
    motivo_desvinculacion = await ServicioMotivoDesvinculacion.buscar_por_id(id)
    if motivo_desvinculacion:
        eliminado = await ServicioMotivoDesvinculacion.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
