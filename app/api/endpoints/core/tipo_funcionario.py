from app.services.core.ServicioTipoFuncionario import ServicioTipoFuncionario
from typing import List
from fastapi import APIRouter, HTTPException, Response, status, Depends
from app.schemas.core.TipoFuncionarioSchema import *
from app.schemas.Message import MessageSchema
from app.api.messages import *
from app.services.auth import ServicioToken


router = APIRouter(prefix="/tipos-funcionarios")


@router.get("/", response_model=List[TipoFuncionarioSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_tipos_funcionarios():
    return await ServicioTipoFuncionario.listar()


@router.get("/{id}", response_model=TipoFuncionarioSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obetner_tipo_funcionario(id: str):
    documento = await ServicioTipoFuncionario.buscar_por_id(id)
    if not documento:
        raise HTTPException(
            status_code=404, detail="Tipo funcionario no encontrado"
        )
    return TipoFuncionarioSchema(**documento[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_tipo_funcionario(response: Response, tipo_funcionario: TipoFuncionarioPostSchema):
    existe = await ServicioTipoFuncionario.existe(tipo_funcionario)
    if not existe:
        registrado = await ServicioTipoFuncionario.agregar_registro(tipo_funcionario)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El tipo funcionario {tipo_funcionario.tipo} ya está resgistrado")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_tipo_funcionario(response: Response, tipo_funcionario: TipoFuncionarioPutSchema):
    existe = await ServicioTipoFuncionario.buscar_por_id(tipo_funcionario.id)
    if existe:
        actualizado = await ServicioTipoFuncionario.actualizar_registro(tipo_funcionario)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_tipo_funcionario(id: str, response: Response):
    documento = await ServicioTipoFuncionario.buscar_por_id(id)
    if documento:
        eliminado = await ServicioTipoFuncionario.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
