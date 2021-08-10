from datetime import datetime
from app.schemas.validaciones import longitud_maxima
from pydantic import BaseModel, Field, validator


class DiscapacidadSchema(BaseModel):
    id: str
    discapacidad: str
    registrado_en: datetime
    actualizado_en: datetime


class DiscapacidadPostSchema(BaseModel):
    discapacidad: str = Field(...)

    @validator('discapacidad')
    def discapacidad_longitud_maxima(cls, value):
        return longitud_maxima(30, value)

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
        return longitud_maxima(30, value)
