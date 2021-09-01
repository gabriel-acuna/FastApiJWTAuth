from datetime import datetime
from app.schemas.validaciones import es_no_numerico, longitud_maxima
from pydantic import BaseModel, Field, validator


class NivelEducativoSchema(BaseModel):
    id: str
    nivel: str
    registrado_en: datetime
    actualizado_en: datetime


class NivelEducativoPostSchema(BaseModel):
    nivel: str = Field(...)

    @validator("nivel")
    def tiempo_dedicacion_maxima_longitud(cls, value):
        r = longitud_maxima(50, value, 12)
        if r and es_no_numerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "nivel": "TERCER NIVEL"
            }
        }


class NivelEducativoPutSchema(BaseModel):
    id: str = Field(...)
    nivel: str = Field(...)

    @validator("nivel")
    def tiempo_dedicacion_maxima_longitud(cls, value):
        r = longitud_maxima(50, value, 12)
        if r and es_no_numerico(value):
            return value
