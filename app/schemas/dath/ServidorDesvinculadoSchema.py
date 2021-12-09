from typing import Optional
from pydantic import BaseModel, Field
from app.schemas.dath.InformacionPersonalSchema import InformacionPersonalResumenSchema
from app.schemas.dath.RegimenLaboralSchema import RegimenLaboralSchema
from app.schemas.dath.ModalidadContractualSchema import ModalidadContractualSchema
from app.schemas.dath.MotivoDesvinculacionSchema import MotivoDesvinculacionSchema
from datetime import date

class ServidorDesvinculadoSchema(BaseModel):
    id:str
    institucion: str
    ruc: str
    persona: InformacionPersonalResumenSchema
    fecha_ingreso: date
    fecha_salida: date
    nombre_planta: str
    regimen: RegimenLaboralSchema
    modalidad: MotivoDesvinculacionSchema
    grupo_ocupacional: str
    pago_liquidacion: str
    fecha_pago: Optional[date]
    valor_cancelado: Optional[float]
    motivo_incumplimiento: str


class ServidorDesvinculadoPostSchema(BaseModel):
    persona: str = Field(...)
    fecha_ingreso: date = Field(...)
    fecha_salida: date = Field(...)
    nombre_planta: str = Field(...)
    regimen: int = Field(...)
    modalidad: str = Field(...)
    grupo_ocupacional: str =Field(...)
    pago_liquidacion: str = Field(...)
    fecha_pago: Optional[date] = Field()
    valor_cancelado: Optional[float] = Field()
    motivo_incumplimiento: str = Field(...)


class ServidorDesvinculadoPutSchema(BaseModel):
    id: str = Field(...)
    persona: str = Field(...)
    fecha_ingreso: date = Field(...)
    fecha_salida: date = Field(...)
    nombre_planta: str = Field(...)
    regimen: int = Field(...)
    modalidad: str = Field(...)
    grupo_ocupacional: str =Field(...)
    pago_liquidacion: str = Field(...)
    fecha_pago: Optional[date] = Field()
    valor_cancelado: Optional[float] = Field()
    motivo_incumplimiento: str = Field(...)
