from datetime import date
from pydantic import BaseModel, Field


class CapacitacionFacilitadorSchema(BaseModel):
    id: str
    id_persona: str
    funcion_evento: str
    institucion_organizadora: str
    lugar: str
    horas: int
    inicio: date
    fin: date
    certificado: str


class CapacitacionFacilitadorPostSchema(BaseModel):
    id_persona: str = Field(...)
    funcion_evento: str = Field(...)
    institucion_organizadora: str = Field(...)
    lugar: str = Field(...)
    horas: int = Field(...)
    inicio: date = Field(...)
    fin: date = Field(...)
    certificado: str = Field(...)


class CapacitacionFacilitadorPutSchema(BaseModel):
    id: str = Field(...)
    funcion_evento: str = Field(...)
    institucion_organizadora: str = Field(...)
    lugar: str = Field(...)
    horas: int = Field(...)
    inicio: date = Field(...)
    fin: date = Field(...)
    certificado: str = Field(...)
