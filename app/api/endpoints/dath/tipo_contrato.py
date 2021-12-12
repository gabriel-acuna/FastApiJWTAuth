from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioTipoContrato import ServicioTipoContrato, TipoContratoSchema, TipoContratoPutSchema, TipoContratoPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/tipos-contratos")


@router.get("/",
            response_model=List[TipoContratoSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_tipos_contratos():
    return await ServicioTipoContrato.listar()


@router.get("/{id}",
            response_model=List[TipoContratoSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_tipo_contrato(id: str):
    tipo_contrato = await ServicioTipoContrato.buscar_por_id(id)
    if not tipo_contrato:
        raise HTTPException(
            status_code=404, detail="Tipo de contrato no encontrado")
    return tipo_contrato


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_tipo_contrato(tipo_contrato: TipoContratoPostSchema, response: Response):
    existe = await ServicioTipoContrato.existe(tipo_contrato)
    if not existe:
        registrado = await ServicioTipoContrato.agregar_registro(tipo_contrato)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El tipo de contrato {tipo_contrato.contrato} ya está resgistrado")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_tipo_contrato(tipo_contrato: TipoContratoPutSchema, response: Response):
    existe = await ServicioTipoContrato.buscar_por_id(tipo_contrato.id)
    if existe:
        actualizado = await ServicioTipoContrato.actualizar_registro(tipo_contrato)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_tipo_contrato(id: str, response: Response):
    tipo_contrato = await ServicioTipoContrato.buscar_por_id(id)
    if tipo_contrato:
        eliminado = await ServicioTipoContrato.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
