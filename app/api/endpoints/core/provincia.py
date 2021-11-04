from app.api.messages import *
from app.schemas.Message import MessageSchema
from app.schemas.core.CantonSchema import CantonSchema
from app.schemas.core.ProvinciaSchema import *
from typing import List
from fastapi import APIRouter, HTTPException, Depends, Body, status, Response
from app.services.core.ServicioProvincia import ServicioProvincia
from app.services.auth import ServicioToken


router = APIRouter(prefix="/provincias")


@router.get("/", response_model=List[ProvinciaSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_provincias():
    return await ServicioProvincia.listar()


@router.get("/{id}", response_model=ProvinciaSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_provincia(id: int):
    provincia = await ServicioProvincia.buscar_por_id(id)
    if not provincia:
        raise HTTPException(status_code=404, detail="Provincia no encontrada")
    return provincia

@router.post("/", response_model=MessageSchema, status_code=201,  dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_provincia(response: Response, provincia:ProvinciaPostSchema = Body(...)):
    existe = await ServicioProvincia.existe(provincia)
    if not existe:
        registrado = await ServicioProvincia.agregar_registro(provincia)
        if registrado:
            return MessageSchema(type="success", content= POST_SUCCESS_MSG)
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La provincia {provincia.provincia} ya está resgistrada")

@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_provincia(response: Response, provincia: ProvinciaPutSchema):
    existe = await ServicioProvincia.buscar_por_id(provincia.id)
    if existe:
        actualizado = await ServicioProvincia.actualizar_registro(provincia)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)

@router.get("/{id}/cantones", response_model=List[CantonSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_cantones_por_provincia(id: int):
    cantones = await ServicioProvincia.listar_cantones_por_provincia(id_provincia=id)
    if not cantones:
        raise HTTPException(
            status_code=404, detail="La provincia no se encontró o no tiene cantones registrados")
    return cantones
