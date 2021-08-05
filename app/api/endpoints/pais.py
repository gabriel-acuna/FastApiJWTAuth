from app.schemas.core.PaisSchema import PaisSchema
from typing import List
from app.services.core.ServicioPais import ServicioPais
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/paises", response_model=List[PaisSchema])
async def listar_paises():
    return await ServicioPais.listar()


@router.get("/paises/{id}", response_model= PaisSchema)
async def obtener_pais(id: int):
    pais = await ServicioPais.buscar_por_id(id)
    if not pais:
        raise HTTPException(status_code=404, detail="País no encontrado")
    return PaisSchema(**pais[0].__dict__)
   