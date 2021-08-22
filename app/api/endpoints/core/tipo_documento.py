from app.services.core.ServicioTipoDocumento import ServicioTipoDocumento
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends
from app.schemas.core.TipoDocumentoSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *
from app.services.auth import ServicioToken


router = APIRouter(prefix="/tipos-documentos")


@router.get("/", response_model=List[TipoDocumentoSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_documentos():
    return await ServicioTipoDocumento.listar()


@router.get("/{id}", response_model=TipoDocumentoSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obetner_documento(id: str):
    documento = await ServicioTipoDocumento.buscar_por_id(id)
    if not documento:
        raise HTTPException(
            status_code=404, detail="Tipo de documento no encontrado"
        )
    return TipoDocumentoSchema(**documento[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_documento(response: Response, documento: TipoDocumentoPostSchema):
    existe = await ServicioTipoDocumento.existe(documento=documento)
    if not existe:
        registrado = await ServicioTipoDocumento.agregar_registro(documento=documento)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El tipo de documento {documento.tipo_documento} ya está resgistrado")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_documento(response: Response, documento: TipoDocumentoPutSchema):
    existe = await ServicioTipoDocumento.buscar_por_id(documento.id)
    if existe:
        actualizado = await ServicioTipoDocumento.actualizar_registro(documento)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_documento(id: str, response: Response):
    documento = await ServicioTipoDocumento.buscar_por_id(id)
    if documento:
        eliminado = await ServicioTipoDocumento.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
