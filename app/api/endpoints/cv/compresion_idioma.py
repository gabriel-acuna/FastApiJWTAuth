from app.schemas.cv.ComprensionIdiomaSchema import *
from app.models.cv.modelos import ComprensionIdioma
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken
from app.schemas.Message import MessageSchema
from typing import List
from app.api.messages import *
from app.services.cv.ServicioComprensionIdioma import ServicioComprensionIdioma


router = APIRouter(
    prefix="/idiomas"
)


@router.get("/persona/{id_persona}",
            response_model=List[ComprensionIdiomaSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def listar_idiomas(id_persona: str):
    return await ServicioComprensionIdioma.listar(id_persona=id_persona)


@router.get("/{id}",
            response_model=ComprensionIdiomaSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())]
            )
async def obtener_idioma(id: str):
    idioma = await ServicioComprensionIdioma.buscar_por_id(id=id)
    if not idioma:
        raise HTTPException(
            status_code=404, detail="Idioma no encontrado"
        )
    return idioma


@router.post("/", response_model=MessageSchema,
             status_code=201,
             dependencies=[Depends(ServicioToken.JWTBearer())])
async def registar_idioma(response: Response, idioma: ComprensionIdiomaPostSchema = Body(...)):
    existe = await ServicioComprensionIdioma.existe(idioma)
    if not existe:
        registrado = await ServicioComprensionIdioma.agregar_registro(idioma)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La capacitación ya está resgistrada")


@router.put("/", response_model=MessageSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_idioma(response: Response, idioma: ComprensionIdiomaPutSchema = Body(...)):
    actualizado = await ServicioComprensionIdioma.actualizar_registro(idioma)
    if actualizado:
        return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)


@router.delete("/{id}",
               response_model=MessageSchema,
               dependencies=[Depends(ServicioToken.JWTBearer())]
               )
async def eliminar_idioma(id: str, response: Response):
    idioma = await ServicioComprensionIdioma.buscar_por_id(id)
    if idioma:
        eliminado = await ServicioComprensionIdioma.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
