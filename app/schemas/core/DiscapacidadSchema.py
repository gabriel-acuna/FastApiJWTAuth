from datetime import datetime
from app.schemas.validaciones import es_no_numerico, longitud_maxima
from pydantic import BaseModel, Field, validator


class DiscapacidadSchema(BaseModel):
    id: str
    discapacidad: str
    registrado_en: datetime
    actualizado_en: datetime


class DiscapacidadPostSchema(BaseModel):
    discapacidad: str = Field(...)

    @validator('discapacidad')
    def discapacidad_validaciones(cls, value):
        r = longitud_maxima(30, value,5)
        if r and es_no_numerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "discapacidad": "AUDITIVA"
            }
        }


class DiscapacidadPutSchema(BaseModel):
    id: str = Field(...)
    discapacidad: str = Field(...)

    @validator('discapacidad')
    def discapacidad_longitud_maxima(cls, value):
        r = longitud_maxima(30, value,5)
        if r and es_no_numerico(value):
            return value
