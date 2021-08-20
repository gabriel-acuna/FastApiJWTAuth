from app.services.core.ServicioTiempoDedicacion import ServicioTiempoDedicacionProfesor
from typing import List
from fastapi import APIRouter, HTTPException, Response, status
from app.schemas.core.TiempoDedicacionProfesorSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *


router = APIRouter(prefix="/tiempos-dedicaciones-profesores")


@router.get("/", response_model=List[TiempoDedicacionProfesorSchema])
async def listar_tiempos_dedicaciones():
    return await ServicioTiempoDedicacionProfesor.listar()


@router.get("/{id}", response_model=TiempoDedicacionProfesorSchema)
async def obetner_tiempo_dedicacion(id: str):
    documento = await ServicioTiempoDedicacionProfesor.buscar_por_id(id)
    if not documento:
        raise HTTPException(
            status_code=404, detail="Tipo de documento no encontrado"
        )
    return TiempoDedicacionProfesorSchema(**documento[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201)
async def registrar_tiempo_dedicacion(response: Response, dedicacion: TiempoDedicacionProfesorPostSchema):
    existe = await ServicioTiempoDedicacionProfesor.existe(dedicacion=dedicacion)
    if not existe:
        registrado = await ServicioTiempoDedicacionProfesor.agregar_registro(dedicacion)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El tiempo de dedicación profesor {dedicacion.tiempo_dedicacion} ya está resgistrado")


@router.put("/", response_model=MessageSchema)
async def actualizar_tiempo_dedicacion(response: Response, dedicacion: TiempoDedicacionProfesorPutSchema):
    existe = await ServicioTiempoDedicacionProfesor.buscar_por_id(dedicacion.id)
    if existe:
        actualizado = await ServicioTiempoDedicacionProfesor.actualizar_registro(dedicacion)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema)
async def eliminar_tiempo_dedicacion(id: str, response: Response):
    documento = await ServicioTiempoDedicacionProfesor.buscar_por_id(id)
    if documento:
        eliminado = await ServicioTiempoDedicacionProfesor.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
