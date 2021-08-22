from app.services.core.ServicioRelacionIES import ServicioRelacionIES
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends
from app.schemas.Message import MessageSchema
from app.schemas.core.RelacionIESSchema import *
from app.api.messages import *
from app.services.auth import ServicioToken


router = APIRouter(prefix="/relaciones-ies")

@router.get("/", response_model=List[RelacionIESSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_relaciones_ies():
    return await ServicioRelacionIES.listar()


@router.get("/{id}", response_model=RelacionIESSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obetner_relacion_ies(id: str):
    documento = await ServicioRelacionIES.buscar_por_id(id)
    if not documento:
        raise HTTPException(
            status_code=404, detail="Relación IES no encontrada"
        )
    return RelacionIESSchema(**documento[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_relacion_ies(response: Response, relacion_ies: RelacionIESPostSchema):
    existe = await ServicioRelacionIES.existe(relacion=relacion_ies)
    if not existe:
        registrado = await ServicioRelacionIES.agregar_registro(relacion=relacion_ies)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La relación IES {relacion_ies.relacion} ya está resgistrada")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_relacion_ies(response: Response, relacion_ies: RelacionIESPutSchema):
    existe = await ServicioRelacionIES.buscar_por_id(relacion_ies.id)
    if existe:
        actualizado = await ServicioRelacionIES.actualizar_registro(relacion_ies)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_relacion_ies(id: str, response: Response):
    documento = await ServicioRelacionIES.buscar_por_id(id)
    if documento:
        eliminado = await ServicioRelacionIES.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)