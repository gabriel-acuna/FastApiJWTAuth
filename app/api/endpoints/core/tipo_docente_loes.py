from app.services.core.ServicioTipoDocenteLOES import ServicioTipoDocenteLOES
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends
from app.schemas.core.TipoDocenteLOESSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *
from app.services.auth import ServicioToken

router = APIRouter(prefix="/tipos-docentes-loes")


@router.get("/", response_model=List[TipoDocenteLOESSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_tipos_docentes():
    return await ServicioTipoDocenteLOES.listar()


@router.get("/{id}", response_model=TipoDocenteLOESSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obetner_tipo_docente(id: str):
    documento = await ServicioTipoDocenteLOES.buscar_por_id(id)
    if not documento:
        raise HTTPException(
            status_code=404, detail="Tipo docente LOES no encontrado"
        )
    return TipoDocenteLOESSchema(**documento[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_tipo_docente(response: Response, tipo_docente: TipoDocenteLOESPostSchema):
    existe = await ServicioTipoDocenteLOES.existe(tipo_docente)
    if not existe:
        registrado = await ServicioTipoDocenteLOES.agregar_registro(tipo_docente)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El tipo ddocente LOES {tipo_docente.tipo_docente} ya está resgistrado")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_tipo_docente(response: Response, tipo_docente: TipoDocenteLOESPutSchema):
    existe = await ServicioTipoDocenteLOES.buscar_por_id(tipo_docente.id)
    if existe:
        actualizado = await ServicioTipoDocenteLOES.actualizar_registro(tipo_docente)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_tipo_docente(id: str, response: Response):
    documento = await ServicioTipoDocenteLOES.buscar_por_id(id)
    if documento:
        eliminado = await ServicioTipoDocenteLOES.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
