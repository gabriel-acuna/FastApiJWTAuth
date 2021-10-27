from app.schemas.core.GradoSchema import  GradoPostSchema, GradoPutSchema, GradoSchema
from app.services.core.ServicioGrado import ServicioGrado
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends, Body
from app.schemas.core.TipoFuncionarioSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *
from app.services.auth import ServicioToken

router = APIRouter(prefix="/grados")


@router.get("/", response_model=List[GradoSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_grados():
    return await ServicioGrado.listar()


@router.get("/${id}",  response_model=GradoSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_grado(id:str):
    grado = await ServicioGrado.buscar_por_id(id)
    if not grado:
        raise HTTPException(
            status_code=404, detail="Grado no encontrado"
        )
    return grado

@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_grado(response: Response, grado: GradoPostSchema = Body(...)):
    existe = await ServicioGrado.existe(grado)
    if not existe:
        registrado = await ServicioGrado.agregar_registro(grado)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El grado {grado.grado} ya está resgistrado")


@router.put("/", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_grado(response: Response, grado: GradoPutSchema = Body(...)):
    actualizado = await ServicioGrado.actualizar_registro(grado)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_grado(id: str, response: Response):
    grado = await ServicioGrado.buscar_por_id(id)
    if grado:
        eliminado = await ServicioGrado.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
