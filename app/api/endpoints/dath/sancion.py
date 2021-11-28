from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioSancion import ServicioSancion, SancionSchema, SancionPutSchema, SancionPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/sanciones")


@router.get("/",
            response_model=List[SancionSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_sanciones():
    return await ServicioSancion.listar()


@router.get("/{id}",
            response_model=List[SancionSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_sancion(id: str):
    sancion = await ServicioSancion.buscar_por_id(id)
    if not sancion:
        raise HTTPException(
            status_code=404, detail="Sanción no encontrada")
    return sancion


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_sancion(sancion: SancionPostSchema, response: Response):
    existe = await ServicioSancion.existe(sancion)
    if not existe:
        registrado = await ServicioSancion.agregar_registro(sancion)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La sanción {sancion.sancion} ya está resgistrada")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_sancion(sancion:  SancionPutSchema, response: Response):
    existe = await ServicioSancion.buscar_por_id(sancion.id)
    if existe:
        actualizado = await ServicioSancion.agregar_registro(sancion)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_sancion(id: str, response: Response):
    sancion = await ServicioSancion.buscar_por_id(id)
    if sancion:
        eliminado = await ServicioSancion.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
