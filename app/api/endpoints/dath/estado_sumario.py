from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioEstadoSumario import ServicioEstadoSumario, EstadoSumarioSchema, EstadoSumarioPutSchema, EstadoSumarioPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/estados-sumarios")


@router.get("/",
            response_model=List[EstadoSumarioSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_estados_sumarios():
    return await ServicioEstadoSumario.listar()


@router.get("/{id}",
            response_model=List[EstadoSumarioSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_estado_sumario(id: str):
    estado_sumario = await ServicioEstadoSumario.buscar_por_id(id)
    if not estado_sumario:
        raise HTTPException(
            status_code=404, detail="Estado sumario no encontrado")
    return estado_sumario


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_estado_sumario(estado_sumario: EstadoSumarioPostSchema, response: Response):
    existe = await ServicioEstadoSumario.existe(estado_sumario)
    if not existe:
        registrado = await ServicioEstadoSumario.agregar_registro(estado_sumario)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El estado sumario {estado_sumario.estado} ya está resgistrado")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_estado_sumario(estado_sumario:  EstadoSumarioPutSchema, response: Response):
    existe = await ServicioEstadoSumario.buscar_por_id(estado_sumario.id)
    if existe:
        actualizado = await ServicioEstadoSumario.actualizar_registro(estado_sumario)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_estado_sumario(id: str, response: Response):
    estado_sumario = await ServicioEstadoSumario.buscar_por_id(id)
    if estado_sumario:
        eliminado = await ServicioEstadoSumario.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
