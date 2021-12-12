from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List, Optional
from app.services.dath.ServicioServidorDesvinculado import ServicioServidorDesvinculado, ServidorDesvinculadoSchema, ServidorDesvinculadoPutSchema, ServidorDesvinculadoPostSchema
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/servidores-desvinculados")


@router.get("/",
            response_model=List[ServidorDesvinculadoSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_estados_sumarios(año:int, mes: Optional[int]):
    if mes:
        return await ServicioServidorDesvinculado.listar_por_año_mes(año, mes)
    return await ServicioServidorDesvinculado.listar_por_año(año)


@router.get("/{id}",
            response_model=List[ServidorDesvinculadoSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_servidor_desvinculado(id: str):
    servidor_desvinculado = await ServicioServidorDesvinculado.buscar_por_id(id)
    if not servidor_desvinculado:
        raise HTTPException(
            status_code=404, detail="Registro no encontrado")
    return servidor_desvinculado


@router.post("/",
             response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_servidor_desvinculado(servidor_desvinculado: ServidorDesvinculadoPostSchema, response: Response):
    existe = await ServicioServidorDesvinculado.existe(servidor_desvinculado)
    if not existe:
        registrado = await ServicioServidorDesvinculado.agregar_registro(servidor_desvinculado)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La desvinculación del servidor ya está resgistrada")


@router.put("/",
            response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_servidor_desvinculado(servidor_desvinculado:  ServidorDesvinculadoPutSchema, response: Response):
    existe = await ServicioServidorDesvinculado.buscar_por_id(servidor_desvinculado.id)
    if existe:
        actualizado = await ServicioServidorDesvinculado.actualizar_registro(servidor_desvinculado)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_servidor_desvinculado(id: str, response: Response):
    servidor_desvinculado = await ServicioServidorDesvinculado.buscar_por_id(id)
    if servidor_desvinculado:
        eliminado = await ServicioServidorDesvinculado.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
