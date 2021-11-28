from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioDeclaracionPatrimonial import ServicioDeclaracionPatrimonial, DeclaracionPatrimonialSchema, DeclaracionPatrimonialDetalladaSchema, DeclaracionPatrimonialPutSchema, DeclaracionPatrimonialPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/declaraciones-patrimoniales")


@router.get("/",
            response_model=List[DeclaracionPatrimonialDetalladaSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_declaraciones():
    return await ServicioDeclaracionPatrimonial.listar()


@router.get("/personal/{id}",
            response_model=List[DeclaracionPatrimonialSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_declaraciones_por_persona(id: str):
    return await ServicioDeclaracionPatrimonial.listar_por_id_persona(id)


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_declaracion(declaracion: DeclaracionPatrimonialPostSchema, response: Response):
    existe = await ServicioDeclaracionPatrimonial.existe(declaracion)
    if not existe:
        registrado = await ServicioDeclaracionPatrimonial.agregar_registro(declaracion)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El declaración de {declaracion.tipo_declaracion} ya está resgistrada")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_declaracion(declaracion:  DeclaracionPatrimonialPutSchema, response: Response):
    existe = await ServicioDeclaracionPatrimonial.buscar_por_id(declaracion.id)
    if existe:
        actualizado = await ServicioDeclaracionPatrimonial.agregar_registro(declaracion)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_declaracion(id: str, response: Response):
    declaracion = await ServicioDeclaracionPatrimonial.buscar_por_id(id)
    if declaracion:
        eliminado = await ServicioDeclaracionPatrimonial.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
