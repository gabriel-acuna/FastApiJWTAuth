from app.schemas.dath.ExpedienteLaboralSchema import ExpedienteLaboralSchema
from app.schemas.dath import DetalleExpedienteSchema
from app.schemas.dath.DetalleExpedienteSchema import *
from app.schemas.Message import *
from app.api.messages import *
from typing import List, Union
from app.services.dath.ServicioExpedienteLaboral import ServicioExpedienteLaboral
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken

router = APIRouter(prefix="/expediente-laboral")


@router.get("/{id_persona}",
    response_model=ExpedienteLaboralSchema,
    dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_expediente_persona(id_persona:str):
    return await ServicioExpedienteLaboral.listar(id_persona=id_persona)


@router.get("detalle/{id}",
    response_model=DetalleExpedienteSchema,
    dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_expediente_persona(id:str):
    expediente = await ServicioExpedienteLaboral.buscar_por_id(id=id)
    if not expediente:
        raise HTTPException(
            status_code=404, detail="Información laboral no encontrada")
    return expediente

@router.post("profesor/{id_persona}",
    response_model=MessageSchema,
    dependencies=[Depends(ServicioToken.JWTBearer())])
async def resgitrar_detalle_expediente_profesor(id_persona:str, expediente: DetalleExpedienteProfesorPostSchema, response: Response, status_code=201, ):
    
    registrado = await ServicioExpedienteLaboral.agregar_registro(id_persona=id_persona, detalle_expediente=expediente)
    if registrado:
        return MessageSchema(type="success", content=POST_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)
    

@router.post("funcionario/{id_persona}",
response_model=MessageSchema,
dependencies=[Depends(ServicioToken.JWTBearer())])
async def resgitrar_detalle_expediente_funcionario(id_persona:str, expediente: DetalleExpedienteFuncionarioPostSchema, response: Response, status_code=201, ):
    
    registrado = await ServicioExpedienteLaboral.agregar_registro(id_persona=id_persona, detalle_expediente=expediente)
    if registrado:
        return MessageSchema(type="success", content=POST_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)

@router.put("/",
    response_model=MessageSchema,
    dependencies=[Depends(ServicioToken.JWTBearer())]
)
async def actualiazar_detalle_expediente(
    response: Response,
    detalle_expediente:Union[DetalleExpedienteProfesorPutSchema, DetalleExpedienteFuncionarioPutSchema]):
    actualizado = await ServicioExpedienteLaboral.actualizar_registro(detalle_expediente= detalle_expediente)
    if actualizado:
         return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG) 
    
@router.delete("/{id}",
    response_model=MessageSchema,
    dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_item_expediente(id:str, response: Response):
    existe = await ServicioExpedienteLaboral.buscar_por_id(id)
    if existe:
        eliminado = await ServicioExpedienteLaboral.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)