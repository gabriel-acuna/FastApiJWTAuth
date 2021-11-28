from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioRegimenLaboral import ServicioRegimenLaboral, RegimenLaboralSchema, RegimenLaboralPutSchema, RegimenLaboralPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/regimenes-laborales")


@router.get("/",
            response_model=List[RegimenLaboralSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_regimenes_laborales():
    return await ServicioRegimenLaboral.listar()


@router.get("/{id}",
            response_model=List[RegimenLaboralSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_regimen_laboral(id: str):
    regimen_laboral = await ServicioRegimenLaboral.buscar_por_id(id)
    if not regimen_laboral:
        raise HTTPException(
            status_code=404, detail="Régimen laboral no encontrado")
    return regimen_laboral


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_regimen_laboral(regimen_laboral: RegimenLaboralPostSchema, response: Response):
    existe = await ServicioRegimenLaboral.existe(regimen_laboral)
    if not existe:
        registrado = await ServicioRegimenLaboral.agregar_registro(regimen_laboral)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El régimen laboral {regimen_laboral.regimen} ya está resgistrado")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_regimen_laboral(regimen_laboral:  RegimenLaboralPutSchema, response: Response):
    existe = await ServicioRegimenLaboral.buscar_por_id(regimen_laboral.id)
    if existe:
        actualizado = await ServicioRegimenLaboral.agregar_registro(regimen_laboral)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_regimen_laboral(id: str, response: Response):
    regimen_laboral = await ServicioRegimenLaboral.buscar_por_id(id)
    if regimen_laboral:
        eliminado = await ServicioRegimenLaboral.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
