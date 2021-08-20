from app.api.messages import DELETE_SUCCESS_MSG, DELETE_WARNING_MSG, ERROR_MSG, POST_SUCCESS_MSG, PUT_SUCCESS_MSG, PUT_WARNING_MSG
from app.schemas.Message import MessageSchema
from typing import List
from app.schemas.core.EtniaSchema import EtniaSchema, EtniaPostSchema, EtniaPutSchema
from app.services.core.ServicioEtnia import ServicioEtnia
from fastapi import APIRouter, HTTPException, Body, Response, status


router = APIRouter(prefix="/etnias")


@router.get("/", response_model=List[EtniaPutSchema])
async def listar_etnias():
    return await ServicioEtnia.listar()


@router.get("/{id}", response_model=EtniaSchema)
async def obtener_etnia(id: str):
    etnia = await ServicioEtnia.buscar_por_id(id)
    if not etnia:
        raise HTTPException(status_code=404, detail="Etnia no encontrada")
    return EtniaSchema(**etnia[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201)
async def registrar_etnia(response: Response, etnia: EtniaPostSchema = Body(...)):
    existe = await ServicioEtnia.existe(etnia=etnia)
    if not existe:
        registrado = await ServicioEtnia.agregar_registro(etnia=etnia)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La etnia {etnia.etnia} ya está resgistrada")


@router.put("/", response_model=MessageSchema)
async def actualizar_etnia(response: Response, etnia: EtniaPutSchema):
    existe = await ServicioEtnia.buscar_por_id(etnia.id)
    if existe:
        actualizado = await ServicioEtnia.actualizar_registro(etnia)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema)
async def eliminar_etnia(id: str, response: Response):
    etnia = await ServicioEtnia.buscar_por_id(id)
    if etnia:
        eliminado = await ServicioEtnia.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
