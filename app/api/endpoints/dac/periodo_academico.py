from app.schemas.dac.PeriodoAcademicoSchema import *
from app.services.dac.ServicioPeridoAcademico import *
from fastapi import APIRouter, HTTPException, Body, Response, Depends, status
from app.services.auth import ServicioToken
from app.schemas.Message import MessageSchema
from typing import List
from app.api.messages import *

router = APIRouter(
    prefix="/periodos-academicos"
)

@router.get("/", response_model=List[PeriodoAcademicoSchema], dependencies=[Depends(ServicioToken.JWTBearer())])
async def listar_campos_estudios_amplios():
    return ServicioPeriodoAcademico.listar()
