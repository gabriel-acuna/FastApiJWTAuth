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

    @validator('discpacidad')
    def discapacidad_longitud_maxima(cls, value):
        longitud_maxima(30, value)

    class Config:
        schema_extra = {
            "discapacidad": {
                "discapacidad": "AUDITIVA"
            }
        }


class DiscapacidadPutSchema(BaseModel):
    id: str = Field(...)
    discapacidad: str = Field(...)

    @validator('discpacidad')
    def discapacidad_longitud_maxima(cls, value):
        longitud_maxima(30, value)
