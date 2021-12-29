from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioSustituto import ServicioSustituto, SustitutoSchema, SustitutoPutSchema, SustitutoPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/sustitutos")


@router.get("/personal/{id_persona}",
            response_model=List[SustitutoSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_sustitutos_persona(id_persona:str):
    return await ServicioSustituto.listar_por_persona(id_persona)


@router.get("/{id}",
            response_model=List[SustitutoSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_sustituto_persona(id: str):
    sustituto = await ServicioSustituto.buscar_por_id(id)
    if not sustituto:
        raise HTTPException(
            status_code=404, detail="Estado sumario no encontrado")
    return sustituto


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_sustituto( response: Response, sustituto: SustitutoPostSchema = Body(...)):
    existe = await ServicioSustituto.existe(sustituto)
    if not existe:
        registrado = await ServicioSustituto.agregar_registro(sustituto)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El sustituto ya está resgistrado")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_sustituto(response: Response, sustituto:  SustitutoPutSchema = Body(...)):
    existe = await ServicioSustituto.buscar_por_id(sustituto.id)
    if existe:
        actualizado = await ServicioSustituto.actualizar_registro(sustituto)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_sustituto(id: str, response: Response):
    sustituto = await ServicioSustituto.buscar_por_id(id)
    if sustituto:
        eliminado = await ServicioSustituto.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
