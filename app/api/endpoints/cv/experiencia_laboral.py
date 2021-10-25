from app.schemas.cv.ExperienciaLaboralSchema import *
from app.models.cv.modelos import ExperienciaLaboral
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken
from app.schemas.Message import MessageSchema
from typing import List
from app.api.messages import *
from app.services.cv.ServicioExperienciaLaboral import ServicioExperienciaLaboral


router = APIRouter(
    prefix="/experiencia-laboral"
)


@router.get("/persona/{id_persona}",
            response_model=List[ExperienciaLaboralSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def listar_experiencia_laboral(id_persona: str):
    return await ServicioExperienciaLaboral.listar(id_persona=id_persona)


@router.get("/{id}",
            response_model=ExperienciaLaboralSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def obtener_experiencia_laboral(id: str):
    experiencia = await ServicioExperienciaLaboral.buscar_por_id(id=id)
    if not experiencia:
        raise HTTPException(
            status_code=404, detail="Experiencia laboral no encontrada"
        )
    return experiencia


@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_experiencia(response: Response, experiencia: ExperienciaLaboralPostSchema = Body(...)):
    existe = ServicioExperienciaLaboral.existe(experiencia)
    if not existe:
        registrado = await ServicioExperienciaLaboral.agregar_registro(experiencia)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La experiencia laboral como {experiencia.cargo} en {experiencia.empresa} ya está resgistrada")


@router.put("/{id}", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_experiencia(id: str, response: Response, experiencia: ExperienciaLaboralPutSchema = Body(...)):
    actualizado = await ServicioExperienciaLaboral.actualizar_registro(id, experiencia)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_experiencia(id: str, response: Response):
    experiencia = await ServicioExperienciaLaboral.buscar_por_id(id)
    if experiencia:
        eliminado = await ServicioExperienciaLaboral.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
