from pydantic import BaseModel, Field
from datetime import date

class MeritoDistincionSchema(BaseModel):
    id:str
    id_persona: str
    titulo: str
    institucion_asupiciante: str
    funcion: str
    fecha_inicio: date
    fecha_fin: date

class MeritoDistincionPostSchema(BaseModel):
    id_persona: str = Field(...)
    titulo: str = Field(...)
    institucion_asupiciante: str  = Field(...)
    funcion: str = Field(...)
    fecha_inicio: date = Field(...)
    fecha_fin: date = Field(...)

class MeritoDistincionPustSchema(BaseModel):
    id:str = Field(...)
    titulo: str = Field(...)
    institucion_asupiciante: str  = Field(...)
    funcion: str = Field(...)
    fecha_inicio: date = Field(...)
    fecha_fin: date = Field(...)