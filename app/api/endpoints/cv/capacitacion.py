from app.services.cv.ServicioCapacitaciones import *
from app.schemas.cv.CapacitacitaonSchema import *
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken
from app.schemas.Message import MessageSchema
from typing import List
from app.api.messages import *


router = APIRouter(
    prefix="/capacitaciones"
)


@router.get("/persona/{id_persona}",
            response_model=List[CapacitacionSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def listar_capacitaciones(id_persona: str):
    return await ServicioCapacitacion.listar(id_persona=id_persona)


@router.get("/{id}",
            response_model=CapacitacionSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def obtener_capacitacion(id: str):
    capacitacion = await ServicioCapacitacion.buscar_por_id(id=id)
    if not capacitacion:
        raise HTTPException(
            status_code=404, detail="Capacitación no encontrada"
        )
    return capacitacion


@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_capacitacion(response: Response, capacitacion: CapacitacionPostSchema = Body(...)):
    registrado = await ServicioCapacitacion.agregar_registro(capacitacion)
    if registrado:
        return MessageSchema(type="success", content=POST_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.put("/{id}", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_capacitacion(id: str, response: Response, capacitacion: CapacitacionPutSchema = Body(...)):
    actualizado = await ServicioCapacitacion.actualizar_registro(id, capacitacion)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_capacitacion(id: str, response: Response):
    capacitacion = await ServicioCapacitacion.buscar_por_id(id)
    if capacitacion:
        eliminado = await ServicioCapacitacion.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
