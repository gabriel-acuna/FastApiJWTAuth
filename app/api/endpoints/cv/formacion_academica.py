from app.services.cv.ServicioFormacionAcademica import ServicioFormacionAcademica
from app.schemas.cv.FormacionAcademicaSchema import *
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken
from app.schemas.Message import MessageSchema
from typing import List
from app.api.messages import *


router = APIRouter(
    prefix="/formacion-academica"
)


@router.get("/persona/{id_persona}",
            response_model=List[FormacionAcademicaSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def listar_fromacion_academica(id_persona: str):
    return await ServicioFormacionAcademica.listar(id_persona=id_persona)


@router.get("/{id}",
            response_model=FormacionAcademicaSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def obtener_fromacion(id: str):
    capacitacion = await ServicioFormacionAcademica.buscar_por_id(id=id)
    if not capacitacion:
        raise HTTPException(
            status_code=404, detail="Formación académica no encontrada"
        )
    return capacitacion


@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_formacion(response: Response, estudio: FormacionAcademicaPostSchema = Body(...)):
    existe = await ServicioFormacionAcademica.existe(estudio)
    if not existe:
        registrado = await ServicioFormacionAcademica.agregar_registro(estudio)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La fromación academica como {estudio.nombre_titulo} ya está resgistrada")


@router.put("/{id}", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_formacion(id: str, response: Response, estudio: FormacionAcademicaPutSchema = Body(...)):
    actualizado = await ServicioFormacionAcademica.actualizar_registro(id, estudio)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_formacion(id: str, response: Response):
    estudio = await ServicioFormacionAcademica.buscar_por_id(id)
    if estudio:
        eliminado = await ServicioFormacionAcademica.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
