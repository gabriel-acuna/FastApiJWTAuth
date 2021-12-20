from pydantic import BaseModel, Field
from datetime import date


class InformacionReproductivaSchema(BaseModel):
    id: str
    id_persona: str
    estado: str
    inicio: date
    fin: date


class InformacionReproductivaPostSchema(BaseModel):
    id_persona: str = Field(...)
    estado: str = Field(...)
    inicio: date = Field(...)
    fin: date = Field(...)

class InformacionReproductivaPutSchema(BaseModel):
    id: str = Field(...)
    estado: str = Field(...)
    inicio: date = Field(...)
    fin: date = Field(...)