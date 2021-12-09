from pydantic import BaseModel, Field
from datetime import date


class InformacionReproductiva(BaseModel):
    id: str
    id_persona: str
    estado: str
    incio: date
    fin: date


class InformacionReproductivaPost(BaseModel):
    id_persona: str = Field(...)
    estado: str = Field(...)
    incio: date = Field(...)
    fin: date = Field(...)

class InformacionReproductivaPut(BaseModel):
    id: str = Field(...)
    estado: str = Field(...)
    incio: date = Field(...)
    fin: date = Field(...)