from app.schemas.core.CampoEducativoSchema import CampoEducativoEspecificoPostSchema, CampoEducativoEspecificoPutSchema, CampoEducativoEspecificoSchema
from app.services.core.ServicioCampoEducativoEspecifico import ServicioCampoEducativoEspecifico
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends, Body
from app.schemas.core.TipoFuncionarioSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *
from app.services.auth import ServicioToken

router = APIRouter(prefix="/campos-especificos")


@router.get("/", response_model=List[CampoEducativoEspecificoSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_campos_estudios_detallados():
    return await ServicioCampoEducativoEspecifico.listar()

@router.get("/${id}",  response_model=CampoEducativoEspecificoSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_campo(id:str):
    campo = await ServicioCampoEducativoEspecifico.buscar_por_id(id)
    if not campo:
        raise HTTPException(
            status_code=404, detail="Campo no encontrado"
        )
    return campo


@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_campo(response: Response, campo: CampoEducativoEspecificoPostSchema = Body(...)):
    existe = await ServicioCampoEducativoEspecifico.existe(campo)
    if not existe:
        registrado = await ServicioCampoEducativoEspecifico.agregar_registro(campo)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El campo de estudio específico ya está resgistrado")


@router.put("/", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_campo(response: Response, campo:CampoEducativoEspecificoPutSchema = Body(...)):
    actualizado = await ServicioCampoEducativoEspecifico.actualizar_registro(campo)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_campo(id: str, response: Response):
    campo = await ServicioCampoEducativoEspecifico.buscar_por_id(id)
    if campo:
        eliminado = await ServicioCampoEducativoEspecifico.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
