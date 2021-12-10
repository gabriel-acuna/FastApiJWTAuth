from pydantic import BaseModel, Field
from datetime import date


class InformacionReproductivaSchema(BaseModel):
    id: str
    id_persona: str
    estado: str
    incio: date
    fin: date


class InformacionReproductivaPostSchema(BaseModel):
    id_persona: str = Field(...)
    estado: str = Field(...)
    incio: date = Field(...)
    fin: date = Field(...)

class InformacionReproductivaPutSchema(BaseModel):
    id: str = Field(...)
    estado: str = Field(...)
    incio: date = Field(...)
    fin: date = Field(...)