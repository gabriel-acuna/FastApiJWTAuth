from app.schemas.core.FinanciamientoBecaSchema import *
from app.services.core.ServicioFinanciamiento import ServicioFinanciamiento
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends, Body
from app.schemas.core.TipoFuncionarioSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *
from app.services.auth import ServicioToken

router = APIRouter(prefix="/financiamientos")


@router.get("/", response_model=List[FinanciamientoBecaSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_tipos_financiamientos():
    return await ServicioFinanciamiento.listar()


@router.get("/${id}",  response_model=FinanciamientoBecaSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_tipo_financiamiento(id:str):
    financiamiento = await ServicioFinanciamiento.buscar_por_id(id)
    if not financiamiento:
        raise HTTPException(
            status_code=404, detail="Tipo de beca no encontrado"
        )
    return financiamiento

@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_financiamiento(response: Response, financiamiento: FinanciamientoBecaPostSchema = Body(...)):
    existe = await ServicioFinanciamiento.existe(financiamiento)
    if not existe:
        registrado = await ServicioFinanciamiento.agregar_registro(financiamiento)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El tipo de financiamiento {financiamiento.financiamiento} ya está resgistrado")


@router.put("/", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_financiamiento(response: Response, financiamiento: FinanciamientoBecaPutSchema = Body(...)):
    actualizado = await ServicioFinanciamiento.actualizar_registro(financiamiento)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_financiamiento(id: str, response: Response):
    financiamiento = await ServicioFinanciamiento.buscar_por_id(id)
    if financiamiento:
        eliminado = await ServicioFinanciamiento.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
