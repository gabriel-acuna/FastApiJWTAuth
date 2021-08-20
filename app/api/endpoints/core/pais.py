from app.schemas.core.PaisSchema import PaisSchema
from typing import List
from app.services.core.ServicioPais import ServicioPais
from fastapi import APIRouter, HTTPException, Depends
from app.services.auth import ServicioToken

router = APIRouter(prefix="/paises")


@router.get("/", response_model=List[PaisSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_paises():
    return await ServicioPais.listar()


@router.get("/{id}", response_model= PaisSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def obtener_pais(id: int):
    pais = await ServicioPais.buscar_por_id(id)
    if not pais:
        raise HTTPException(status_code=404, detail="País no encontrado")
    return PaisSchema(**pais[0].__dict__)
   