from app.schemas.core.OrganigramaSchema import AreaOrganigrama
from app.schemas.Message import MessageSchema
from app.api.messages import *
from typing import List

from app.schemas.core.AreaInstitucionalSchema import *
from app.services.core.ServicioAreaInstitucion import ServicioAreaInstitucion
from fastapi import APIRouter, HTTPException, Body, Response, status, Depends
from app.services.auth import ServicioToken


router = APIRouter(prefix="/areas-institucionales")


@router.get("/",
            response_model= List[AreaInstitucionSchema],
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_areas_institucionales():
    return await ServicioAreaInstitucion.listar()


@router.get("/{id}",
            response_model=AreaInstitucionSchema,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_area(id:int):
    area = await ServicioAreaInstitucion.buscar_por_id(id)
    if not area:
        raise HTTPException(
            status_code=404, detail="Área institucional no encontrada")
    return AreaInstitucionSchema(**area[0].__dict__)


@router.get("/{estructura}/{id}/areas",
            response_model=AreaOrganigrama,
            dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_areas(estructura:int, id:int):
    params = { 'id_area': id, 'id_estructura': estructura}
    area =  await ServicioAreaInstitucion.obtener_subareas(params)
    if not area.area:
        raise HTTPException(
            status_code=404, detail="Área institucional no encontrada")
    return area


@router.post("/", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def registrar_area(response: Response, area: AreaInstitucionalPostSchema = Body(...)):
    existe = await ServicioAreaInstitucion.existe(area= area)
    if not existe:
        registrado = await ServicioAreaInstitucion.agregar_registro(area)
        if registrado:
            return MessageSchema(type="success", content=POST_SUCCESS_MSG)
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"El área {area.nombre} ya está resgistrada")


@router.put("/", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actualizar_area(response: Response, area: AreaInstitucionalPutSchema):
    existe = await ServicioAreaInstitucion.buscar_por_id(area.id)
    if existe:
        actualizado = await ServicioAreaInstitucion.actualizar_registro(area)
        if actualizado:
            return MessageSchema(type="success", content=PUT_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=PUT_WARNING_MSG)


@router.delete("/{id}", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def eliminar_area(id: int, response: Response):
    area = await ServicioAreaInstitucion.buscar_por_id(id)
    print(area)
    if area:
        eliminado = await ServicioAreaInstitucion.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content=DELETE_SUCCESS_MSG)

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type="warning", content=DELETE_WARNING_MSG)
