from app.services.cv.ServicioReferencia import *
from app.schemas.cv.ReferenciaSchema import *
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken
from app.schemas.Message import MessageSchema
from typing import List
from app.api.messages import *


router = APIRouter(
    prefix="/referencias"
)


@router.get("/",
            response_model=List[ReferenciaSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def listar_referncias(id_persona: str):
    return await ServicioReferencia.listar(id_persona=id_persona)


@router.get("/id",
            response_model=ReferenciaSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def obtener_referencia(id: str):
    capacitacion = await ServicioReferencia.buscar_por_id(id=id)
    if not capacitacion:
        raise HTTPException(
            status_code=404, detail="Referencia no encontrada"
        )
    return capacitacion


@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_referencia(response: Response, capacitacion: ReferenciaPostSchema = Body(...)):
    registrado = await ServicioReferencia.agregar_registro(capacitacion)
    if registrado:
        return MessageSchema(type="success", content=POST_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.put("/{id}", response_model=MessageSchema,
            status_code=201,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_referncia(id: str, response: Response, capacitacion: ReferenciaPutSchema = Body(...)):
    actualizado = await ServicioReferencia.actualizar_registro(capacitacion)
    if actualizado:
        return MessageSchema(type="success", content=POST_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_referencia(id: str, response: Response):
    capacitacion = await ServicioReferencia.buscar_por_id(id)
    if capacitacion:
        eliminado = await ServicioReferencia.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
