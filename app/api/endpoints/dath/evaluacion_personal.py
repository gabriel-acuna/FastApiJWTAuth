from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioEvaluacionPersonal import ServicioEvaluacionPersonal, EvaluacionPersonalSchema, EvaluacionPersonalPutSchema, EvaluacionPersonalPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/evaluaciones-personal")


@router.get("/personal/{id_persona}",
            response_model=List[EvaluacionPersonalSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_evaluaciones(id_persona: str):
    return await ServicioEvaluacionPersonal.listar_por_persona(id_persona)


@router.get("/{id}",
            response_model=List[EvaluacionPersonalSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_evaluacion(id: str):
    evaluacion = await ServicioEvaluacionPersonal.buscar_por_id(id)
    if not evaluacion:
        raise HTTPException(
            status_code=404, detail="Evaluación no encontrada")
    return evaluacion


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_evaluacion(evaluacion: EvaluacionPersonalPostSchema, response: Response):
    existe = await ServicioEvaluacionPersonal.existe(evaluacion)
    if not existe:
        registrado = await ServicioEvaluacionPersonal.agregar_registro(evaluacion)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La evaluación ya está resgistrada")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_evaluacion(evaluacion:  EvaluacionPersonalPutSchema, response: Response):
    existe = await ServicioEvaluacionPersonal.buscar_por_id(evaluacion.id)
    if existe:
        actualizado = await ServicioEvaluacionPersonal.actualizar_registro(evaluacion)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_evaluacion(id: str, response: Response):
    evaluacion = await ServicioEvaluacionPersonal.buscar_por_id(id)
    if evaluacion:
        eliminado = await ServicioEvaluacionPersonal.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
