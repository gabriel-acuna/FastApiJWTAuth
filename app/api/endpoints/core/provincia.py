from app.schemas.core.CantonSchema import CantonSchema
from app.schemas.core.ProvinciaSchema import ProvinciaSchema
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.services.core.ServicioProvincia import ServicioProvincia
from app.services.auth import ServicioToken


router = APIRouter(prefix="/provincias")


@router.get("/", response_model=List[ProvinciaSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_provincias():
    return await ServicioProvincia.listar()


@router.get("/{id}", response_model=ProvinciaSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_provincias(id: int):
    provincia = await ServicioProvincia.buscar_por_id(id)
    if not provincia:
        raise HTTPException(status_code=404, detail="Provincia no encontrada")
    return ProvinciaSchema(**provincia[0].__dict__)


@router.get("/{id}/cantones", response_model=List[CantonSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_cantones_por_provincia(id: int):
    cantones = await ServicioProvincia.listar_cantones_por_provincia(id_provincia=id)
    if not cantones:
        raise HTTPException(
            status_code=404, detail="La provincia no se encontró o no tiene cantones registrados")
    return cantones
