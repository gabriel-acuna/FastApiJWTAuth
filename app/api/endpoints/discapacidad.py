from app.schemas.Message import MessageSchema
from typing import List
from app.schemas.core.DiscapacidadSchema import DiscapacidadPostSchema, DiscapacidadPutSchema, DiscapacidadSchema
from app.services.core.ServicioDiscapacidad import ServicioDiscapacidad
from fastapi import APIRouter, HTTPException, Body, Response, status

router = APIRouter(prefix="/discapacidades")


@router.get("/", response_model=List[DiscapacidadSchema])
async def listar_discapacidades():
    return await ServicioDiscapacidad.listar()


@router.get("/{id}", response_model=DiscapacidadSchema)
async def obtener_discapacidad(id: str):
    discapacidad = await ServicioDiscapacidad.buscar_por_id(id)
    if not discapacidad:
        raise HTTPException(
            status_code=404, detail="Discapacidad no encontrada")
    return DiscapacidadSchema(**discapacidad[0].__dict__)


@router.post("/", response_model=MessageSchema, status_code=201)
async def registar_discapacidad(response: Response, discapacidad: DiscapacidadPostSchema = Body(...)):
    existe = await ServicioDiscapacidad.existe(discapacidad=discapacidad)
    if not existe:
        registrado = await ServicioDiscapacidad.agregar_registro(discapacidad=discapacidad)
        if registrado:
            return MessageSchema(type="success", content="Se registró correctamente")

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content="Algo salió mal intente otra vez")
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La discapacidad {discapacidad.discapacidad} ya está resgistrada")


@router.put("/", response_model=MessageSchema)
async def actualizar_discapacidad(response: Response, discapacidad: DiscapacidadPutSchema = Body(...)):
    existe = await ServicioDiscapacidad.buscar_por_id(str(discapacidad.id))
    if existe:
        actualizado = await ServicioDiscapacidad.actualizar_registro(discapacidad)
        if actualizado:
            return MessageSchema(type="success", content="Se actualizó correctamente")

        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content="Algo salió mal intente otra vez")
    response.status_code = status.HTTP_202_ACCEPTED
    return MessageSchema(type="warning", content=f"La actualización no se pudo completar")


@router.delete("/{id}",response_model=MessageSchema)
async def eliminar_registro(id: str, response:Response):
    discapacidad = await ServicioDiscapacidad.buscar_por_id(id)
    if discapacidad:
        eliminado = await ServicioDiscapacidad.eliminar_registro(id)
        if eliminado:
            return MessageSchema(type="success", content="Se eliminó correctamente")
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content="Algo salió mal intente otra vez")
    return MessageSchema(type="warning", content="La eliminación no se pudo completar")
