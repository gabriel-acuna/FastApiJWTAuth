from app.schemas.dath.InformacionPersonalSchema import InformacionPersonalPostSchema, InformacionPersonalPutSchema, InformacionPersonalSchema
from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List
from app.services.dath.ServicioInformacionPersonal import ServicioInformacionPersonal
from fastapi import APIRouter, HTTPException, Body, Response, Depends,status
from app.services.auth import ServicioToken


router = APIRouter(prefix="/personal")

@router.get("/",
    response_model=List[InformacionPersonalSchema],
    dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_personal():
    return await ServicioInformacionPersonal.listar()

@router.get("/{id}",
    response_model=InformacionPersonalSchema,
    dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_persona(id:str):
    persona = await ServicioInformacionPersonal.buscar_por_id(id=id)
    if not persona:
        raise HTTPException(
            status_code=404, detail="Información personal no encontrada")
    return persona

@router.post("/",
    response_model=MessageSchema,
    status_code=201,
    dependencies=[Depends(ServicioToken.JWTBearer())])
async def resgitrar_informacion_personal(persona: InformacionPersonalPostSchema, response: Response, status_code=201, ):
    existe = await ServicioInformacionPersonal.existe(**{
        'id':persona.identificacion,
        'correo_institucional':persona.correo_institucional })
    if not existe:
        registrado = await ServicioInformacionPersonal.agregar_registro(persona)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La identificación {persona.identificacion} o el correo {persona.correo_institucional} ya está resgistrado")

@router.put("/{id}",
    response_model=MessageSchema,
    dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_informacion_personal(id:str, persona: InformacionPersonalPutSchema, response: Response):
    existe = await ServicioInformacionPersonal.existe(**{
        'id':id,
        'correo_institucional':persona.correo_institucional })
    if existe:
        actualizado = await ServicioInformacionPersonal.actualizar_registro(
            persona=persona, id=id
        )
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)