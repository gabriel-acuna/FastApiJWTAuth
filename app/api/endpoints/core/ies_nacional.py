from app.schemas.core.IESNacionalSchema import *
from app.services.core.ServicioIES import ServicioIES
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends, Body
from app.schemas.core.TipoFuncionarioSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *
from app.services.auth import ServicioToken

router = APIRouter(prefix="/iess")


@router.get("/", response_model=List[IESNacionalSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_ies_nacionales():
    return await ServicioIES.listar()


@router.get("/${id}",  response_model=IESNacionalSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_ies_nacional(id:str):
    ies = await ServicioIES.buscar_por_id(id)
    if not ies:
        raise HTTPException(
            status_code=404, detail="IES no encontrada"
        )
    return ies

@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_ies(response: Response, ies: IESNacionalPostSchema = Body(...)):
    existe = await ServicioIES.existe(ies)
    if not existe:
        registrado = await ServicioIES.agregar_registro(ies)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La IES {ies.institucion} ya está resgistrado")


@router.put("/", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_ies(response: Response, ies: IESNacionalPutSchema = Body(...)):
    actualizado = await ServicioIES.actualizar_registro(ies)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_ies(id: str, response: Response):
    ies = await ServicioIES.buscar_por_id(id)
    if ies:
        eliminado = await ServicioIES.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
