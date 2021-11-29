from datetime import date
from typing import Optional
from pydantic import BaseModel
from app.schemas.core.PaisSchema import PaisSchema
import enum

from pydantic.fields import Field

class TipoCertificado(str, enum.Enum):
    ASISTENCIA = "ASISTENCIA"
    APROBACION = "APROBACIÓN"

class CapacitacionSchema(BaseModel):
    id:str
    id_persona:str
    tipo_evento:str
    institucion_organizadora:str
    funcion_evento: Optional[str]
    pais: PaisSchema
    lugar:str
    horas: str
    inicio: date
    fin: date
    tipo_certificado: TipoCertificado
    url: Optional[str]

class CapacitacionPostSchema(BaseModel):
    id_persona:str = Field(...)
    tipo_evento:str = Field(...)
    institucion_organizadora:str = Field(...)
    funcion_evento: Optional[str]
    pais: str
    lugar:str = Field(...)
    horas: int = Field(...)
    inicio: date = Field(...)
    fin: date = Field(...)
    tipo_certificado: TipoCertificado
    url: Optional[str]


class CapacitacionPutSchema(BaseModel):
    tipo_evento:str = Field(...)
    institucion_organizadora:str = Field(...)
    funcion_evento: Optional[str]
    pais: str
    lugar:str = Field(...)
    horas: int = Field(...)
    inicio: date = Field(...)
    fin: date = Field(...)
    tipo_certificado: TipoCertificado
    url: Optional[str]