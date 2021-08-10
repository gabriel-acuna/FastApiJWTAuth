from datetime import datetime
from app.models.core.modelos_principales import Nacionalidad
from app.schemas.validaciones import longitud_maxima
from pydantic import BaseModel, Field, validator


class PaisSchema(BaseModel):
    id: str
    pais: str
    nacionalidad: str
    registrado_en: datetime
    actualizado_en: datetime


class PaisPostSchema(BaseModel):
    pais: str = Field(...)
    nacionalidad: str = Field(...)

    @validator('pais')
    def pais_longitud_maxima(cls, value):
        return longitud_maxima(120, value)

    @validator('nacionalidad')
    def nacionalidad_longitud_maxima(cls, value):
        longitud_maxima(120, value)

    class Config:
        schema_extra = {
            "example": {
                "pais": "ECUADOR",
                "nacionalidad": "ECUATORIANA"
            }
        }


class PaisPutSchema(BaseModel):
    id: str = Field(...)
    pais: str = Field(...)
    nacionalidad: str = Field(...)

    @validator('pais')
    def pais_longitud_maxima(cls, value):
        longitud_maxima(120, value)

    @validator('nacionalidad')
    def nacionalidad_longitud_maxima(cls, value):
        longitud_maxima(120, value)
