from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioFamiliarPersonal import ServicioFamiliarPersonal, FamiliarSchema, FamiliarPutSchema, FamiliarPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/familiares-personal")


@router.get("/personal/{id}",
            response_model=List[FamiliarSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_familiares():
    return await ServicioFamiliarPersonal.listar_por_id_persona()


@router.get("/{id}",
            response_model=List[FamiliarSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_familiar(id: str):
    familiar = await ServicioFamiliarPersonal.buscar_por_id(id)
    if not familiar:
        raise HTTPException(
            status_code=404, detail="Familiar no encontrado")
    return familiar


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_familiar(familiar: FamiliarPostSchema, response: Response):
    existe = await ServicioFamiliarPersonal.existe(familiar)
    if not existe:
        registrado = await ServicioFamiliarPersonal.agregar_registro(familiar)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El familiar ya está resgistrado")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_familiar(familiar:  FamiliarPutSchema, response: Response):
    existe = await ServicioFamiliarPersonal.buscar_por_id(familiar.id)
    if existe:
        actualizado = await ServicioFamiliarPersonal.agregar_registro(familiar)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_familiar(id: str, response: Response):
    familiar = await ServicioFamiliarPersonal.buscar_por_id(id)
    if familiar:
        eliminado = await ServicioFamiliarPersonal.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
