from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.schemas.core.EstructuraInstitucionalSchema import *
from app.services.core.ServicioEstructuraInstitucional import ServicioEstructuraInstitucional, EstructuraInstitucional
from fastapi import APIRouter, HTTPException, Body, Response, status, Depends
from app.services.auth import ServicioToken


router = APIRouter(prefix="/estructura-institucional")


@router.get("/",
            response_model=EstructuraInstitucionalSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_estados_civiles():
    return await ServicioEstructuraInstitucional.listar()


@router.get("/{id}",
            response_model=EstructuraInstitucionalSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_estructura_institucional(id:int):
    estructura_institucional = await ServicioEstructuraInstitucional.buscar_por_id(id)
    if not estructura_institucional:
        raise HTTPException(
            status_code=404, detail="Estructura institucional no encontrado")
    return EstructuraInstitucionalSchema(**estructura_institucional[0].__dict__)



@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_estructura_institucional(response: Response, estructura_institucional: EstructuraInstitucionalPostSchema = Body(...)):
    existe = await ServicioEstructuraInstitucional.existe(estructura= estructura_institucional)
    if not existe:
        registrado = await ServicioEstructuraInstitucional.agregar_registro(estructura_institucional)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El estructura aprobada mediante {estructura_institucional.documento_aprobacion} ya está resgistrado")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_estructura_institucional(response: Response, estructura_institucional: EstructuraInstitucionalPutSchema):
    existe = await ServicioEstructuraInstitucional.buscar_por_id(estructura_institucional.id)
    if existe:
        actualizado = await ServicioEstructuraInstitucional.actualizar_registro(estructura_institucional)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_estructura_institucional(id: str, response: Response):
    etnia = await ServicioEstructuraInstitucional.buscar_por_id(id)
    if etnia:
        eliminado = await ServicioEstructuraInstitucional.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
