from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioModalidadContractual import ServicioModalidadContractual, ModalidadContractualSchema, ModalidadContractualPutSchema, ModalidadContractualPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/modalidades-contractuales")


@router.get("/",
            response_model=List[ModalidadContractualSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_modalidades_contractuales():
    return await ServicioModalidadContractual.listar()


@router.get("/{id}",
            response_model=List[ModalidadContractualSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_modalidad_contractual(id: str):
    modalidad_contractual = await ServicioModalidadContractual.buscar_por_id(id)
    if not modalidad_contractual:
        raise HTTPException(
            status_code=404, detail="Modalidad ontractual no encontrado")
    return modalidad_contractual


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_modalidad_contractual(modalidad_contractual: ModalidadContractualPostSchema, response: Response):
    existe = await ServicioModalidadContractual.existe(modalidad_contractual)
    if not existe:
        registrado = await ServicioModalidadContractual.agregar_registro(modalidad_contractual)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La modalidad contractual {modalidad_contractual.modalidad} ya está resgistrada")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_modalidad_contractual(modalidad_contractual:  ModalidadContractualPutSchema, response: Response):
    existe = await ServicioModalidadContractual.buscar_por_id(modalidad_contractual.id)
    if existe:
        actualizado = await ServicioModalidadContractual.agregar_registro(modalidad_contractual)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_modalidad_contractual(id: str, response: Response):
    modalidad_contractual = await ServicioModalidadContractual.buscar_por_id(id)
    if modalidad_contractual:
        eliminado = await ServicioModalidadContractual.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
