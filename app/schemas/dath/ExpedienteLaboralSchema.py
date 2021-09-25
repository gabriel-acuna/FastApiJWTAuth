from app.schemas.dath.DetalleExpedienteSchema import DetalleExpedienteSchema
from typing import List
from pydantic import BaseModel
from datetime import date


class ExpedienteLaboralSchema(BaseModel):
    id:str
    id_persona:str
    fecha_ingreso: date
    detalle: List[DetalleExpedienteSchema]
