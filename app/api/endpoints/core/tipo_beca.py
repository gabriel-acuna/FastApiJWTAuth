from app.schemas.core.TipoBecaSchema import *
from app.services.core.ServicioTipoBeca import ServicioTipoBeca
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends, Body
from app.schemas.core.TipoFuncionarioSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *
from app.services.auth import ServicioToken

router = APIRouter(prefix="/tipo-becas")


@router.get("/", response_model=List[TipoBecaSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_tipos_becas():
    return await ServicioTipoBeca.listar()


@router.get("/${id}",  response_model=TipoBecaSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_tipo_beca(id:str):
    tipo_beca = await ServicioTipoBeca.buscar_por_id(id)
    if not tipo_beca:
        raise HTTPException(
            status_code=404, detail="Tipo de beca no encontrado"
        )
    return tipo_beca

@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_tipo_beca(response: Response, tipo_beca: TipoBecaPostSchema = Body(...)):
    existe = await ServicioTipoBeca.existe(tipo_beca)
    if not existe:
        registrado = await ServicioTipoBeca.agregar_registro(tipo_beca)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El tipo de beca {tipo_beca.tipo_beca} ya está resgistrado")


@router.put("/", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_tipo_beca(response: Response, tipo_beca: TipoBecaPutSchema = Body(...)):
    actualizado = await ServicioTipoBeca.actualizar_registro(tipo_beca)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_tipo_beca(id: str, response: Response):
    tipo_beca = await ServicioTipoBeca.buscar_por_id(id)
    if tipo_beca:
        eliminado = await ServicioTipoBeca.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
