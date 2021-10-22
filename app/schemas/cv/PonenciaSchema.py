from pydantic import BaseModel, Field
from datetime import date

class PonenciaSchema(BaseModel):
    id: str
    id_persona: str
    tema: str
    institucion_organizadora: str
    evento: str
    caracter: str
    lugar : str
    fecha: date 


class PonenciaPostSchema(BaseModel):
    id_persona: str = Field(...)
    tema: str = Field(...)
    institucion_organizadora: str = Field(...)
    evento: str = Field(...)
    caracter: str = Field(...)
    lugar : str = Field(...)
    fecha: date = Field(...)

class PonenciaPutSchema(BaseModel):
    id: str = Field(...)
    tema: str = Field(...)
    institucion_organizadora: str = Field(...)
    evento: str = Field(...)
    caracter: str = Field(...)
    lugar : str = Field(...)
    fecha: date = Field(...)