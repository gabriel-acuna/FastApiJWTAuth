from app.schemas.cv.PonenciaSchema import *
from app.models.cv.modelos import Ponencia
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken
from app.schemas.Message import MessageSchema
from typing import List
from app.api.messages import *
from app.services.cv.ServicioPonencia import ServicioPonencia


router = APIRouter(
    prefix="/ponencias"
)


@router.get("/persona/{id_persona}",
            response_model=List[PonenciaSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def listar_ponencias(id_persona: str):
    return await ServicioPonencia.listar(id_persona=id_persona)


@router.get("/{id}",
            response_model=PonenciaSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def obtener_ponencia(id: str):
    capacitacion = await ServicioPonencia.buscar_por_id(id=id)
    if not capacitacion:
        raise HTTPException(
            status_code=404, detail="Capacitación no encontrada"
        )
    return capacitacion


@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_ponencia(response: Response, ponencia: PonenciaPostSchema = Body(...)):
    existe = await ServicioPonencia.existe(ponencia)
    if not existe:
        registrado = await ServicioPonencia.agregar_registro(ponencia)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La poencia {ponencia.tema} ya está resgistrada")


@router.put("/", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_ponencia(response: Response, ponencia: PonenciaPutSchema = Body(...)):
    actualizado = await ServicioPonencia.actualizar_registro(ponencia)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_ponencia(id: str, response: Response):
    ponencia = await ServicioPonencia.buscar_por_id(id)
    if ponencia:
        eliminado = await ServicioPonencia.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
