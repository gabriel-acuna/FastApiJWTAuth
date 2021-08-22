from app.services.core.ServicioCategoriaDocenteLOSEP import ServicioCategoriaDocenteLOSEP
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends
from app.schemas.Message import MessageSchema
from app.schemas.core.CategoriaDocenteLOSEPSchema import *
from app.api.messages import *
from app.services.auth import ServicioToken

router = APIRouter(prefix="/categorias-docentes-losep")


@router.get("/", response_model=List[CategoriaDocenteLOSEPSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_categorias_docentes():
    return await ServicioCategoriaDocenteLOSEP.listar()


@router.get("/{id}", response_model=CategoriaDocenteLOSEPSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obetner_categoria_docente(id: str):
    documento = await ServicioCategoriaDocenteLOSEP.buscar_por_id(id)
    if not documento:
        raise HTTPException(
            status_code=404, detail="Categoría de docente LOSEP no encontrada"
        )
    return CategoriaDocenteLOSEPSchema(**documento[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_categoria_docente(response: Response, categoria_docente: CategoriaDocenteLOSEPPostSchema):
    existe = await ServicioCategoriaDocenteLOSEP.existe(categoria_docente)
    if not existe:
        registrado = await ServicioCategoriaDocenteLOSEP.agregar_registro(categoria_docente)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La categoría de docente LOES {categoria_docente.categoria_docente} ya está resgistrada")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_categoria_docente(response: Response, categoria_docente: CategoriaDocenteLOSEPPutSchema ):
    existe = await ServicioCategoriaDocenteLOSEP.buscar_por_id(categoria_docente.id)
    if existe:
        actualizado = await ServicioCategoriaDocenteLOSEP.actualizar_registro(categoria_docente)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_categoria_docente(id: str, response: Response):
    documento = await ServicioCategoriaDocenteLOSEP.buscar_por_id(id)
    if documento:
        eliminado = await ServicioCategoriaDocenteLOSEP.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
