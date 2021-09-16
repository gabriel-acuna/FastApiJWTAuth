from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.schemas.core.EstadoCivilSchema import *
from app.services.core.ServicioEstadoCivil import ServicioEstadoCivil
from fastapi import APIRouter, HTTPException, Body, Response, status, Depends
from app.services.auth import ServicioToken


router = APIRouter(prefix="/estados-civiles")


@router.get("/",
            response_model=EstadoCivilSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_estados_civiles():
    return await ServicioEstadoCivil.listar()


@router.get("/{id}",
            response_model=EstadoCivilSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_estado_civil(id:int):
    estado_civil = await ServicioEstadoCivil.buscar_por_id(id)
    if not estado_civil:
        raise HTTPException(
            status_code=404, detail="Estado civil no encontrado")
    return EstadoCivilSchema(**estado_civil[0].__dict__)



@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_estado_civil(response: Response, estado_civil: EstadoCivilPostSchema = Body(...)):
    existe = await ServicioEstadoCivil.existe(estado_civil= estado_civil)
    if not existe:
        registrado = await ServicioEstadoCivil.agregar_registro(estado_civil)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El estado civil {estado_civil.estado_civil} ya está resgistrado")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_estado_civil(response: Response, estado_civil: EstadoCivilPutSchema):
    existe = await ServicioEstadoCivil.buscar_por_id(estado_civil.id)
    if existe:
        actualizado = await ServicioEstadoCivil.actualizar_registro(estado_civil)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_estado_civil(id: str, response: Response):
    etnia = await ServicioEstadoCivil.buscar_por_id(id)
    if etnia:
        eliminado = await ServicioEstadoCivil.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
