from typing import List
from app.api.messages import *
from app.schemas.Message import MessageSchema
from app.schemas.core.CantonSchema import *
from app.services.core.ServicioCanton import ServicioCanton
from fastapi import APIRouter, HTTPException, Depends, Body, Response, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/cantones")


@router.get("/", response_model=List[CantonSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_cantones():
    return await ServicioCanton.listar()


@router.get("/{id}", response_model=CantonSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_canton(id: int):
    canton = await ServicioCanton.buscar_por_id(id)
    if not canton:
        raise HTTPException(status_code=404, detail="Cantón no encontrado")
    return CantonSchema(**canton[0].__dict__)

@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_canton(response: Response, canton: CantonPostSchema = Body(...)):
    existe = await ServicioCanton.existe(canton)
    if not existe:
        registrado = await ServicioCanton.agregar_registro(canton)
        if registrado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El cantón {canton.canton} ya está resgistrada")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_canton(response: Response, canton: CantonPutSchema):
    existe = await ServicioCanton.buscar_por_id(canton.id)
    if existe:
        actualizado = await ServicioCanton.actualizar_registro(canton)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_etnia(id: str, response: Response):
    etnia = await ServicioCanton.buscar_por_id(id)
    if etnia:
        eliminado = await ServicioCanton.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
