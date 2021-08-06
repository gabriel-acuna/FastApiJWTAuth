from typing import List
from app.schemas.core.CantonSchema import CantonSchema
from app.services.core.ServicioCanton import ServicioCanton
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/cantones")

@router.get("/", response_model=List[CantonSchema])
async def listar_cantones():
    return await ServicioCanton.listar()

@router.get("/{id}", response_model= CantonSchema)
async def obtener_canton(id:int):
    canton = await ServicioCanton.buscar_por_id(id)
    if not canton:
        raise HTTPException(status_code=404, detail="Cantón no encontrado")
    return CantonSchema(**canton[0].__dict__)
