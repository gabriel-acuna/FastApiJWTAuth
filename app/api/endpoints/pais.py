from typing import List
from fastapi import APIRouter, HTTPException
from app.models.core.modelos_principales import Pais
from app.schemas.core.PaisSchema import PaisSchema

router = APIRouter()


@router.get("/paises")
async def listar_paises():
    paises: List[PaisSchema] = []
    resultado = await Pais.listar()
    for pais in resultado:
        p = PaisSchema(**pais[0].__dict__)
        paises.append(p)
    return paises


@router.get("/paises/{id}")
async def obtener_pais(id: int):
    resultado = await Pais.obtener(id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Pais no encontrado")
    return PaisSchema(**resultado.__dict__)
