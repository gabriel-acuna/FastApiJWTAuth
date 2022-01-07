from app.schemas.Message import MessageSchema
from app.services.auth.ServicioRol import ServicioRol, RolPostSchema, RolSchema, RolPutSchema
from fastapi import APIRouter, Body, Response, status, HTTPException, Depends
from app.services.auth import ServicioToken
from typing import List
from app.api.messages import *


router = APIRouter(prefix="/roles")


@router.get("/", response_model=List[RolSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_roles():
    return await ServicioRol.listar()


@router.get("/{id}", response_model=RolSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_etnia(id: str):
    rol = await ServicioRol.buscar_por_id(id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return RolSchema(**rol[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_rol(response: Response, rol: RolPostSchema = Body(...)):
    existe = await ServicioRol.existe(rol=rol)
    if not existe:
        registrado = await ServicioRol.agregar_registro(rol=rol)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El rol {rol.rol} ya está resgistrado")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_rol(response: Response, rol: RolPutSchema):
    existe = await ServicioRol.buscar_por_id(rol.id)
    if existe:
        actualizado = await ServicioRol.actualizar_registro(rol)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_rol(id: str, response: Response):
    rol = await ServicioRol.buscar_por_id(id)
    if rol:
        eliminado = await ServicioRol.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
