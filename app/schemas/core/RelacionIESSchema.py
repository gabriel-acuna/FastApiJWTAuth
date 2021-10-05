from datetime import datetime
from app.schemas.validaciones import es_no_numerico, longitud_maxima
from pydantic import BaseModel, Field, validator


class RelacionIESSchema(BaseModel):
    id: str
    relacion: str
    registrado_en: datetime
    actualizado_en: datetime


class RelacionIESPostSchema(BaseModel):
    relacion: str = Field(...)

    @validator('relacion')
    def relacion_longitud_maxima(cls, value):
        r = longitud_maxima(50, value, 8)
        if r and es_no_numerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "relacion": "NOMBRAMIENTO"
            }
        }


class RelacionIESPutSchema(BaseModel):
    id: str = Field(...)
    relacion: str = Field(...)

    @validator('relacion')
    def relacion_longitud_maxima(cls, value):
        r = longitud_maxima(50, value, 8)
        if r and es_no_numerico(value):
            return value
