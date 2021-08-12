from app.services.core.ServicioTipoEscalafonNombramiento import ServicioTipoEscalafonNombramiento
from typing import List
from fastapi import APIRouter, HTTPException, Response, status
from app.schemas.core.TipoEscalafonNombramientoSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *


router = APIRouter(prefix="/tipos-escalafones-nombramientos")


@router.get("/", response_model=List[TipoEscalafonNombramientoSchema])
async def listar_tipos_escalafones_nombramientos():
    return await ServicioTipoEscalafonNombramiento.listar()


@router.get("/{id}", response_model=TipoEscalafonNombramientoSchema)
async def obetner_tipo_esclafon_nombramiento(id: str):
    documento = await ServicioTipoEscalafonNombramiento.buscar_por_id(id)
    if not documento:
        raise HTTPException(
            status_code=404, detail="Tipo de escalafón nombramiento no encontrado"
        )
    return TipoEscalafonNombramientoSchema(**documento[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201)
async def registrar_tipo_escalafon_nombramiento(response: Response, tipo_escalafon: TipoEscalafonNombramientoPostSchema):
    existe = await ServicioTipoEscalafonNombramiento.existe(tipo_escalafon=tipo_escalafon)
    if not existe:
        registrado = await ServicioTipoEscalafonNombramiento.agregar_registro(tipo_escalafon=tipo_escalafon)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El tipo de escalafón nombramiento {tipo_escalafon.escalafon_nombramiento} ya está resgistrado")


@router.put("/", response_model=MessageSchema)
async def actualizar_tipo_escalafon_nombramiento(response: Response, tipo_escalafon: TipoEscalafonNombramientoPutSchema):
    existe = await ServicioTipoEscalafonNombramiento.buscar_por_id(tipo_escalafon.id)
    if existe:
        actualizado = await ServicioTipoEscalafonNombramiento.actualizar_registro(tipo_escalafon)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema)
async def eliminar_tipo_escalafon_nombramiento(id: str, response: Response):
    documento = await ServicioTipoEscalafonNombramiento.buscar_por_id(id)
    if documento:
        eliminado = await ServicioTipoEscalafonNombramiento.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
