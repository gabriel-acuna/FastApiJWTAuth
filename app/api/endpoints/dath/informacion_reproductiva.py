from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioInformacionReproductiva import ServicioInformacionReproductiva, InformacionReproductivaSchema, InformacionReproductivaPutSchema, InformacionReproductivaPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/informacion-reproductiva")


@router.get("/personal/{id_persona}",
            response_model=List[InformacionReproductivaSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_informacion_reproductiva_persona(id_persona: str):
    return await ServicioInformacionReproductiva.listar_por_persona(id_persona)


@router.get("/{id}",
            response_model=List[InformacionReproductivaSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_informacion_reproductiva(id: str):
    informacion_reproductiva = await ServicioInformacionReproductiva.buscar_por_id(id)
    if not informacion_reproductiva:
        raise HTTPException(
            status_code=404, detail="Registro no encontrado")
    return informacion_reproductiva


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_informacion_reproductiva(informacion_reproductiva: InformacionReproductivaPostSchema, response: Response):
    existe = await ServicioInformacionReproductiva.existe(informacion_reproductiva)
    if not existe:
        registrado = await ServicioInformacionReproductiva.agregar_registro(informacion_reproductiva)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La información reproductiva ya está resgistrada")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_informacion_reproductiva(informacion_reproductiva:  InformacionReproductivaPutSchema, response: Response):
    existe = await ServicioInformacionReproductiva.buscar_por_id(informacion_reproductiva.id)
    if existe:
        actualizado = await ServicioInformacionReproductiva.actualizar_registro(informacion_reproductiva)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_informacion_reproductiva(id: str, response: Response):
    informacion_reproductiva = await ServicioInformacionReproductiva.buscar_por_id(id)
    if informacion_reproductiva:
        eliminado = await ServicioInformacionReproductiva.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
