from app.services.core.ServicioNacionalidad import ServicioNacionalidad
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends
from app.schemas.core.NacionalidadSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *
from app.services.auth import ServicioToken


router = APIRouter(prefix="/nacionalidades")


@router.get("/", response_model=List[NacionalidadSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_nacionalidades():
    return await ServicioNacionalidad.listar()


@router.get("/{id}", response_model=NacionalidadSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_nacionalidad(id: str):
    nacionalidad = await ServicioNacionalidad.buscar_por_id(id)
    if not nacionalidad:
        raise HTTPException(
            status_code=404, detail="Nacionalidad no encontrada"
        )
    return NacionalidadSchema(**nacionalidad[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_nacionalidad(response: Response, nacionalidad: NacionalidadPostSchema):
    existe = await ServicioNacionalidad.existe(nacionalidad=nacionalidad)
    if not existe:
        registrado = await ServicioNacionalidad.agregar_registro(nacionalidad=nacionalidad)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La nacionalidad {nacionalidad.nacionalidad} ya está resgistrada")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_nacionalidad(response: Response, nacionalidad: NacionalidadPutSchema):
    existe = await ServicioNacionalidad.buscar_por_id(nacionalidad.id)
    if existe:
        actualizado = await ServicioNacionalidad.actualizar_registro(nacionalidad)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_nacionalidad(id: str, response: Response):
    nacionalidad = await ServicioNacionalidad.buscar_por_id(id)
    if nacionalidad:
        eliminado = await ServicioNacionalidad.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
