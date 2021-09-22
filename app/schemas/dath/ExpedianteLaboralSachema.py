from app.models.dath.modelos import DetalleExpedianteLaboral
from typing import List
from pydantic import BaseModel


class ExpedienteLaboralSchema(BaseModel):
    id:str
    id_persona:str
    detalle: List[DetalleExpedianteLaboral]