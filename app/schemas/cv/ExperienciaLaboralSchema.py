from typing import Optional
from pydantic import BaseModel, Field
from datetime import date

class ExperienciaLaboralSchema(BaseModel):
    id: str
    id_persona: str
    empresa: str
    unidad_administrativa: str
    lugar: str
    cargo: str
    motivo_ingreso:str
    inicio: date
    fin: Optional[date]
    motivo_salida: Optional[str]

class ExperienciaLaboralPostSchema(BaseModel):
    id_persona: str = Field(...)
    empresa: str = Field(...)
    unidad_administrativa: str = Field(...)
    lugar: str = Field(...)
    cargo: str = Field(...)
    motivo_ingreso:str = Field(...)
    inicio: date = Field(...)
    fin: Optional[date] = Field()
    motivo_salida: Optional[str] = Field()

class ExperienciaLaboralPutSchema(BaseModel):
    id: str = Field(...)
    empresa: str = Field(...)
    unidad_administrativa: str = Field(...)
    lugar: str = Field(...)
    cargo: str = Field(...)
    motivo_ingreso:str = Field(...)
    inicio: date = Field(...)
    fin: Optional[date] = Field()
    motivo_salida: Optional[str] = Field()

