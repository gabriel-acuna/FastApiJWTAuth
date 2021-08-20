from app.services.core.ServicioCategoriaContratoProfesor import ServicioCategoriaContratoProfesor
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends
from app.schemas.Message import MessageSchema
from app.schemas.core.CategoriaContratoProfesorSchema import *
from app.api.messages import *
from app.services.auth import ServicioToken

router = APIRouter(prefix="/categorias-contrato-profesores")


@router.get("/", response_model=List[CategoriaContratoProfesorSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_categorias_contratos_profesores():
    return await ServicioCategoriaContratoProfesor.listar()


@router.get("/{id}", response_model=CategoriaContratoProfesorSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obetner_categoria_contrato_profesor(id: str):
    documento = await ServicioCategoriaContratoProfesor.buscar_por_id(id)
    if not documento:
        raise HTTPException(
            status_code=404, detail="Categoría de contrato profesor no encontrada"
        )
    return CategoriaContratoProfesorSchema(**documento[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_categoria_contrato_profesor(response: Response, categoria_contrato: CategoriaContratoProfesorSchema):
    existe = await ServicioCategoriaContratoProfesor.existe(categoria=categoria_contrato)
    if not existe:
        registrado = await ServicioCategoriaContratoProfesor.agregar_registro(categoria=categoria_contrato)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La categoría de contarto profesor {categoria_contrato.categoria_contrato} ya está resgistrada")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_categoria_contrato_profesor(response: Response, categoria_contrato: CategoriaContratoProfesorPostSchema):
    existe = await ServicioCategoriaContratoProfesor.buscar_por_id(categoria_contrato.id)
    if existe:
        actualizado = await ServicioCategoriaContratoProfesor.actualizar_registro(categoria_contrato)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_categoria_contrato_profesor(id: str, response: Response):
    documento = await ServicioCategoriaContratoProfesor.buscar_por_id(id)
    if documento:
        eliminado = await ServicioCategoriaContratoProfesor.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
