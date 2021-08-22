from app.api.messages import DELETE_SUCCESS_MSG, DELETE_WARNING_MSG, ERROR_MSG, POST_SUCCESS_MSG, PUT_SUCCESS_MSG, PUT_WARNING_MSG
from app.schemas.Message import MessageSchema
from typing import List
from app.schemas.core.DiscapacidadSchema import DiscapacidadPostSchema, DiscapacidadPutSchema, DiscapacidadSchema
from app.services.core.ServicioDiscapacidad import ServicioDiscapacidad
from fastapi import APIRouter, HTTPException, Body, Response, status, Depends
from app.services.auth import ServicioToken

router = APIRouter(prefix="/discapacidades")


@router.get("/", response_model=List[DiscapacidadSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_discapacidades():
    return await ServicioDiscapacidad.listar()


@router.get("/{id}", response_model=DiscapacidadSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_discapacidad(id: str):
    discapacidad = await ServicioDiscapacidad.buscar_por_id(id)
    if not discapacidad:
        raise HTTPException(
            status_code=404, detail="Discapacidad no encontrada")
    return DiscapacidadSchema(**discapacidad[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_discapacidad(response: Response, discapacidad: DiscapacidadPostSchema = Body(...)):
    existe = await ServicioDiscapacidad.existe(discapacidad=discapacidad)
    if not existe:
        registrado = await ServicioDiscapacidad.agregar_registro(discapacidad=discapacidad)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La discapacidad {discapacidad.discapacidad} ya está resgistrada")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_discapacidad(response: Response, discapacidad: DiscapacidadPutSchema = Body(...)):
    existe = await ServicioDiscapacidad.buscar_por_id(str(discapacidad.id))
    if existe:
        actualizado = await ServicioDiscapacidad.actualizar_registro(discapacidad)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_discapacidad(id: str, response: Response):
    discapacidad = await ServicioDiscapacidad.buscar_por_id(id)
    if discapacidad:
        eliminado = await ServicioDiscapacidad.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
