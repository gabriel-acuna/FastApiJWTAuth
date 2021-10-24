from app.schemas.cv.MeritoDistincionSchema import *
from app.models.cv.modelos import MeritoDistincion
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken
from app.schemas.Message import MessageSchema
from typing import List
from app.api.messages import *
from app.services.cv.ServicioMerito import ServicioMerito


router = APIRouter(
    prefix="/meritos-distinciones"
)


@router.get("/persona/{id_persona}",
            response_model=List[MeritoDistincionSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def listar_merito(id_persona: str):
    return await ServicioMerito.listar(id_persona=id_persona)


@router.get("/{id}",
            response_model=MeritoDistincionSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def obtener_merito(id: str):
    merito = await ServicioMerito.buscar_por_id(id=id)
    if not merito:
        raise HTTPException(
            status_code=404, detail="Mérito no encontrado"
        )
    return merito


@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_merito(response: Response, merito: MeritoDistincionPostSchema = Body(...)):
    existe = ServicioMerito.existe(merito)
    if not existe:
        registrado = await ServicioMerito.agregar_registro(merito)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La capacitación ya está resgistrada")


@router.put("/{id}", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_merito(id: str, response: Response, merito: MeritoDistincionPutSchema = Body(...)):
    actualizado = await ServicioMerito.actualizar_registro(id, merito)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_merito(id: str, response: Response):
    merito = await ServicioMerito.buscar_por_id(id)
    if merito:
        eliminado = await ServicioMerito.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
