from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioRegimenDisciplinario import ServicioRegimenDisciplinario, RegimenDisciplinarioSchema, RegimenDisciplinarioPutSchema, RegimenDisciplinarioPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/regimenes-disciplinarios")


@router.get("/{anio}",
            response_model=List[RegimenDisciplinarioSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_regimen_disciplinario_por_año(anio: int):
    return await ServicioRegimenDisciplinario.listar_por_anio(anio)


@router.get("/{id}/{mes}",
            response_model=List[RegimenDisciplinarioSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_regimen_disciplinario_por_año_mes(anio: int, mes: str):
    return await ServicioRegimenDisciplinario.listar_por_anio_mes(anio, mes)


@router.get("personal/{id}",
            response_model=List[RegimenDisciplinarioSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_regimen_disciplinario_por_persona(id: str):
    return await ServicioRegimenDisciplinario.listar_por_persona(id)


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_regimen_disciplinario(regimen_disciplinario: RegimenDisciplinarioPostSchema, response: Response):
    existe = await ServicioRegimenDisciplinario.existe(regimen_disciplinario)
    if not existe:
        registrado = await ServicioRegimenDisciplinario.agregar_registro(regimen_disciplinario)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El régimen disciplinario ya está resgistrado")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_regimen_disciplinario(regimen_disciplinario:  RegimenDisciplinarioPutSchema, response: Response):
    existe = await ServicioRegimenDisciplinario.buscar_por_id(regimen_disciplinario.id)
    if existe:
        actualizado = await ServicioRegimenDisciplinario.agregar_registro(regimen_disciplinario)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_regimen_disciplinario(id: str, response: Response):
    regimen_disciplinario = await ServicioRegimenDisciplinario.buscar_por_id(id)
    if regimen_disciplinario:
        eliminado = await ServicioRegimenDisciplinario.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
