from app.services.cv.ServicioTipoEvento import ServicioTipoEvento, TipoEventoSchema, TipoEventoPostSchema, TipoEventoPutSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken
from app.schemas.Message import MessageSchema
from typing import List
from app.api.messages import *


router = APIRouter(
    prefix="/eventos"
)


@router.get("/",
            response_model=List[TipoEventoSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def listar_eventos():
    return await ServicioTipoEvento.listar()


@router.get("/{id}",
            response_model=TipoEventoSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def obtener_evento(id: str):
    evento = await ServicioTipoEvento.buscar_por_id(id=id)
    if not evento:
        raise HTTPException(
            status_code=404, detail="Evento no encontrado"
        )
    return evento


@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_evento(response: Response, evento: TipoEventoPostSchema = Body(...)):
    existe = await ServicioTipoEvento.existe(evento)
    if not existe:
        registrado = await ServicioTipoEvento.agregar_registro(evento)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    else:
        response.status_code = status.HTTP_202_ACCEPTED
        return MessageSchema(type="warning",content =f"El evento {evento.evento} ya está registrado" )


@router.put("/", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_evento(id: str, response: Response, evento: TipoEventoPutSchema = Body(...)):
    actualizado = await ServicioTipoEvento.actualizar_registro(evento)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_evento(id: str, response: Response):
    evento = await ServicioTipoEvento.buscar_por_id(id)
    if evento:
        eliminado = await ServicioTipoEvento.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
