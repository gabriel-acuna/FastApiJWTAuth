from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioTipoNombramiento import ServicioTipoNombramiento, TipoNombramientoSchema, TipoNombramientoPutSchema, TipoNombramientoPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/tipos-nombramientos")


@router.get("/",
            response_model=List[TipoNombramientoSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_tipos_nombramientos():
    return await ServicioTipoNombramiento.listar()


@router.get("/{id}",
            response_model=List[TipoNombramientoSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_tipo_nombramiento(id: str):
    tipo_nombramiento = await ServicioTipoNombramiento.buscar_por_id(id)
    if not tipo_nombramiento:
        raise HTTPException(
            status_code=404, detail="Tipo de contrato no encontrado")
    return tipo_nombramiento


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_tipo_nombramiento(tipo_nombramiento: TipoNombramientoPostSchema, response: Response):
    existe = await ServicioTipoNombramiento.existe(tipo_nombramiento)
    if not existe:
        registrado = await ServicioTipoNombramiento.agregar_registro(tipo_nombramiento)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El tipo de nombramiento {tipo_nombramiento.nombramiento} ya está resgistrado")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_tipo_nombramiento(tipo_nombramiento: TipoNombramientoPutSchema, response: Response):
    existe = await ServicioTipoNombramiento.buscar_por_id(tipo_nombramiento.id)
    if existe:
        actualizado = await ServicioTipoNombramiento.actualizar_registro(tipo_nombramiento)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_tipo_nombramiento(id: str, response: Response):
    tipo_nombramiento = await ServicioTipoNombramiento.buscar_por_id(id)
    if tipo_nombramiento:
        eliminado = await ServicioTipoNombramiento.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
